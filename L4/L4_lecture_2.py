import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.xiachufang.com/explore/')
html = res.text
soup = BeautifulSoup(html,'html.parser')
# tag_items = soup.find_all('div',class_='info pure-u')
# info = []
# for item in tag_items:
#     name_allocation = item.find('p',class_='name')
#     name = name_allocation.find('a')
#     material= item.find('p',class_='ing ellipsis')
#     rename = name.text.strip()
#     href = 'http://www.xiachufang.com'+name['href']
#     print(rename,material.text,'\n',href)
#     info_cell = [rename,href,material.text]
#     info.append(info_cell)
#
# print(info)

# 第二种检索方式
food_name_all = soup.find_all('p',class_='name')
material_all = soup.find_all('p',class_='ing ellipsis')
list_all = []
for i in range(len(food_name_all)):
    food_name = food_name_all[i].find('a').text.strip()
    food_href = food_name_all[i].find('a')['href']
    whole_href = 'http://www.xiachufang.com'+food_href
    material = material_all[i].text.replace('\n','')
    list_cell = [food_name,whole_href,material]
    list_all.append(list_cell)
print(list_all)