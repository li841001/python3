import requests
from bs4 import BeautifulSoup
import re

res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/')
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='comment-body')
# print(items)
k = 0
for item in items:
    author = item.find(class_='fn')
    k += 1
    # print(author.text)
    time = item.find('time')
    content = item.find(class_='comment-content')
    # print(content.text)
    print('%s%s\n发表评论：\n%s\n\n'%(author.text,time.text,content.text))

print(k)
