import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
print(soup)
print('--------------------------')
print(soup.header)
print('--------------------------')
tag = soup.header.p.string
print(tag)
print('--------------------------')
tag = soup.header.a.attrs
print(tag)
