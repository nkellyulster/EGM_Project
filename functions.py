# The department of Education dataset is poorly formatted and lots of columns
# have leading and trailing whitespace. This fuction address this issue.
# def remove_whitespace(merged_data):
#     merged_data.columns = merged_data.columns.str.strip()
#     return merged_data

#Function for converting kilometers to miles
def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
      
# Function to convert distance to area
def convert_distance_to_area(row, distance_column):
    return row[distance_column] ** 2 * math.pi

# Function to apply the conditional sustainability logic
def sustainable_schools(row):
    if (row['Urban/ Rural     '] == "RURAL" and row['total enrolment'] < 105) or (row['Urban/ Rural     '] == "URBAN" and row['total enrolment'] < 140):
        return 'Not Sustainable'
    else:
        return 'Sustainable'
