#Function for converting kilometers to miles
def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
km_to_miles(345)

# Function to apply the conditional logic
def sustainability(row):
    if (row['urban/ rural     '] == "Rural" and row['total enrolment'] < 105) or (row['urban/ rural     '] == "Urban" and row['total enrolment'] < 140):
        return 'Not Sustainable'
    else:
        return 'Sustainable'
