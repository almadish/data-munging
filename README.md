# Raw Data Munging

## Overview
I will try to make usable a real data source: **NASA's historic measurements of the Earth's surface temperatures**.  In order to do analysis of this data I will:
1. Download raw data.
1. Write a Python program to clean up (i.e. munge) the data and save it into a standard Comma-Separated Values (CSV) format text file.
1. Write a second Python program to do some simple analysis of the data in the CSV file.

## Step-by-step method

### Part 1: Download the data
NASA's [GISS Surface Temperature Analysis web site](https://data.giss.nasa.gov/gistemp/) gives an overview of the data set - they publish recordings in the change of the Earth's surface temperature going back to the year 1880.  
- The numbers do not represent actual temperature readings, but rather represent temperature *anomalies*.
- Their [FAQ page](https://data.giss.nasa.gov/gistemp/faq/#q101) includes some additional explanations that might be helpful.

Download [the raw data in fixed-width column format](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt).
- save the raw data file into the directory named `data` in this repository.

Take a look at the data in the file... 
- Try to understand what is represented by each row and column.  
- Look for explanations in the site's FAQ as necessary.
- Try to spot issues that will make the data difficult to analyze with a program.

### Part 2: Munge it
The raw data has some some features that make it difficult to analyze with a program. 

I wrote a Python program in the file named `munge.py` to clean up the raw data and saved it into a CSV-formatted file named `clean_data.csv` within the `data` directory of this repository.
- I used plain Python in this project withouth using analysis modules such as 'pandas' or 'csv' for munging (I will use pandas and csv modules in the next projects and later in Part 3 of this project, this is just to understand how plain Python works)

    Issues my program must address:
    - there are many lines at the top and bottom of the file that contain notes and not the raw data - **all lines with notes must be removed**.
- the column headings are repeated on multiple lines throughout the file - **remove all but the first line of column headings**.
- there are some blank lines in the middle of the data - **remove all blank lines**.
- there is missing data indicated with `***` - figure out how to **handle missing data so that your analyses are correct**.
- the temperature anomalies in this data are given in 0.01 degrees Celsius.  **Convert temperature anomalies to Farenheit**, the US standard unit of temperature:
    - the formula to do this can be found within the data set
    - format the results so that there's one decimal place (use [format](https://docs.python.org/3/library/functions.html#format) with `.1f` as the second argument)
- since this data is in *fixed-width column format*, there are inconsistent numbers of spaces separating the numeric values... **you optionally may want to standardize how many spaces are used as separators**.
- you are welcome to do **any additional cleanup that helps** you analyze the data in the next step.

Your program must do this cleanup and transformation in a way that is repeatable.  If we were to take the original data file from NASA and run your `munge.py` program on it, these issues would all be resolved in a new file, `clean_data.csv`.

### Part 3: Analyze data set
Now that I have the data in easy to parse CSV format, I am going to perform some aggregate statistics on the data.

I wrote a Python program in the file named `analyze.py` that does the following:
- opens up your cleaned up data file, `clean_data.csv` and imports it using Python's `csv` module.
- outputs the average temperature anomaly in degrees Farenheit for each decade since 1880.  For example, output the average temperature anomaly for the decades:
    - 1880 to 1889
    - 1890 to 1899
    - 1900 to 1909
    - ...and so on.
- Here I used the `csv` module to help parse my CSV data file in the analysis
