# The department of Education dataset is poorly formatted and lots of columns
# have leading and trailing whitespace. This fuction address this issue.
def remove_whitespace(merged_data):
    merged_data.columns = merged_data.columns.str.strip()
    return merged_data

#Function for converting kilometers to miles
def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
      
# Function to convert distance to area
def convert_distance_to_area(distance):
    global merged_data
    return merged_data[distance] ** 2 * math.pi
