# Strategically Important Small Schools v1.0

## 📰 Aim
The aim of the Strategically Important Small Schools (SISS) project is to look at the number of primary schools in Northern Ireland and identify which small schools are strategically important, based on their location, enrolment, and management type.

## 🙋 Audience
Anyone with an interest in primary school education in Northern Ireland or anyone with a general interest in the role small schools play across the education system. This project should be of interest to decision-makers within the Department of Education as well as management authorities who are involved in making strategic decisions about the future of primary education in Northern Ireland.

## 📥 Installation Instructions
All of the Python script and data required to create the outputs of this project are provided directly in GitHub.

To access this code you will need to clone this repository to your own machine. This code was written in Python V3.13 in R Studio. To connect this repository to R Studio you will need Git For Windows and the latest version of R Studio installed. Once they are installed complete the following steps to access the repository.
1.  In R Studio click on File > New Project
2.  Select Version Control
3.  Select Git
4.  Paste `https://github.com/nkellyulster/Strategically-Important-Small-Schools` as the Repository URL
5.  The Project directory name should auto populate as` Strategically-Important-Small-Schools`
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

The locational data comes from the Doogal website and is already saved in GitHub as the BT_postcodes.csv file. Should you wish to manually read the spreadsheet you first need to download the file from the [BT postcodes Northern Ireland page](https://www.doogal.co.uk/UKPostcodes?Search=BT). Click on the Download button and select "Data for this area as CSV (for Excel etc)". This will download the CSV file to your machine. Simply insert the file path in the code chuck below to read it into Pyth:
```ruby
bt_postcodes = pd.read_csv(<you_file_path.csv>)
```

## 📖 Background
According to NI school enrolment data there are XXX primary schools in Northern Ireland. The Department of Education’s policy document ‘Schools for the Future: A Policy for Sustainable Schools’, outlines six criteria which provide a framework for considering issues of school sustainability. In reality, the key determinant of a school's sustainability is it’s enrolment. In an urban area the enrolment threshold for a sustainable school is 140 pupils, and in a rural area it is 105 pupils. According to the Department's own threshold, in 2023/24 there are XXX schools (XX% of the total primary schools) which are ‘not sustainable’ based on enrolment.
