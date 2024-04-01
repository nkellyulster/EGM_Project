import pandas as pd
import folium
import shapely

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

# Read the bt_postcodes CSV file which contains Postcode / co-oridnates data
bt_postcodes = pd.read_csv(bt_postcodes_url)
