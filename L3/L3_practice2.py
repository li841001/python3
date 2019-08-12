import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/')
html = res.text
soup = BeautifulSoup(html,'html.parser')
main_item = soup.find(class_='side_categories')
items = main_item.find_all('a')
# print(items1)
print(items)
k = 0
for item in items:
    # k += 1
    # print(k)
    category = item.find('a')
    try:
        print('%s\n%s\n'%(item.text,item['href']))
    except AttributeError:
        continue