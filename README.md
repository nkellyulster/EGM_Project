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
* [Outputs](https://github.com/nkellyulster/Strategically-Important-Small-Schools#-outputs) 
* [Troubleshooting](https://github.com/nkellyulster/Strategically-Important-Small-Schools#%EF%B8%8F-troubleshooting)

# 🎯 Aim
This study uses the Python programming language to apply Geographic Information Systems (GIS) analysis to Northern Ireland (NI) primary school level enrolment data. The primary aim of the analysis is to produce evidence-based analysis of the distance between each of the 787 primary schools in NI and their closest school, based on differing management types. This study examines the sustainability of all primary schools, investigating the potential for designating a number of small schools as being Strategically Important Small Schools (SISS).

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

In December 2023, the long-awaited *Independent Review of Education* was [published](https://www.independentreviewofeducation.org.uk/). The Review is an outworking of the New Decade, New Approach deal, which stated “the education system has a diversity of school types, each with its own distinctive ethos and values. However, it is not sustainable. The parties acknowledge the progress made in developing new models of sharing, cooperation and integration. There is a desire to build on this as a basis for delivering long-term improvements in the quality, equity and sustainability of the system. The parties agree that the Executive will commission and oversee an independent fundamental review with a focus on quality and sustainability.”

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

## Setting up R Studio
> [!IMPORTANT]  
> All of the Python script and data required to create the outputs of this project are provided directly in GitHub.

You will need to ensure that you have the [latest version of Python installed](https://www.python.org/downloads/). You will also require an IDE such as [R Studio](https://posit.co/download/rstudio-desktop/), [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows), [Spyder](https://www.spyder-ide.org/#section-download) or [Anaconda](https://www.anaconda.com/download).

Once you have both Python and your IDE installed the easiest way to access the code and files is to link your IDE to the GitHub repository. To do this you will need to have a [GitHub account](https://github.com/) and then [install Git For Windows](https://git-scm.com/download/win).

To access this code you will need to clone this repository to your machine. This code was written in `Python Version 3.13` in R Studio. To connect this repository to R Studio you will need Git For Windows and the latest version of R Studio installed. Once they are installed complete the following steps to access the repository.
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

Should you wish to manually load the data from the original sources you can do this.

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
To load the 2023/24 dataset and read in the reference data sheet run the following Python script:
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

The code can be run in small chunks to produce some of the outputs or can be run in its entirety to produce all outputs.

# 🐍 Outputs
In terms of outputs, the code produces a number of dataframes, csv outputs, html interactive maps and charts.

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

The purpose of this research is to identify the methodology behind identifying Strategically Important Small Schools and use evidence-based, GIS approaches to identify these schools.

# 🎛️ Troubleshooting
There are limited things that can go wrong with this code, which means there are probably more things that can go wrong with the code than I am willing to admit.

All of the input files are read directly from the GitHub repository and guidance is provided above on how to manually read in data.

This means the only other problem that could realistically exist is that your version of Python is too old or you have not read in the required Python libraries.

If your version of Python is too old, you should get the most recent version of Python that is available. This code was written using `version 3.12` so I would suggest using `version 3.12.`

If you have not installed the required libraries I would recommend installing the required libraries. A list of all the required external modules is provided at the very top of the [Strategically Important Small Schools.py script](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Strategically_Important_Small_Schools.py) and in the [environment file](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/environment.yml).

Functionality has been provided which allows for historic data to be read in from the [Department of Education's School enrolments - school level data website](https://www.education-ni.gov.uk/articles/school-enrolments-school-level-data). This website contains primary school enrolment data as far back as 2009/10. This allows users to compare the various outputs from the current year against data at any point from 2009/2010. There is a comment in the script to explain how to do this as well as as advisory note to say that the data structure differs from year to year so care should be taken to ensure that the `all_schools` dataframe generates correctly. Should the `all_schools` dataframe not generate as a result of missing columns or column with different names you should consult the console to determine what the error is.

For example, the error `KeyError: "['DE ref'] not found in axis"` indicates that the column `DE ref` is not found and when you look closer at the input file you can see that in this file the relevant column is called `De ref` so the code will need to be amended to read the data in correctly.
