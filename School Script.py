# Import libraries
import pandas as pd
import folium
import shapely
from shapely.geometry import Point
from haversine import haversine, Unit

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
# URL for the 2023/24 primary school level data
primary_school_url = "https://github.com/nkellyulster/EGM_Project/raw/main/School%20level%20-%20primary%20schools%20data%202223.XLSX"

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

# Filter to retain only the DE Reference and the Total Enrolment columns from the enrolment df                        
selected_enrolment = enrolment.loc[:, ['DE ref', 'total enrolment']]

# Retain only the selected columns from the bt_postcodes dataframe
selected_bt_postcodes = bt_postcodes.loc[:, ['Postcode', 'Latitude', 'Longitude']]

# Join the schools dataframe and the enrolment dataframe and drop 'DE ref' column from new df
all_schools = pd.merge(schools, selected_enrolment, how='inner', left_on='De ref', right_on='DE ref')
all_schools = all_schools.drop('DE ref', axis = 1)

# Join the schools and selected_bt_postcodes dataframes using postcode and Postcode variables
merged_data = pd.merge(all_schools, selected_bt_postcodes, how='inner', left_on='postcode', right_on='Postcode')

# Remove unused columns from merged_data df
merged_data = merged_data.drop(['address 1', 'school type', 'district council (2014)', 'ward (2014)', 'DEA (2014)', 'Postcode'], axis=1)

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
