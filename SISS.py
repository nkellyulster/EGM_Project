# Import libraries
import pandas as pd
import folium
import shapely
from shapely.geometry import Point
from haversine import haversine, Unit
import plotly.express as px
import numpy

# Import my functions
from functions import km_to_miles
#from functions import sustainable_schools
from functions import convert_distance_to_area
#from functions import remove_whitespace function not working correctly

###############################################################################

# Function to apply the conditional sustainability logic
def sustainable_schools(row):
    if (row['Urban/ Rural     '] == "RURAL" and row['total enrolment'] < 105) or (row['Urban/ Rural     '] == "URBAN" and row['total enrolment'] < 140):
        return 'Not Sustainable'
    else:
        return 'Sustainable'

###############################################################################
# Context

"""
The NI Department of Education publish school level enrolment data every year.
This is based on the school census that takes place every October.
The Primary School data for the most recent year, 2023/24, was published on 19th March 2024 
at https://www.education-ni.gov.uk/publications/school-enrolment-school-level-data-202324
"""

###############################################################################
# Import data files
# URL for the 2023/24 primary school level data saved in GitHub
primary_school_url = "https://github.com/nkellyulster/EGM_Project/raw/main/School%20level%20-%20primary%20schools%20-%20data%20202324.XLSX"

# URL for BT postcodes CSV saved in GitHub
bt_postcodes_url = "https://raw.githubusercontent.com/nkellyulster/EGM_Project/main/BT%20postcodes.csv"

# Read the bt_postcodes CSV file which contains Postcode / co-oridnates data
bt_postcodes = pd.read_csv(bt_postcodes_url)

# The following chunk reads in the url for the Primary School XLSX spreadsheet, 
# open the 'reference data' tab and skips the first 3 rows
schools = pd.read_excel(primary_school_url,
sheet_name = "reference data",
skiprows = 3)

# Read in the enrolment tab and skip the first 3 rows                        
enrolment = pd.read_excel(primary_school_url,
sheet_name = "Enrolments",
skiprows = 3)

# Removes the bt_postcodes_url and primary_school_url as they are no longer needed
del bt_postcodes_url
del primary_school_url

###############################################################################
# Data cleaning

# Retain only the DE Reference and the Total Enrolment columns from the enrolment df                        
selected_enrolment = enrolment.loc[:, ['DE ref', 'total enrolment']]

# Retain only the selected columns from the bt_postcodes df
selected_bt_postcodes = bt_postcodes.loc[:, ['Postcode', 'Latitude', 'Longitude']]

# Join the schools df and the enrolment df and drop 'DE ref' column from new df
all_schools = pd.merge(schools, selected_enrolment, how='inner', left_on='De ref', right_on='DE ref')
all_schools = all_schools.drop('DE ref', axis = 1)

# Join the schools and selected_bt_postcodes dfs using postcode and Postcode variables
merged_data = pd.merge(all_schools, selected_bt_postcodes, how='inner', left_on='postcode', right_on='Postcode')

# Remove unused columns from merged_data df
merged_data = merged_data.drop(['address 1', 'school type', 'district council (2014)', 'ward (2014)', 'DEA (2014)', 'Irish Medium School', 'Postcode'], axis=1)

# Function to remove leading and trailing whitespace
#merged_data.columns = merged_data.columns.str.strip()

################################################################################
# Spatial analysis
"""
This section of the code creates various distance calculations. The different 
calculations are as follows:
* the distance from each school to the nearest school
* the distance from each school to the nearest school in the same management type
* the distance from each school to the nearest school NOT in the same management type

All of these calculations will be created in one master dataframe and will then be
seperated out into smaller dataframes for ease of navigation and analysis.
"""

# Calculate distance to nearest school, the name of the nearest school, the 
# management type of the nearest school, distance to the nearest school in the 
# same management type, and the name of the nearest school in the same management type, 
# for each school

nearest_distances = []
nearest_schools = []
nearest_management_types = []
nearest_same_management_schools = []
nearest_same_management_distances = []

for idx, row in merged_data.iterrows():
    min_distance = float('inf')
    nearest_school = None
    nearest_management_type = None
    nearest_same_management_school = None
    nearest_same_management_distance = float('inf')
    
    for idx2, row2 in merged_data.iterrows():
        if idx != idx2:  # Exclude the current school
            distance = haversine((row['Latitude'], row['Longitude']), (row2['Latitude'], row2['Longitude']), unit=Unit.KILOMETERS)
            if distance < min_distance:
                min_distance = distance
                nearest_school = row2['school name']
                nearest_management_type = row2['management type']
            if row2['management type'] == row['management type'] and distance < nearest_same_management_distance:
                nearest_same_management_distance = distance
                nearest_same_management_school = row2['school name']
    
    # Append values to the lists inside the loop
    nearest_distances.append(min_distance)
    nearest_schools.append(nearest_school)
    nearest_management_types.append(nearest_management_type)
    nearest_same_management_distances.append(nearest_same_management_distance)
    nearest_same_management_schools.append(nearest_same_management_school)

# Add the columns to the merged_data DataFrame
merged_data['nearest_distance'] = nearest_distances
merged_data['nearest_school'] = nearest_schools
merged_data['nearest_management_type'] = nearest_management_types
merged_data['nearest_same_management_distance'] = nearest_same_management_distances
merged_data['nearest_same_management_school'] = nearest_same_management_schools

# This chunk finds the distance from each school to the nearest school not in the
# same management type, the name of the nearest school not in the same management 
# type and the management type of the nearest school not in the same management type

nearest_schools = []
nearest_distances = []
nearest_management_types = []

for idx, row in merged_data.iterrows():
    min_distance = float('inf')
    nearest_school = None
    nearest_management_type = None
    
    for idx2, row2 in merged_data.iterrows():
        if idx != idx2 and row['management type'] != row2['management type']:  # Exclude the current school and same management type
            distance = haversine((row['Latitude'], row['Longitude']), (row2['Latitude'], row2['Longitude']), unit=Unit.KILOMETERS)
            if distance < min_distance:
                min_distance = distance
                nearest_school = row2['school name']
                nearest_management_type = row2['management type']
    
    nearest_distances.append(min_distance)
    nearest_schools.append(nearest_school)
    nearest_management_types.append(nearest_management_type)

# Add the columns to the merged_data DataFrame
merged_data['nearest_distance_other_management'] = nearest_distances
merged_data['nearest_school_other_management'] = nearest_schools
merged_data['nearest_management_type_other_management'] = nearest_management_types

# Sustainability
# For a school to be deemed sustainable by the Department of Education it must 
# have more than 140 pupils for an Urban school and more than 105 pupils for a 
# Rural school. For this the custom 'sustainable' function is used.

merged_data['Sustainability'] = merged_data.apply(sustainable_schools, axis=1)

################################################################################
# Create new dataframes

# Define the bins for distance ranges
bins = [0, 1, 2.9, 4.9, 7.4, 9.9, float('inf')]
labels = ['<1', '1-2.9', '3-4.9', '5-7.4', '7.5-9.9', '>10']

# Count all schools
school_count = merged_data['total enrolment'].count()
school_count

# Count all schools by management type
management_type_count = merged_data.groupby(['management type']).size().reset_index(name='count')
management_type_count = management_type_count.sort_values(by='count', ascending=False)
management_type_count

# Count all schools by parliamentary constituency
management_type_count = merged_data.groupby(['constituency']).agg({'total enrolment': 'count'})
management_type_count = management_type_count.sort_values(by='total enrolment', ascending=False)
management_type_count

# Count all schools by management type & parliamentary constituency
management_type_constituency_count = merged_data.groupby(['constituency', 'management type']).size().reset_index(name='count')
management_type_constituency_count

# Total number of pupils
total_enrolment_sum = merged_data['total enrolment'].sum()
total_enrolment_sum

# Total number of pupils by management type
total_enrolment_by_management_type = merged_data.groupby('management type')['total enrolment'].sum()
total_enrolment_by_management_type_sorted = total_enrolment_by_management_type.sort_values(ascending=False)
total_enrolment_by_management_type

# Total number of pupils by parliamentary constituency
total_enrolment_constituency = merged_data.groupby('constituency')['total enrolment'].sum()
total_enrolment_constituency = total_enrolment_constituency.sort_values(ascending=False)
total_enrolment_constituency

# Total number of sustainable and unsutainable schools
sustainable_count = merged_data.groupby(['Sustainability']).agg({'total enrolment': 'count'})
sustainable_count['Percentage'] = (sustainable_count['total enrolment'] / school_count) * 100
sustainable_count

# Total number of pupils in unsustainable schools
sustainable_pupils = merged_data.groupby('Sustainability').agg({'total enrolment': 'sum'})
sustainable_pupils['Percentage'] = (sustainable_pupils['total enrolment'] / total_enrolment_sum) * 100

# Number of Catholic Maintained & Controlled Schools
count_catholic_maintained_controlled = merged_data[(merged_data['management type'] == 'Catholic Maintained') | (merged_data['management type'] == 'Controlled')]
count_catholic_maintained_controlled = count_catholic_maintained_controlled['total enrolment'].count()
count_catholic_maintained_controlled

percentage_schools_catholic_maintained_controlled = count_catholic_maintained_controlled / school_count
percentage_schools_catholic_maintained_controlled

# Number of pupils educated in Catholic Maintained & Controlled Schools
sum_catholic_maintained_controlled = merged_data[(merged_data['management type'] == 'Catholic Maintained') | (merged_data['management type'] == 'Controlled')]
sum_catholic_maintained_controlled = sum_catholic_maintained_controlled['total enrolment'].sum()
sum_catholic_maintained_controlled

percentage_enroled_catholic_maintained_controlled = sum_catholic_maintained_controlled / total_enrolment_sum
percentage_enroled_catholic_maintained_controlled

# Nearest School
nearest_school = merged_data.loc[:, ['De ref', 'school name', 'management type', 'constituency', 'total enrolment', 'nearest_school',
       'nearest_management_type']]

# Nearest school in the same management type
nearest_school_same_management = merged_data.loc[:, ['De ref', 'school name', 'management type', 'constituency', 'total enrolment', 'nearest_same_management_distance',
       'nearest_same_management_school']]

# Nearest school not in the same managment type
nearest_school_not_same_management = merged_data.loc[:, ['De ref', 'school name', 'management type', 'constituency', 'total enrolment', 'nearest_distance_other_management',
       'nearest_school_other_management', 'nearest_management_type_other_management']]
nearest_school_not_same_management = nearest_school_not_same_management.sort_values(by='nearest_distance_other_management', ascending=True)

# Roulston Cook
""" 
In their 2020 research "Isolated Together", Roulston & Cook used the Department
of Educatio  2018/19 primary school data "to identify pairs of primary schools 
consisting of one Controlled and one Maintained school, located in close proximity 
to each other but not in the vicinity of other schools of the same management 
type". The following chuck of code replicates this research. Full referencing
for this research is provided in the attached report.
"""

Roulston_Cook = merged_data[(merged_data['management type'] == 'Catholic Maintained') | (merged_data['management type'] == 'Controlled')]
Roulston_Cook = Roulston_Cook.loc[:, ['De ref', 'school name', 'town', 'management type', 'total enrolment', 'nearest_distance_other_management',
       'nearest_school_other_management', 'nearest_management_type_other_management', 'Sustainability']]
Roulston_Cook = Roulston_Cook.sort_values(by='nearest_distance_other_management', ascending=True)
Roulston_Cook = Roulston_Cook[(Roulston_Cook['Sustainability'] == 'Not Sustainable')]
Roulston_Cook.drop(columns=['Sustainability'], inplace=True)
Roulston_Cook = Roulston_Cook[(Roulston_Cook['nearest_distance_other_management'] <1.60934)]
duplicate_indices = Roulston_Cook[Roulston_Cook['school name'].isin(Roulston_Cook['nearest_school_other_management'])].index
Roulston_Cook.drop(duplicate_indices, inplace=True)
Roulston_Cook

# Strategically important small schools
strategically_important_small_schools = merged_data.loc[:, ['De ref', 'school name', 'management type', 'constituency', 'total enrolment', 'nearest_same_management_distance',
       'nearest_same_management_school', 'Sustainability']]
strategically_important_small_schools = strategically_important_small_schools[(strategically_important_small_schools['Sustainability'] == 'Not Sustainable')]
strategically_important_small_schools = strategically_important_small_schools[(strategically_important_small_schools['management type'] == 'Catholic Maintained') | (strategically_important_small_schools['management type'] == 'Controlled')]
strategically_important_small_schools.drop(columns=['Sustainability'], inplace=True)
strategically_important_small_schools = strategically_important_small_schools.sort_values(by='nearest_same_management_distance', ascending=False)

# Bin the distances into specified ranges
strategically_important_small_schools['distance_range'] = pd.cut(strategically_important_small_schools['nearest_same_management_distance'], bins=bins, labels=labels, right=False)

# Count occurrences in each bin
distance_counts = pd.DataFrame(strategically_important_small_schools['distance_range'].value_counts(sort=False).reindex(labels, fill_value=0))
distance_counts.reset_index(inplace=True)

strategically_important_small_schools = strategically_important_small_schools.head(20)
strategically_important_small_schools = strategically_important_small_schools.drop('distance_range', axis = 1)
strategically_important_small_schools

count_strategically_important_small_schools_constituency = strategically_important_small_schools.groupby(['management type']).size().reset_index(name='count')
count_strategically_important_small_schools_constituency = count_strategically_important_small_schools_constituency.sort_values(by='count', ascending=False)
count_strategically_important_small_schools_constituency

count_strategically_important_small_schools_management_type = strategically_important_small_schools.groupby(['constituency']).size().reset_index(name='count')
count_strategically_important_small_schools_management_type = count_strategically_important_small_schools_management_type.sort_values(by='count', ascending=False)
count_strategically_important_small_schools_management_type
################################################################################
# Charts


################################################################################
# Maps

# Create a geometry column by combining Longitude and Latitude
merged_data['geom'] = merged_data.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)

# Create a map centered at the mean Latitude and Longitude
m = folium.Map(location=[merged_data['Latitude'].mean(), merged_data['Longitude'].mean()], zoom_start=8)

# Add markers for each school
for idx, row in merged_data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['school name']).add_to(m)

# Save the map to an HTML file
m.save('map.html')
