# Strategically Important Small Schools v1.0

## 📰 Aim
The aim of the Strategically Important Small Schools (SISS) project is to look at the number of primary schools in Northern Ireland and identify which small schools are strategically important, based on their location, enrolment, and management type.

## 🙋 Audience
Anyone with an interest in primary school education in Northern Ireland or anyone with a general interest in the role small schools play across the education system. This project should be of interest to decision-makers within the Department of Education as well as management authorities who are involved in making strategic decisions about the future of primary education in Northern Ireland.

##  🚗 Roadmap
![alt text](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/Strategically%20Important%20Small%20Schools%20Roadmap.png?raw=true)


## 📥 Installation Instructions
All of the Python script and data required to create the outputs of this project are provided directly in GitHub.

You will need to ensure that you have the [latest version of Python installed](https://www.python.org/downloads/). You will also require an IDE such as [R Studio](https://posit.co/download/rstudio-desktop/), [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows), [Spyder](https://www.spyder-ide.org/#section-download) or [Anaconda](https://www.anaconda.com/download).

Once you have both Python and your IDE installed the easiest way to access the code and files is to link your IDE to the GitHub repository. To do this you will need to have a [GitHub account](https://github.com/) and then [install Git For Windows](https://git-scm.com/download/win).

To access this code you will need to clone this repository to your machine. This code was written in `Python Version 3.13` in R Studio. To connect this repository to R Studio you will need Git For Windows and the latest version of R Studio installed. Once they are installed complete the following steps to access the repository.
1.  In R Studio click on File > New Project
2.  Select Version Control
3.  Select Git
4.  Paste `https://github.com/nkellyulster/Strategically-Important-Small-Schools` as the Repository URL
5.  The Project directory name should auto-populate as` Strategically-Important-Small-Schools`
6.  Select a location on your machine as the `subdirectory` location
7.  Click Create Project
8.  This should clone the Repo and allow you to run the `SISS.py` file.

Should you wish to manually load the data from the original sources you can do this.

NI primary school enrolment data is updated on an annual basis by the NI Department of Education. The [school enrolments page](https://www.education-ni.gov.uk/topics/statistics-and-research/school-enrolments) contains a plethora of information and datasets. School level enrolment data from 2009/10 - 2023/24 is available on the [School enrolments - school level data page](https://www.education-ni.gov.uk/articles/school-enrolments-school-level-data). The most recent dataset, for 2023/24 was published on 19 March 2024 and the [datatset used in this project is available as an XLSX file](https://www.education-ni.gov.uk/sites/default/files/publications/education/School%20level%20-%20pre-school%20data%20-%20202324.XLSX).

### 📤 Manual Installation
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

## 🏃 Running the code
Running the code is a fairly straightforward process.

The code can be run in small chunks to produce some of the outputs or can be run in its entirety to produce all outputs.

### 🐍 Outputs
In terms of outputs, the code produces a number of dataframes, csv outputs, html interactive maps and charts.

This code produces the following outputs: 
*  `rows_not_in_bt_postcodes` a dataframe with all the school postcodes which do not appear in the `bt_postcodes` dataframe
*  `school_count` a simple count of the number of primary schools in Northern Ireland 
*  `management_type_count` a count of all primary schools in Northern Ireland broken down by management type
*  `constituency_count` a count of all primary schools in Northern Ireland broken down by constituency
*  `management_type_constituency_count` a count of all primary schools in Northern Ireland broken down by management type **and** constituency 
*  `total_enrolment_sum` the sum of all pupils in all primary schools in Northern Ireland
*  `total_enrolment_by_management_type` the total number of pupils educated in each management type in Northern Ireland
*  `total_enrolment_constituency` the total number of pupils educated in each constituency in Northern Ireland
*  `sustainable_count` the number of sustainable and unsustainable primary schools in Northern Ireland (based on the criteria laid out in the `sustainable_schools` function)
*  `sustainable_pupils` is the sum of pupils being educated in sustainable and unsustainable schools
*  `count_catholic_maintained_controlled` is a count of the number of Catholic Maintained and Controlled schools
*  `percentage_schools_catholic_maintained_controlled` is the percentage of Catholic Maintained and Controlled schools relative to the total number of primary schools in Northern Ireland
*  `sum_catholic_maintained_controlled` is a sum of the number of pupils being educated in Catholic Maintained and Controlled schools
*  `percentage_enroled_catholic_maintained_controlled` is the number of pupils educated in Catholic Maintained and Controlled schools relative to the total number of primary school pupils in Northern Ireland
*  `nearest_school` this provides the nearest primary school to each primary school, **irrespective of the management type**
*  `nearest_school_same_management` this provides the nearest primary school to each primary school in the **same management type**
*  nearest_school_not_same_management this provides the nearest primary school to each primary school that is **not in the same management type**
*  `Roulston_Cook` this replicate the research carried out by [Roulston & Cook](https://pure.ulster.ac.uk/en/publications/isolated-together-pairs-of-primary-schools-duplicating-provision) in their 2020 Research `Isolated Together: Pairs of Primary Schools Duplicating Provision`
*  `strategically_important_small_schools` this produces the primary schools which meet the criteria of being *Strategically Important Small Schools*.  To produce this output the `nearest_school_same_management` dataframe is filtered to show only the schools which are deemed as *Unsustainable*. The distance to the nearest school in the same management time is sorted in descending order and only those schools which are at least 7.5km away from another school in the same management type are retained 
*  `count_strategically_important_small_schools_constituency` this is a simple count of the number of schools in the `strategically_important_small_schools` by constituency
*  `count_strategically_important_small_schools_management_type` this is a count of the number of `strategically_important_small_schools` by management type
*  `Map: All Primary Schools by Management Type` this map shows all primary schools in Northern Ireland, with the marker for each management type coloured differently 
*  `Map: Strategically Important Small Schools` this map shows all of the Strategically Important Small Schools in Northern Ireland, with the marker for each management type coloured differently
*  `Map: Strategically Important Small Schools with boundaries` this is the same as `Map: Strategically Important Small Schools` only this has the parliamentary boundaries layer added

## 📖 Background
According to NI school enrolment data there are 787 primary schools in Northern Ireland. 

The Department of Education’s policy document [‘Schools for the Future: A Policy for Sustainable Schools’](https://www.education-ni.gov.uk/publications/schools-future-policy-sustainable-schools), outlines six criteria that provide a framework for considering issues of school sustainability. This document stems from the [2006 Independent Strategic Review of Education](https://dera.ioe.ac.uk/id/eprint/9777/1/review_of_education.pdf), more commonly known as the Bain Report.

In reality, the key determinant of a school's sustainability is it’s enrolment. In an urban area the enrolment threshold for a sustainable school is 140 pupils, and in a rural area it is 105 pupils. According to the Department's own criteria, in 2023/24 there are 210 schools (27% of the total primary schools) which are ‘not sustainable’ based on enrolment.

## 🎛️ Troubleshooting
There are limited things that can go wrong with this code, which means there are probably more things that can go wrong with the code than I am willing to admit.

All of the input files are read directly from the GitHub repository and guidance is provided above on how to manually read in data.

This means the only other problem that could realistically exist is that your version of Python is too old or you have not read in the required Python libraries.

If your version of Python is too old, you should get the most recent version of Python that is available. This code was written using version 3.12 so I would suggest using `version 3.12.`

If you have not installed the required libraries I would recommend installing the required libraries. A list of all the required libraries is contained at the very top of the [SISS.py script](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/SISS.py) or in the [environment file](https://github.com/nkellyulster/Strategically-Important-Small-Schools/blob/main/environment.yml).

Functionality has been provided which allows for historic data to be read in from the [Department of Education's School enrolments - school level data website](https://www.education-ni.gov.uk/articles/school-enrolments-school-level-data). This website contains primary school enrolment data as far back as 2009/10. This allows users to compare the various outputs from the current year against data at any point from 2009/2010. There is a comment in the script to explain how to do this as well as as advisory note to say that the data structure differs from year to year so care should be taken to ensure that the `all_schools` dataframe generates correctly. Should the `all_schools` dataframe not generate as a result of missing columns or column with different names you should consuly the console to determine what the error is.

For example, the error `KeyError: "['DE ref'] not found in axis"` indicates that the column `DE ref` is not found and when you look closer at the input file you can see that in this file the releavnt column is called `De ref` so the code will need to be amended to read the data in correctly.
