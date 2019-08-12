import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

name_input = input('输入要查询的电影名称：')
name = name_input.encode('gbk')
# print(quote(name))
link = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+ quote(name)

res = requests.get(link)
res.encoding = 'gbk'
html_search = res.text
soup_search = BeautifulSoup(html_search,'html.parser')
search_result = soup_search.find('div',class_='co_content8').find('ul').text.strip()

if search_result != '共0页/0条记录':     #   万一找不到电影
    link_search = soup_search.find('div',class_='co_content8').find('a')['href']


    link_search_w = 'https://www.ygdy8.com'+link_search
    res_movie = requests.get(link_search_w)
    res_movie.encoding = 'gbk'          #   解决乱码问题
    html_movie = res_movie.text
    soup_movie = BeautifulSoup(html_movie,'html.parser')
    download_mag = soup_movie.find('div',class_='co_content8').find('p').find('a')['href']
    download_ftp = soup_movie.find('div',class_='co_content8').find('tbody').find('a')['href']
    print('磁力链接：\n',download_mag,'\n')
    print('FTP链接：\n',download_ftp,'\n')
else:
    print('未找到电影')