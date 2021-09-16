# Chapter 2, exercise 2

## Loading
In this exercise, data on used cars in Budapest with the model **Volkswagen Passat** was collected. As a source, [joautok.hu ](https://joautok.hu/hasznaltauto/budapest/hasznalt/volkswagen/passat) a website for used cars ads was used. 

For web scraping with Python, [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library was used. The result is stored in Excel file using [pandas](https://pandas.pydata.org/) and [openpyxl](https://openpyxl.readthedocs.io/en/stable/) library. Python code that was used for web scraping can be found in _webScrapingHTML.py_ file. 

The most important characteristics of used cars such as their name, price, and mileage was scraped from the website. Then, this data is stored into *dataset.xlsx* Excel file inside **raw** folder. This file contains the data for 112 cars. 

*dataset.xlsx* Excel file contains the following variables:

- **Names**
- **Mileage**
- **Prices**

## Cleaning
Then, data cleaning process was started. Raw data was in cross-sectional (xsec) data form as observations (cars) come from same time (5 P.M. 24th October, 2020) and each observation referes to different units (cars, *VW Passat 1.4* and *VW Passat 1.6* in this case). 

After carefully reviewing the file, it was ensured that each observation is in one row and each variable is in one column. Variables (*name, price, and mileage*) were ready for the analysis. car_id varible was added as an ID to uniquely identify each car. All the variables were stored in an appropriate format. car_id is stored as a numeric. As the data on web such as name, mileage and price are text, they are stored as a string. It would be more appropriate to transform these three variables from string to text as they represent numeric value. But it was decided to do this step in the further analysis as it is time-consuming process and it is not important at this stage. There were no missing values. All the values were in their admissable range. For instance, there were no negative value for price (e.g. -15000) that would make no sense. Units of measurement for variable values are indicated in VARAIBLES.xlsx file. For example, kilometer for mileage and Hungarian forint for price. Relative variable labels were also provided. 

Then, this tiny data table is stored into a workfile as a *dataset_clean.xlsx* Excel file inside **clean** folder. A , *dataset_clean.xlsx* Excel file contains the following variables:

- **car_id**: unique identifier for each car
- **names**: name of the each car
- **mileage**: how many distance the car passed. (in kilometers)
- **prices**: price of a car (in Hungarian forint)