import pandas as pd
import folium
import shapely
from shapely.geometry import Point

# The NI Department of Education publish school level enrolment data every year.
# This is based on the school census that takes place every October.
# The Primary School data for the most recent year, 2023/24, was published on
# 19th March 2024 at https://www.education-ni.gov.uk/publications/school-enrolment-school-level-data-202324

# URL for the 2023/24 primary school level data
primary_school_url = "https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20primary%20schools%20data%202223.XLSX"

# URL for BT postcodes CSV saved in GitHub
bt_postcodes_url = "https://raw.githubusercontent.com/nkellyulster/EGM_Project/main/BT%20postcodes.csv"

# The following chunk reads in the url for the Primary School XLSX
# spreadsheet, open the 'reference data' tab and skips the first 3 rows
schools = pd.read_excel(primary_school_url,
sheet_name = "reference data",
skiprows = 3)

# Read in the enrolment tab and skip the first 3 rows                        
enrolment = pd.read_excel(primary_school_url,
sheet_name = "Enrolments",
skiprows = 3)

# Filter to retain only the DE Referene and the Total Enrolment columns                        
selected_enrolment = enrolment.loc[:, ['DE ref', 'total enrolment']]

# Join the schools dataframe and the enrolment dataframe
all_schools = pd.merge(schools, selected_enrolment, how='inner', left_on='De ref', right_on='DE ref')

# Read the bt_postcodes CSV file which contains Postcode / co-oridnates data
bt_postcodes = pd.read_csv(bt_postcodes_url)

# Retain only the selected columns from the bt_postcodes dataframe
selected_bt_postcodes = bt_postcodes.loc[:, ['Postcode', 'Latitude', 'Longitude']]

# Join the schools and selected_bt_postcodes dataframes using potcode and Postcode variables
merged_data = pd.merge(all_schools, selected_bt_postcodes, how='inner', left_on='postcode', right_on='Postcode')

# Count the number of pupils in each constituency and sort descending
constituency_count = merged_data.groupby(['constituency']).agg({'total enrolment': 'sum'})
constituency_count = constituency_count.sort_values(by='total enrolment', ascending=False)

# Count the number of pupils in each constituency and by management type and sort descending
constituency_management_type_count = merged_data.groupby(['constituency', 'management type']).agg({'total enrolment': 'sum'}).reset_index()
constituency_management_type_count = constituency_management_type_count.sort_values(by=['constituency', 'total enrolment'], ascending=[True, False])

# Count the number of pupils educated in Urban and Rural schools and sort descending
urban_rural_count = merged_data.groupby(['urban/ rural     ']).agg({'total enrolment': 'sum'})
urban_rural_count = urban_rural_count.sort_values(by='total enrolment', ascending=False)

# Calculate the total sum of pupils and then calculate the urban/ rural percentage split
total_sum = urban_rural_count['total enrolment'].sum()
urban_rural_count['Percentage'] = (urban_rural_count['total enrolment'] / total_sum) * 100

# Create a geometry column by combining Longitude and Latitude
merged_data['geom'] = merged_data.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)

# Create a map centered at the mean Latitude and Longitude
m = folium.Map(location=[merged_data['Latitude'].mean(), merged_data['Longitude'].mean()], zoom_start=8)

# Add markers for each school
for idx, row in merged_data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['school name']).add_to(m)

# Save the map to an HTML file
m.save('map.html')
