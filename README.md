![Strategically Important Small Schools logo](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/SISS%20logo.png)

# 🧮 Contents
* [Aim](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-aim)
* [Background](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-background)
* [Strategically Important Small Schools](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-strategically-important-small-schools)
* [Audience](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-audience)
* [Roadmap](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-roadmap)
* [Installation Instructions](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-installation-instructions)
* [Manual Instructions](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-manual-installation)
* [Running the code](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-running-the-code)
* [What the script does!](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-what-the-script-does)
* [Outputs](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-outputs) 
* [Troubleshooting](https://github.com/nkellyulster/Strategically-Important-Small-Schools#%EF%B8%8F-troubleshooting)

# 🎯 Aim
This study uses the Python programming language to apply Geographic Information Systems (GIS) analysis to Northern Ireland (NI) primary school level enrolment data. The primary aim of the analysis is to produce evidence-based analysis of the distance between each of the 787 primary schools in NI and their closest school, based on differing management types. This study examines the sustainability of all primary schools, investigating the potential for designating a number of small schools as being Strategically Important Small Schools (SISS).

> [!IMPORTANT]  
> All of the Python script and data required to create the outputs of this project are provided directly in GitHub.

# 📖 Background
According to [NI school enrolment data published by the NI Department of Education](https://www.education-ni.gov.uk/publications/school-enrolment-school-level-data-202223) there are 787 primary schools in Northern Ireland for the academic year 2023/24. 

The Department is responsible for managing the school estate and planning, on an area basis, for the future provision of schools. This entire process is part of their objective to "ensure that all children get a first class education in fit for purpose facilities, regardless of background or where they live." The Department of Education’s policy document [‘Schools for the Future: A Policy for Sustainable Schools’](https://www.education-ni.gov.uk/publications/schools-future-policy-sustainable-schools), outlines six criteria that provide a framework for considering issues of school sustainability. This document stems from the [2006 Independent Strategic Review of Education](https://dera.ioe.ac.uk/id/eprint/9777/1/review_of_education.pdf), more commonly known as the Bain Report.

The policy sets out six criteria to be considered in assessing a school's educational viability, as follows:-

* quality educational experience
* stable enrolment trends
* sound financial position
* strong leadership and management
* accessibility
* strong links with the community

In reality, the key determinant of a school's sustainability is its enrolment. In an urban area the enrolment threshold for a sustainable school is 140 pupils, and in a rural area it is 105 pupils. According to the Department's own criteria, in 2023/24 there are 210 schools (27% of the total primary schools) which are ‘not sustainable’ based on enrolment.

Every year the management authority of schools work together with the Education Authority and Department of Education to determine which primary schools which are deemed as unsustainable should be considered for closure. The process that feeds into this involves the publication of a Case for Change from the management authority and this can lead to the creation of a Development Proposal which can ultimately lead to the Minister of Education making a decision on whether or not a school should close. Since 2009/10 over 60 small, mostly rural primary schools have been closed, having been deemed unsustainable.

For a number of years, there has been a growing sense that the Sustainable Schools Policy has been a blunt instrument used as the justification for the closing of small, rural schools, and that criteria should be used to identify small schools which are strategically important. This would not mean that these schools would be exempt from the consideration of the Sustainable Schools Policy but that their relative remoteness would be taken into consideration when schools were being assessed under the policy.

In December 2023, the long-awaited *Independent Review of Education* was [published](https://www.independentreviewofeducation.org.uk/). The Review is an outworking of the [New Decade, New Approach](https://assets.publishing.service.gov.uk/media/5e178b56ed915d3b06f2b795/2020-01-08_a_new_decade__a_new_approach.pdf) deal, which stated “the education system has a diversity of school types, each with its own distinctive ethos and values. However, it is not sustainable. The parties acknowledge the progress made in developing new models of sharing, cooperation and integration. There is a desire to build on this as a basis for delivering long-term improvements in the quality, equity and sustainability of the system. The parties agree that the Executive will commission and oversee an independent fundamental review with a focus on quality and sustainability.”

# 🏫 Strategically Important Small Schools
The idea of designating some schools as being strategically important has been discussed for a number of years but there has been no actual progress on how to determine what constitutes a strategically important small school. And that is the issue which this project aims to address.

![Strategically Important Small Schools Roadmap](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/Tyrone%20Constitution.jpg)
*Caption: Tyrone Constitution - Thursday 25 April 2024 - "Greater recognition needed for strategically important small schools"*

Using GIS analysis of the distance between schools and looking at the distances between different management types a number of schools have been designated as being strategically important small schools as there is a considerable distance between them and the nearest school in the same management type. The outputs of this project can be examined in more detail, but produce very clear recommendations on a small number of schools which, if they were closed on the grounds of 'sustainability' would have a negative impact on their local areas. Due to the nature of this analysis, and the methodology adopted, these schools are typically schools from the minority community in an area that has schools for the other main management type, which is why the designation of these schools as being important takes on a more strategic approach.

# 🙋 Audience
Anyone with an interest in primary school education in Northern Ireland or anyone with a general interest in the role small schools play across the education system. This project should be of interest to both policy-makers and decision-makers within the Department of Education, the Educathion Authority, as well as management authorities who are involved in making strategic decisions about the future of primary education in Northern Ireland.

#  🚗 Roadmap
![Tyrone Constitution - Thursday 25 April 2024 - "Greater recognition needed for strategically important small schools"](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/Strategically%20Important%20Small%20Schools%20Roadmap.png)

# 📥 Installation Instructions

## Setup
> [!IMPORTANT]  
> To run this code you need to have R Studio (or a different IDE), Python and Git installed.
> 1.	R Studio Integrated Development Environment (IDE) from the [Posit website](https://posit.co/download/rstudio-desktop/).
> 2.	Python which can be directly downloaded from the [Python website](https://www.python.org/downloads/). This code was written in `Python Version 3.13` in R Studio.
> 3.	[Git For Windows](https://git-scm.com/downloads), this will ensure that you can connect your IDE to the[ Strategically Important Small Schools GitHub repository](https://github.com/nkellyulster/Strategically-Important-Small-Schools).
>
> You will also need a [GitHub account which you can sign up for free](https://github.com/join).

## Other IDEs
This project was written in R Studio but other IDEs are available, such as [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows), [Spyder](https://www.spyder-ide.org/#section-download) or [Anaconda](https://www.anaconda.com/download).

## Setting up R Studio
To run this code you will need to clone this repository to your machine. Once you have all the software installed and have a GitHub account, complete the following steps to access the repository.
1.  In R Studio click on File > New Project

![Step 1](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/Step1.png)

2.  Select Version Control

![Step 2](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/Step2.png)

3.  Select Git

![Step 3](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/Step3.png)

4.	In the Clone Git Repository window, in the “Repository URL” box, add the url: “https://github.com/nkellyulster/Strategically-Important-Small-Schools”
This automatically populates the “Project directory name” box but if it does not you should key “Strategically-Important-Small-Schools”.
In “Create project as a subdirectory of:” you should select a folder on your machine to create a project folder.
Finally, click the Create Project button.

![Step 4](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/Step4.png)

5.	This will clone the GitHub repository to your machine.
   
![Step 5](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/Step5.png)

6.	Your project is now created and you are connected to the SISS GitHub repository.

![Step 6](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/Step6.png)

Should you wish to manually load the data from the original sources you can do this. A step by step guide on how to do this is provided in the [Manual Installation](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-manual-installation) section of this Readme.

NI primary school enrolment data is updated on an annual basis by the NI Department of Education. The [school enrolments page](https://www.education-ni.gov.uk/topics/statistics-and-research/school-enrolments) contains a plethora of information and datasets. School level enrolment data from 2009/10 - 2023/24 is available on the [School enrolments - school level data page](https://www.education-ni.gov.uk/articles/school-enrolments-school-level-data). The most recent dataset, for 2023/24 was published on 19 March 2024 and the [datatset used in this project is available as an XLSX file](https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20pre-school%20data%20-%20202324.XLSX).

Links are provided in the code so that enrolment data from every year since 2009/10 can be analsysed.

## Packages
The following packages are used to run this Python script.
*  [csv](https://docs.python.org/3/library/csv.html)
*  [math](https://docs.python.org/3/library/math.html)
*  [collections](https://docs.python.org/3/library/collections.html)
*  [folium](https://pypi.org/project/folium/)
*  [geopandas](https://geopandas.org/)
*  [numpy](https://numpy.org/)
*  [pandas](https://pandas.pydata.org/)
*  [plotly.express](https://plotly.com/python/plotly-express/)
*  [folium.plugins](https://python-visualization.github.io/folium/latest/user_guide/plugins.html)
*  [haversine](https://pypi.org/project/haversine/)
*  [shapely](https://pypi.org/project/shapely/)

# 📤 Manual Installation
To manually load the 2023/24 dataset and read in the reference data sheet run the following Python script:
```ruby
schools = pd.read_excel("https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20pre-school%20data%20-%20202324.XLSX",
sheet_name = "reference data",
skiprows = 3)
```

Equally, to load the 2023/24 dataset and read in the enrolment data sheet run the following Python script:
```ruby
enrolment = pd.read_excel("https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20pre-school%20data%20-%20202324.XLSX",
sheet_name = "total enrolment",
skiprows = 3)
```

The locational data comes from the Doogal website and is already saved in GitHub as the `BT_postcodes.csv` file. Should you wish to manually read the spreadsheet you first need to download the file from the [BT postcodes Northern Ireland page](https://www.doogal.co.uk/UKPostcodes?Search=BT). Click on the Download button and select "Data for this area as CSV (for Excel etc)". This will download the CSV file to your machine. Simply insert the file path in the code chuck below to read it into Pyth:
```ruby
bt_postcodes = pd.read_csv(<you_file_path.csv>)
```

# 🏃 Running the code
Running the code is a fairly straightforward process.

> [!TIP]  
> The code can be run in small chunks to produce some of the outputs or can be run in its entirety to produce all outputs.

To run all the code, from start to finish, to produce all of the outputs, simply click in the main script window, press `Control + A` to highlight all the text and press `Control + Enter` to run the script. Alternatively, when all of the text is highlighted you can click the `Run` button at the top of main script window. **Please be aware it take a few minutes to run the code from start to finish and produce all of the outputs.**

![Running the code](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/Running-Code.png)

If you want to run through the code chunk by chunk, to see what the output of each process is, simply higlight the rows you wish to run, then run the code, as outlined above.

# 🐍 What the script does!
The scripts are hopefully written in a way that are hopefully logical and clear to understand. This section will look at the scripts at a very high level, giving an overview, rather than a line-by-line blow of what they do.
There are 2 main scripts used for this project.

## Functions
This is a short script file and is only 49 lines long. In it are 3 custom functions which:
*   Convert kilometers to miles
*   Convert distance to area
*   Classify a school as being Sustainable or Not Sustainable based on Department of Education guidelines.

All funtions use `docstrings` to explain in more detail what the functions do, what the inputs are and what the outputs are.
All functions are read in to the Strategically Important Small Schools script.

## Strategically Important Small Schools
This is the main script file for the project and is almost 600 lines long.

This script is broken down into several different sections to make it easier to understand and navigate.
### 1. Setup
#### 1.1 External Modules
External modules, which are outlined in the [Packages section of this document](https://github.com/nkellyulster/Strategically-Important-Small-Schools#packages) are laoded here.
#### 1.2 Import my functions
The 3 custom functions from [functions.py](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/functions.py) are loaded here.

### 2. Context
This brief section gives some background to the type of data that is read in to the analysis and provides a link to the Department of Education website where the raw data can be accessed.

### 3. Import data files
This section is where the inputs are read in from. Basic data manipulation is used to indicate which tabs from which spreadsheets are used.

### 4. Previous years data
Links to 14 years worth of data are provided. This covers the period from 2009/10 to 2022/23. By uncommenting these links the user can read in enrolment and school data for the academic year they want. This allows the users to compare the changing nature of the primary school estate over the past number of years.
As the links point to the datasets held on the Department of Education website there is assurance that the data contained is the original and has not been amended or altered in any way.

### 5. Data cleaning
This section of code combines the `enrolment`, `school` and `postcodes` data into one master dataframe.
A manual workaround is included to manually add co-ordinates for school postcode data which is missing from the `postcodes` dataframe. A check is built into this to ensure that the number of schools remains unchanged from the start of this process to the end. This section will need to be revised to look at school data from a different year.
Dataframes are cleaned and unnecessary columns are removed in advances of the analysis stages.

### 6. Spatial analysis
Spatial analysis is carried out to calculate:
* the distance from each school to the nearest school
* the distance from each school to the nearest school in the same management type
* the distance from each school to the nearest school NOT in the same management type
This is the main section for spatial analysis and the outputs from this stage feed directly into the main conclusions of this project. The master dataframe that is produced at this stage will be filtered into more usable outputs at later stages.

### 7. Create dataframe and value outputs
This section is where the majority of analysis is carried out.
Datasets are filtered to produce the main outputs and dataframes are counted and summed to produce a wide range of useful analysis and outputs.
A number of csv outputs are produced from this stage.

### 8. Strategically Important Small Schools Analysis
The purpose of this project is to carry out analysis on Strategically Important Small Schools and this section is where this analysis is carried out.

Distances between schools are binned into the following categories for ease of analysis.

| Title | Bin Range |
| --- | --- |
|Less than 1km | <1 |
|Between 1km and 2.9km | 1-2.9 |
|Between 3km and 4.9km | 3 - 4.9 |
|Between 5km and 7.4km | 5 - 7.4 |
|Between 7.5km and 9.9km | 7.5 - 9.9 |
|Greater than 10km | >=10 |

### 9. Create charts outputs
3 interactive charts are created to highlight some of the key findings of this study.

### 10. Create maps outputs
3 interactive map are created to highlight some of the key findings of this study.

# 📤 Outputs
In terms of outputs, the code produces over 30 outputs, including values, dataframes, csv outputs, html interactive maps and charts.

This code produces the following outputs: 
*  `rows_not_in_bt_postcodes` a dataframe with all the school postcodes which do not appear in the `bt_postcodes` dataframe
*  `merged_data` dataframe with all variables. This output is also saved as a `CSV` file in the `Outputs` folder
*  `school_count` a simple count of the number of primary schools in Northern Ireland 
*  `management_type_count` a count of all primary schools in Northern Ireland broken down by management type
*  `constituency_count` a count of all primary schools in Northern Ireland broken down by constituency
*  `management_type_constituency_count` a count of all primary schools in Northern Ireland broken down by management type **and** constituency. This output is also saved as a `CSV` file in the `Outputs` folder
*  `total_enrolment_sum` the sum of all pupils in all primary schools in Northern Ireland
*  `total_enrolment_by_management_type` the total number of pupils educated in each management type in Northern Ireland. This output is also saved as a `CSV` file in the `Outputs` folder
*  `total_enrolment_constituency` the total number of pupils educated in each constituency in Northern Ireland. This output is also saved as a `CSV` file in the `Outputs` folder
*  `sustainable_count` the number of sustainable and unsustainable primary schools in Northern Ireland (based on the criteria laid out in the `sustainable_schools` function)
*  `sustainable_pupils` is the sum of pupils being educated in sustainable and unsustainable schools
*  `count_catholic_maintained_controlled` is a count of the number of Catholic Maintained and Controlled schools
*  `percentage_schools_catholic_maintained_controlled` is the percentage of Catholic Maintained and Controlled schools relative to the total number of primary schools in Northern Ireland
*  `sum_catholic_maintained_controlled` is a sum of the number of pupils being educated in Catholic Maintained and Controlled schools
*  `percentage_enroled_catholic_maintained_controlled` is the number of pupils educated in Catholic Maintained and Controlled schools relative to the total number of primary school pupils in Northern Ireland
*  `nearest_school` this provides the nearest primary school to each primary school, **irrespective of the management type**. This output is also saved as a `CSV` file in the `Outputs` folder
*  `nearest_school_same_management` this provides the nearest primary school to each primary school in the **same management type**. This output is also saved as a `CSV` file in the `Outputs` folder
*  `nearest_school_not_same_management` this provides the nearest primary school to each primary school that is **not in the same management type**. This output is also saved as a `CSV` file in the `Outputs` folder
*  `Roulston_Cook` this replicate the research carried out by [Roulston & Cook](https://pure.ulster.ac.uk/en/publications/isolated-together-pairs-of-primary-schools-duplicating-provision) in their 2020 Research `Isolated Together: Pairs of Primary Schools Duplicating Provision`
*  `strategically_important_small_schools` this produces the primary schools which meet the criteria of being *Strategically Important Small Schools*.  To produce this output the `nearest_school_same_management` dataframe is filtered to show only the schools which are deemed as *Unsustainable*. The distance to the nearest school in the same management time is sorted in descending order and only those schools which are at least 7.5km away from another school in the same management type are retained. This output is also saved as a `CSV` file in the `Outputs` folder 
*  `count_strategically_important_small_schools_constituency` this is a simple count of the number of schools in the `strategically_important_small_schools` by constituency. This output is also saved as a `CSV` file in the `Outputs` folder
*  `count_strategically_important_small_schools_management_type` this is a count of the number of `strategically_important_small_schools` by management type. This output is also saved as a `CSV` file in the `Outputs` folder
*  `Map: All Primary Schools by Management Type` this map shows all primary schools in Northern Ireland, with the marker for each management type coloured differently. This output is also saved as a `HTML` file in the `Outputs` folder
*  `Map: Strategically Important Small Schools` this map shows all of the Strategically Important Small Schools in Northern Ireland, with the marker for each management type coloured differently. This output is also saved as a `HTML` file in the `Outputs` folder
*  `Map: Strategically Important Small Schools with boundaries` this is the same as `Map: Strategically Important Small Schools` only this has the parliamentary boundaries layer added. This output is also saved as a `HTML` file in the `Outputs` folder
*  `Chart: bar chart of all schools by management type` this interactive bar chart provides a breakdown of all schools by management type. This output is also saved as a `HTML` file in the `Outputs` folder
*  `Chart: bar chart of all pupils by management type` this interactive bar chart provides a breakdown of all pupils by management type. This output is also saved as a `HTML` file in the `Outputs` folder
*  `Chart: treemap of all schools by management type` this interactive treemap provides a breakdown of all schools by management type. This output is also saved as a `HTML` file in the `Outputs` folder
*  `Chart: treemap of all schools by constituency and management type` this interactive treemap provides a breakdown of all schools by both constituency and management type. This output is also saved as a `HTML` file in the `Outputs` folder
*  `Chart: treemap of total enrolment in SISS by management type and constituency` this interactive treemap provides a breakdown of pupil enrolment in Strategically Important Small Schools by management type and constituency. This output is also saved as a `HTML` file in the `Outputs` folder
*  `Chart: treemap of count of SISS by constituency and management type` this interactive treemap provides a breakdown of all Strategically Important Small Schools by constituency management type. This output is also saved as a `HTML` file in the `Outputs` folder

##
The Maps which are created label each of the schools by their Management Type. The legend for each Management Type is listed below:
| Management Type | Legend |
| --- | --- |
| Controlled | Blue |
| Catholic Maintained | Green | 
| Other Maintained | Red |
| Controlled Integrated | Yellow | 
| GMI | Orange | 
| Voluntary | Purple | 

# 🎛️ Troubleshooting
There are limited things that can go wrong with this code, as all of the input files are read directly from the GitHub repository and guidance is provided above on how to manually read in data.

This means the only other problem that could realistically exist is that your version of Python is too old or you have not read in the required Python libraries.

## Out of date Python version
If your version of Python is too old, you should get the most recent version of Python that is available. This code was written using `version 3.12` so I would suggest using `version 3.12.`

## Package issue
If you have not installed the required libraries I would recommend installing the required libraries. A list of all the required external modules is provided at the very top of the [Strategically Important Small Schools.py script](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Strategically_Important_Small_Schools.py) and in the [environment file](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/environment.yml).

Should any of these packages not install correctly they can be manually installed in the terminal using the following syntax. For example, to manually install pandas simply key the following in the terminal:

`pip install pandas`

![pip install pandas](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Images/terminal.png)

## Changing structure of Department of Education data
Analysis can be carried out on data going back as far as 2009/10, but unfortunately the structure of the data has changed numerous times over the years. This can cause errors when the school level data is being read in. Should there be errors in creating the `schools` or `enrolment` dataframes this is likely the cause of the error. 

By amending the script in the `selected_enrolment` and `all_schools` dataframes this can easily be resolved.

For example, the error `KeyError: "['DE ref'] not found in axis` indicates that the column `DE ref` is not found and when you look closer at the input file you can see that in this file the relevant column is called `De ref` so the code will need to be amended to read the data in correctly.

## Postcode errors
Functionality has been provided which allows for historic data to be read in from the [Department of Education's School enrolments - school level data website](https://www.education-ni.gov.uk/articles/school-enrolments-school-level-data). 

This website contains primary school enrolment data as far back as 2009/10. This allows users to compare the various outputs from the current year against data at any point from 2009/2010. There is a comment in the script to explain how to do this as well as as advisory note to say that the data structure differs from year to year so care should be taken to ensure that the `all_schools` dataframe generates correctly. Should the `all_schools` dataframe not generate as a result of missing columns or column with different names you should consult the console to determine what the error is.

This is the extract of code which is used to identify and resolve this issue:
~~~
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
~~~
