# Chapter 1, exercise 4

In this exercise, data on used cars with the model **Opel Astra** was collected. As a source, [joautok.hu ](https://joautok.hu/hasznaltauto/opel/astra) website was used. 

It was difficult to understand the structure of the website. Additionally, it was not clear how to get a specific data (price, name, mileage) for each car. Fortunately, a [YouTube Video Tutorial](https://www.youtube.com/watch?v=Jnn2kIqPH7o) was helpful to understand how to do web scraping using Python. Python code that was used for web scraping can be found in _webScrapingHTML.py_ file. Also, [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library was used for pulling data out of HTML. The result is stored in Excel file using [pandas](https://pandas.pydata.org/) and [openpyxl](https://openpyxl.readthedocs.io/en/stable/) library as it was suggested in [stackoverflow](https://stackoverflow.com/questions/43853053/write-data-present-in-list-to-a-column-in-excel-sheet-using-xlxs-writer-module).

Name, price, mileage of each car was scraped from the website. Then, this data is stored into *dataset.xlsx* Excel file inside **raw** folder. This file contains the data for 432 cars. 

*dataset.xlsx* Excel file contains the following variables:

- **Names**: name of the each car
- **Mileage**: how many distance the car passed. (in kilometers)
- **Prices**: price of a car (in Hungarian forint)
