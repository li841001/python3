import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work/')
html = res.text
soup = BeautifulSoup(html,'html.parser')

main_item = soup.find(class_='site-content')
items = main_item.find_all('article')

for item in items:
    title = item.find(class_='entry-title')
    title1 = title.find('a')
    pub_time = item.find(class_='entry-date published')
    print(title1.text,pub_time.text,title1['href'])