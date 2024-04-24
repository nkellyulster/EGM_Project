###############################################################################
# Setup 

# Import libraries
import csv
import folium
import geopandas as gpd
import numpy as np
import pandas as pd
import plotly.express as px
from collections import defaultdict
from folium.plugins import MarkerCluster
from haversine import haversine
from haversine import haversine, Unit
from shapely.geometry import Point

# Import my functions
from functions import km_to_miles
from functions import sustainable_schools
from functions import convert_distance_to_area

###############################################################################
# Context

"""
The NI Department of Education publish school level enrolment data every year.
This is based on the school census that takes place every October.
The Primary School data for the most recent year, 2023/24, was published on 19th March 2024 
at https://www.education-ni.gov.uk/publications/school-enrolment-school-level-data-202324
For further detail see the README file
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
# opens the 'reference data' tab and skips the first 3 rows
schools = pd.read_excel(primary_school_url,
sheet_name = "reference data",
skiprows = 3)

# Reads in the enrolment tab and skip the first 3 rows                        
enrolment = pd.read_excel(primary_school_url,
sheet_name = "Enrolments",
skiprows = 3)

# Import GeoJSON file with parliamentary boundaries
constituency_boundaries = gpd.read_file("C:\\Users\\Niall\\Documents\\EGM_Project\\OSNI_Open_Data_-_50K_Boundaries_-_Parliamentary_Constituencies.geojson")

# Removes the bt_postcodes_url and primary_school_url as they are no longer needed
del bt_postcodes_url
del primary_school_url

################################################################################
# Previous years data
"""
The calcualtions in this script are all based on the most recent data published 
by the Department of Education (2023/24). It may be of use to others to look at 
other years enrolment data.

As of April 2024, enrolment data for schools is available as far back as 2009/10
on the Department of Education website at: 
https://www.education-ni.gov.uk/articles/school-enrolments-school-level-data
  
Should you wish to carry out this analysis on historic data simply uncomment the
line below which relates to the year that you want to analyse and comment out
the Import data files line which contains primary_school_url

There may be issues with data struture of files changing over the year so you 
should tke care when readin in the data that it the all_schools dataframe is
correct
"""
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/de/primary-schools-data-0910-supp-r.xlsx" #2009/10
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/de/primary-schools-data-1011-supp-inc-unfilled-r.xlsx" #2010/11
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/de/primary-schools-data-11-12-supp-inc-unfilled-places-r.xlsx" #2011/12
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/de/primary-schools-data-2012-13-supp-inc-unfilled-places-2.xlsx" #2012/13
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/de/primary-schools-data-2013-14-supp-inc-unfilled-places.xlsx" #2013/14
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/de/primary-schools-data-1415-supp-with-unfilled-places.xlsx" #2014/15
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/de/School%20level%20-%20primary%20schools%20data%201516%20supp_0.XLSX" #2015/16
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20primary%20schools%20data%201617%20supp.XLSX" #2016/17
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20primary%20schools%20data%20supp%201718.xlsx" #2017/18
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/education/Copy%20of%20School%20level%20-%20primary%20schools%20data%201819.XLSX" #2018/19
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20primary%20schools%20data%201920%20suppressed.XLSX" #2019/20
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20primary%20schools%20data%202020-21.xlsx" #2020/21
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20primary%20schools%20data%202122.XLSX" #2021/22
#primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20primary%20schools%20data%202223.XLSX" #2022/23

################################################################################
# Data cleaning

# Retain only the DE Reference and the Total Enrolment columns from the enrolment df   
# Creates a new df called selected_enrolment
selected_enrolment = enrolment.loc[:, ['DE ref', 'total enrolment']]

# Retain only the selected columns from the bt_postcodes df
# Creates a new df called selected_bt_postcodes
selected_bt_postcodes = bt_postcodes.loc[:, ['Postcode', 'Latitude', 'Longitude']]

# Join the schools df and the enrolment df and drop 'DE ref' column from new df
all_schools = pd.merge(schools, selected_enrolment, how='inner', left_on='De ref', right_on='DE ref')
all_schools = all_schools.drop('DE ref', axis = 1)

# Join the schools and selected_bt_postcodes dfs using postcode and Postcode variables
merged_data = pd.merge(all_schools, selected_bt_postcodes, how='inner', left_on='postcode', right_on='Postcode')

# This check is added to identify any schools which do not appear in the merged_data
# df becuase their school postcode does not appear in the bt_postcodes df
bt_postcodes_postcodes = selected_bt_postcodes['Postcode'].tolist()
rows_not_in_bt_postcodes = all_schools[~all_schools['postcode'].isin(bt_postcodes_postcodes)]

# The following 3 postcodes were identified from the rows_not_in_bt_postcodes df
# so their latitiude and logitude values were sourced from Google Maps
missing_postcodes = pd.DataFrame({
    'Postcode': ['BT13 3SY', 'BT4 3HJ', 'BT78 3GA', 'BT79 0GZ'],
    'Latitude': [54.615622286274096, 54.601342361930584, 54.512571453329244, 54.5993316600317],
    'Longitude': [-5.9826709693148885, -5.85227797613058, -7.469365801273217, -7.2545584724318095]
})

# Missing_postcodes df is appeneded to bottom of selecteD_bt_postcodes df
selected_bt_postcodes = selected_bt_postcodes._append(missing_postcodes, ignore_index=True)

# Rerun the process again
merged_data = pd.merge(all_schools, selected_bt_postcodes, how='inner', left_on='postcode', right_on='Postcode')
bt_postcodes_postcodes = selected_bt_postcodes['Postcode'].tolist()
rows_not_in_bt_postcodes = all_schools[~all_schools['postcode'].isin(bt_postcodes_postcodes)]

# At this point there is still one school missing. The issue has been caused with
# a `tab` rather than a single space in the postcode in the all_schools df. This 
# value will be replaced.
all_schools.replace('BT6  0AG', 'BT6 0AG', inplace=True)

# Rerun the process one final time
merged_data = pd.merge(all_schools, selected_bt_postcodes, how='inner', left_on='postcode', right_on='Postcode')
bt_postcodes_postcodes = selected_bt_postcodes['Postcode'].tolist()
rows_not_in_bt_postcodes = all_schools[~all_schools['postcode'].isin(bt_postcodes_postcodes)]
# There are now no longer any rows_not_in_bt_postcodes df and the number of rows
# (787) is the same in both the all_schools and merged_data dfs. Success!

# Remove unused columns from merged_data df
merged_data = merged_data.drop(['address 1', 'school type', 'district council (2014)', 'ward (2014)', 'DEA (2014)', 'Irish Medium School', 'Postcode'], axis=1)

# Write the merged_data df as a CSV
merged_data.to_csv("Outputs/1. merged_data.csv", index=False)

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

Calculate distance to nearest school, the name of the nearest school, the 
management type of the nearest school, distance to the nearest school in the 
same management type, and the name of the nearest school in the same management type, 
for each school

All distance calculations are give in km
"""

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

# Add the columns to the merged_data df
merged_data['nearest_distance'] = nearest_distances
merged_data['nearest_school'] = nearest_schools
merged_data['nearest_management_type'] = nearest_management_types
merged_data['nearest_same_management_distance'] = nearest_same_management_distances
merged_data['nearest_same_management_school'] = nearest_same_management_schools

"""
This chunk finds the distance from each school to the nearest school not in the
same management type, the name of the nearest school not in the same management 
type and the management type of the nearest school not in the same management type
"""

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
"""
For a school to be deemed sustainable by the Department of Education it must 
have more than 140 pupils for an Urban school and more than 105 pupils for a 
Rural school. For this the custom 'sustainable_schools' function is used.
Further information on sustainability is provided in the README file.
"""

merged_data['Sustainability'] = merged_data.apply(sustainable_schools, axis=1)

################################################################################
# Create new dataframes

# Define the bins for distance ranges
# Bins are created for the purposes of grouping data
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
constituency_count = merged_data.groupby(['constituency']).agg({'total enrolment': 'count'})
constituency_count = constituency_count.sort_values(by='total enrolment', ascending=False)
constituency_count

# Count all schools by management type & parliamentary constituency
management_type_constituency_count = merged_data.groupby(['constituency', 'management type']).size().reset_index(name='count')
management_type_constituency_count
# Writes this output as a CSV file
management_type_constituency_count.to_csv("Outputs/2. management_type_constituency_count.csv", index=False)

# Total number of pupils
total_enrolment_sum = merged_data['total enrolment'].sum()
total_enrolment_sum

# Total number of pupils by management type
total_enrolment_by_management_type = merged_data.groupby('management type')['total enrolment'].sum()
total_enrolment_by_management_type = pd.DataFrame(total_enrolment_by_management_type)
total_enrolment_by_management_type = total_enrolment_by_management_type.sort_values(by='total enrolment', ascending=False)
total_enrolment_by_management_type = total_enrolment_by_management_type_sorted.rename_axis('management type').reset_index()
total_enrolment_by_management_type
# Writes this output as a CSV file
total_enrolment_by_management_type.to_csv("Outputs/3. total_enrolment_by_management_type.csv", index=False)

# Total number of pupils by parliamentary constituency
total_enrolment_constituency = merged_data.groupby('constituency')['total enrolment'].sum()
total_enrolment_constituency = pd.DataFrame(total_enrolment_constituency)
total_enrolment_constituency = total_enrolment_constituency.sort_values(by='total enrolment', ascending=False)
total_enrolment_constituency = total_enrolment_constituency.rename_axis('constituency').reset_index()
total_enrolment_constituency
# Writes this output as a CSV file
total_enrolment_constituency.to_csv("Outputs/4. total_enrolment_constituency.csv", index=False)

# Total number of sustainable and unsutainable schools
sustainable_count = merged_data.groupby(['Sustainability']).agg({'total enrolment': 'count'})
sustainable_count['Percentage'] = (sustainable_count['total enrolment'] / school_count) * 100
sustainable_count

# Total number of pupils in unsustainable schools
sustainable_pupils = merged_data.groupby('Sustainability').agg({'total enrolment': 'sum'})
sustainable_pupils['Percentage'] = (sustainable_pupils['total enrolment'] / total_enrolment_sum) * 100
sustainable_pupils

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
# Finalises the nearest_school df by removing unnecessary columns
nearest_school = merged_data.loc[:, ['De ref', 'school name', 'management type', 'constituency', 'total enrolment', 'nearest_school',
       'nearest_management_type']]
nearest_school
# Writes this output as a CSV file
nearest_school.to_csv("Outputs/5. nearest_school.csv", index=False)

# Nearest school in the same management type
# Finalises the nearest_school_same_management df by removing unnecessary columns

nearest_school_same_management = merged_data.loc[:, ['De ref', 'school name', 'management type', 'constituency', 'total enrolment', 'nearest_same_management_distance',
       'nearest_same_management_school']]
nearest_school_same_management
# Writes this output as a CSV file
nearest_school_same_management.to_csv("Outputs/6. nearest_school_same_management.csv", index=False)

# Nearest school not in the same managment type
# Finalises the nearest_school_not_same_management df by removing unnecessary columns
nearest_school_not_same_management = merged_data.loc[:, ['De ref', 'school name', 'management type', 'constituency', 'total enrolment', 'nearest_distance_other_management',
       'nearest_school_other_management', 'nearest_management_type_other_management']]
nearest_school_not_same_management = nearest_school_not_same_management.sort_values(by='nearest_distance_other_management', ascending=True)
nearest_school_not_same_management
# Writes this output as a CSV file
nearest_school_not_same_management.to_csv("Outputs/6. nearest_school_not_same_management.csv", index=False)

# Roulston Cook
""" 
In their 2020 research "Isolated Together", Roulston & Cook used the Department
of Educatio  2018/19 primary school data "to identify pairs of primary schools 
consisting of one Controlled and one Maintained school, located in close proximity 
to each other but not in the vicinity of other schools of the same management 
type". The following chuck of code replicates this research. Full referencing
for this research is provided in the attached report.
"""

# As Catholic Maintained and Controlled schools acount for almsot 90% of pupils
# this analysis is carried out looking at only these two management types
Roulston_Cook = merged_data[(merged_data['management type'] == 'Catholic Maintained') | (merged_data['management type'] == 'Controlled')]
# Only required columns and analysis is retained
Roulston_Cook = Roulston_Cook.loc[:, ['De ref', 'school name', 'town', 'management type', 'total enrolment', 'nearest_distance_other_management',
       'nearest_school_other_management', 'nearest_management_type_other_management', 'Sustainability']]
Roulston_Cook = Roulston_Cook.sort_values(by='nearest_distance_other_management', ascending=True)
Roulston_Cook = Roulston_Cook[(Roulston_Cook['Sustainability'] == 'Not Sustainable')]
Roulston_Cook.drop(columns=['Sustainability'], inplace=True)
# Roulston Cook analysis only looked at schools "that were not withing one mile"
# of a school from the other management type so the data is filtered to only look
# at schools less than 1.60934km / 1 mile apart
Roulston_Cook = Roulston_Cook[(Roulston_Cook['nearest_distance_other_management'] <1.60934)]
# The duplicate_indicies was used to remove ans schools which appear from the 
# 'school name' column that have appeared in the 'nearest_school_other_management
# column as they will be duplicates.
duplicate_indices = Roulston_Cook[Roulston_Cook['school name'].isin(Roulston_Cook['nearest_school_other_management'])].index
Roulston_Cook.drop(duplicate_indices, inplace=True)
Roulston_Cook
# Writes this output as a CSV file
Roulston_Cook.to_csv("Outputs/7. Roulston_Cook.csv", index=False)

# Strategically important small schools
"""
This is the key section of the project.
This chuck filters for all schools that are not sustainable based on enrolment.
It filters out to retain only the Catholic Maintianed and the Controlled schools.
They are sorted in descending order by the distance to the nearest school in the 
same management type.
"""
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

# This next line counts th enumber of schools where the distance to the nearest
# school in a differnet management type is greater than 7.5km
greater_than_7500m = len(strategically_important_small_schools[strategically_important_small_schools['nearest_same_management_distance'] >= 7.5])

# This df selects only the schools where the distance to the nearest school in a
# different management type is greater then 7.5km
strategically_important_small_schools = strategically_important_small_schools.head(greater_than_7500m)
strategically_important_small_schools = strategically_important_small_schools.drop('distance_range', axis = 1)
strategically_important_small_schools
# Writes this output as a CSV file
strategically_important_small_schools.to_csv("Outputs/8. strategically_important_small_schools.csv", index=False)

# Counts the number of strategically important small schools by management type
count_strategically_important_small_schools_constituency = strategically_important_small_schools.groupby(['management type']).size().reset_index(name='count')
count_strategically_important_small_schools_constituency = count_strategically_important_small_schools_constituency.sort_values(by='count', ascending=False)
count_strategically_important_small_schools_constituency

# Counts the number of strategically important small schools by constituency
count_strategically_important_small_schools_management_type = strategically_important_small_schools.groupby(['constituency']).size().reset_index(name='count')
count_strategically_important_small_schools_management_type = count_strategically_important_small_schools_management_type.sort_values(by='count', ascending=False)
count_strategically_important_small_schools_management_type
# Writes this output as a CSV file
count_strategically_important_small_schools_management_type.to_csv("Outputs/9. count_strategically_important_small_schools_management_type.csv", index=False)

################################################################################
# Charts

# Bar chart of all schools by management type
fig = px.bar(management_type_count, x='management type', y='count',
             title='Number of Schools by Management Type',
             labels={'management type': 'Management Type', 'count': 'School Count'})
# Saves this output as a HTML file
fig.write_html('Outputs/Chart - school_count_by_management_type.html')

# Bar chart of sum all pupils by management type
fig = px.bar(total_enrolment_by_management_type, y='total enrolment', 
             title='Total Enrolment by Management Type', 
             labels={'management type': 'Management Type', 'total enrolment': 'Total Enrolment'})
# Saves this output as a HTML file
fig.write_html('Outputs/Chart - total_enrolment_by_management_type.html')

# Treemap of all schools by management type
fig = px.treemap(management_type_count, path=['management type'], values='count',
                 title='Number of Schools by Management Type')
# Saves this output as a HTML file
fig.write_html('Outputs/Chart - school_count_by_management_type_treemap.html')

# Treemap of all schools by constituency and management type
fig = px.treemap(management_type_constituency_count, 
                 path=['constituency', 'management type'], 
                 values='count',
                 title='Number of Schools by Constituency and Management Type')
# Saves this output as a HTML file
fig.write_html('Outputs/Chart - school_count_by_constituency_management_type_treemap.html')

# Treemap of total enrolment in SISS by management type and constituency
fig = px.treemap(strategically_important_small_schools, 
                 path=['constituency', 'management type'], 
                 values='total enrolment',
                 title='Number of Pupils enrolled in Strategically Important Small Schools by Constituency and Management Type')
# Saves this output as a HTML file
fig.write_html('Outputs/Chart - SSIS_by_constituency_management_type_treemap.html')

# Treemap of count of SISS by constituency and management type
SISS_count_by_group = strategically_important_small_schools.groupby(['constituency', 'management type']).size().reset_index(name='count')
fig = px.treemap(SISS_count_by_group, 
                 path=['constituency', 'management type'], 
                 values='count',
                 title='Number of Strategically Important Small Schools by Constituency and Management Type')
# Saves this output as a HTML file
fig.write_html('Outputs/Chart - SISS_count_by_constituency_management_type_treemap.html')

################################################################################
# Maps

# Define colors for each management type - this will be used in all maps
colors = {
    'Controlled': 'blue',
    'Catholic Maintained': 'green',
    'Other Maintained': 'red',
    'Controlled Integrated': 'yellow',
    'GMI': 'orange',
    'Voluntary': 'purple',}

## Map 1: All Primary Schools by Management Type
merged_data['geom'] = merged_data.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
m = folium.Map(location=[merged_data['Latitude'].mean(), merged_data['Longitude'].mean()], zoom_start=8)
title_html = '<h3 align="center" style="font-size:20px"><b>All Primary Schools by Management Type</b></h3>'
m.get_root().html.add_child(folium.Element(title_html))
for idx, row in merged_data.iterrows():
    color = colors.get(row['management type'], 'black')
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['school name'], icon=folium.Icon(color=color)).add_to(m)
# Saves this output as a HTML file
m.save("Outputs/Map - All Primary Schools by Management Type.html")

## Map 2: Strategically Important Small Schools
# The merged_data df is filtered to retain only the rows which are in the 
# strategically_important_small_schools df
strategically_important_schools = merged_data[merged_data['De ref'].isin(strategically_important_small_schools['De ref'].unique())].copy()

# Create a geometry column by combining Longitude and Latitude
strategically_important_schools['geom'] = strategically_important_schools.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)

# Create a map centered at the mean Latitude and Longitude
m = folium.Map(location=[strategically_important_schools['Latitude'].mean(), strategically_important_schools['Longitude'].mean()], zoom_start=8)
title_html = '<h3 align="center" style="font-size:20px"><b>Strategically Important Small Schools by Management Type</b></h3>'
m.get_root().html.add_child(folium.Element(title_html))
for idx, row in strategically_important_schools.iterrows():
    color = colors.get(row['management type'], 'black')
    popup_content = f"<b>School Name:</b> {row['school name']}<br>"
    popup_content += f"<b>Management Type:</b> {row['management type']}<br>"
    popup_content += f"<b>Enrolment:</b> {row['total enrolment']}<br>"
    folium.Marker([row['Latitude'], row['Longitude']], popup=popup_content, icon=folium.Icon(color=color)).add_to(m)
# Saves this output as a HTML file
m.save("Outputs/Map - Strategically Important Small Schools.html")

###
## Map 3: Strategically Important Small Schools with boundaries

# The merged_data df is filtered to retain only the rows which are in the 
# strategically_important_small_schools df
strategically_important_schools = merged_data[merged_data['De ref'].isin(strategically_important_small_schools['De ref'].unique())].copy()
strategically_important_schools['geom'] = strategically_important_schools.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
m = folium.Map(location=[strategically_important_schools['Latitude'].mean(), strategically_important_schools['Longitude'].mean()], zoom_start=8)
title_html = '<h3 align="center" style="font-size:20px"><b>Strategically Important Small Schools by Management Type with boundaries</b></h3>'
m.get_root().html.add_child(folium.Element(title_html))
for idx, row in strategically_important_schools.iterrows():
    color = colors.get(row['management type'], 'black')
    popup_content = f"<b>School Name:</b> {row['school name']}<br>"
    popup_content += f"<b>Management Type:</b> {row['management type']}<br>"
    popup_content += f"<b>Enrolment:</b> {row['total enrolment']}<br>"
    folium.Marker([row['Latitude'], row['Longitude']], popup=popup_content, icon=folium.Icon(color=color)).add_to(m)
folium.GeoJson(
    constituency_boundaries,
    name='constituency boundaries',
).add_to(m)
# Saves this output as a HTML file
m.save("Outputs/Map - Strategically Important Small Schools with boundaries.html")

# A map shaded to show the number of pupils in each constituency/ number unstustinable schools?
