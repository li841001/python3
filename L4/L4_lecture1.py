import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.xiachufang.com/explore/')
html = res.text
soup = BeautifulSoup(html,'html.parser')
tag_items = soup.find_all('div',class_='info pure-u')

info = []

for item in tag_items:
    name_allocation = item.find('p',class_='name')
    name = name_allocation.find('a')
    material= item.find('p',class_='ing ellipsis')
    rename = name.text.strip()
    # 去掉空字符
    re_material = material.text.replace('\n','')
    # 去掉换行符号
    href = 'http://www.xiachufang.com'+name['href']
    print(rename,material.text,'\n',href)
    info_cell = [rename,href,re_material]
    info.append(info_cell)

print(info)