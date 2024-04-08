#Function for converting kilometers to miles
def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
km_to_miles(345)

# Function to apply the conditional sustainability logic
def sustainability(row):
    if (row['Urban/ Rural     '] == "Rural" and row['total enrolment'] < 105) or (row['Urban/ Rural     '] == "Urban" and row['total enrolment'] < 140):
        return 'Not Sustainable'
    else:
        return 'Sustainable'
      
# Function to convert distance to area
def convert_distance_to_area(distance):
    global merged_data
    return merged_data[distance] ** 2 * math.pi
