"""
The following functions have been created in order to automate the boring stuff 
and ensure that repetivie actions are minimised. Each function will be commented
to provide detail of what it is doing.
"""

# Function for converting kilometers to miles
"""
This fucntion is created to convert km to miles. All anaslys in this project is
carried out in km. However, the analysis carried out by Roulston and Cook is 
measures distance in miles, so in order to allow for direct comparion in the 
roulston_cook dataframe distances are converted to miles.
"""

def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
      
# Function to convert distance to area
"""
It is useful to look at the distance between schools but it is also useful to
look at in terms of area. So going back to GCSE maths, this function has been 
created to convert the distance between two schools (the radius) into area by 
using the caluclation:
  area = pi x radius squared
"""

def convert_distance_to_area(row, distance_column):
    return row[distance_column] ** 2 * 3.141592653589793

# Function to apply the conditional sustainability logic
"""
One of the key determinents of sustainability for the Department is the enrolment
of a school. A school is defined as sustainable if it is classified as being Urban
and having an enrolment of over 140 and if it is Rural if the enrolment is over 
105. In order to automate this calculation the sustainable_schools function has 
been created. Any school which meets this criteria is defined as being 'Sustainable'
and any which do not are classified as being 'Unsustianble'.
"""

def sustainable_schools(row):
    if (row['Urban/ Rural     '] == "RURAL" and row['total enrolment'] < 105) or (row['Urban/ Rural     '] == "URBAN" and row['total enrolment'] < 140):
        return 'Not Sustainable'
    else:
        return 'Sustainable'
