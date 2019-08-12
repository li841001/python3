import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for item in items:
    name = item.find('h3')
    star = item.find('p')
    price = item.find(class_='price_color')
    print(name.text,'\n',star['class'],'\n',price.text,'\n')
