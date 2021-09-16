import pandas as pd
import requests
from bs4 import BeautifulSoup

car_names = []
list_of_prices = []
mileages = []
url = "https://joautok.hu/hasznaltauto/opel/astra?page=1"

page_counter = 2
while len(list_of_prices) < 400:
    response = requests.get(url)
    page = response.content

    soup = BeautifulSoup(page, 'html.parser')

    items_div = soup.find('div', id='items')
    a_items = items_div.find_all('a', class_='item')

    for a in a_items:
        # add prices
        list_of_prices.append(a['data-price'])
        # add names
        font_div = a.find('div', class_='image')
        h2_div = a.find('div', class_='h2-top')
        span_element = h2_div.find('span')
        car_names.append(span_element.get_text())
        # add mileage
        upper_div = a.find('div', class_='details upper-details')
        year_div = upper_div.find('div', class_='year-odo')
        span_mileage = year_div.find('span', class_='dotted')
        mileages.append(span_mileage.get_text())

    url = url[:-1]
    url += str(page_counter)
    # increment page number in the url
    page_counter += 1

# show all names, mileages, prices
counter = 0
for item in list_of_prices:
    print("Price #" + str(counter) + ": " +
          list_of_prices[counter] +
          " name is: " + car_names[counter] +
          " mile is: " + mileages[counter])
    counter += 1


df = pd.DataFrame.from_dict(
    {'Names': car_names, 'Mileage': mileages, 'Prices': list_of_prices})
# save to excel file
df.to_excel('ch1ex4/raw/dataset.xlsx', header=True, index=False)