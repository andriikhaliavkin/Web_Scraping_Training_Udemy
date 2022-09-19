import requests
from bs4 import BeautifulSoup
import re

import pandas as pd

# # url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
# #
# # page = requests.get(url)
# #
# # soup = BeautifulSoup(page.text, 'lxml')
# # print(soup)
# # print('--------------------------')
# # print(soup.header)
# # print('--------------------------')
# # tag = soup.header.p.string
# # print(tag)
# # print('--------------------------')
# # tag = soup.header.a.attrs
# # print(tag)
#
new_url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
new_page = requests.get(new_url)
new_soup = BeautifulSoup(new_page.text, 'lxml')
# # header_test = new_soup.find('header')
# # print(header_test)
# print('--------------------------')
# new_div = new_soup.find('div', {'class': 'container test-site'})
# print(new_div)
# print('--------------------------')
#
new_element = new_soup.find('h4', {'class': 'pull-right price'})
print(new_element)
print('--------------------------')
# new_element = new_soup.find('h4', class_ = 'pull-right price')
# print(new_element)
new_element = new_soup.find_all('h4', {'class': 'pull-right price'})
print(new_element)
print('--------------------------')
new_element = new_soup.find_all('a', {'class': 'title'})
print(new_element)
print('--------------------------')
new_element = new_soup.find_all('p', {'class': 'pull-right'})
print(new_element)
print('--------------------------')
new_element = new_soup.find_all(['h4', 'p'])
print(new_element)
print('--------------------------')
new_element = new_soup.find_all(id = True)
print(new_element)
print('--------------------------')
new_element = new_soup.find_all(string = 'Iphone')
print(new_element)
print('--------------------------')
new_element = new_soup.find_all(string = re.compile('Iph'))
print(new_element)
print('--------------------------')
print('--------------------------')
print('--------------------------')
product_name = new_soup.find_all('a', class_ = 'title')
product_name_list =[]
for i in product_name:
    name = i.text
    product_name_list.append(name)

print(product_name_list)

price = new_soup.find_all('h4', class_ = 'pull-right price')
price_list = []
for i in price:
    price2 = i.text
    price_list.append(price2)
print(price_list)


table = pd.DataFrame({'product name': product_name_list, 'price list': price_list})
print(table)