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
      
sustainability(45)
