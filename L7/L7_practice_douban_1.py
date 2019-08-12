import requests,openpyxl
from bs4 import BeautifulSoup

    #   excel文件操作
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Top250'

sheet['A1'] = '排名'
sheet['B1'] = '片名'
sheet['C1'] = '简介'
sheet['D1'] = '评分'
sheet['E1'] = '影片链接'


headers = {'User-Agent':'Chrome/75.0.3770.142'}
moviePy = []
for i in range(0,250,25):
    res_href = 'https://movie.douban.com/top250?start=%s&filter='%str(i)
    res = requests.get(res_href,headers=headers)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    movie_li_allocation = soup.find('div',class_='article')
    movie_li = movie_li_allocation.find_all('li')
    for movies in movie_li:
        movie_name = movies.find('div',class_='hd').find('span',class_='title').text.strip().replace('\n','')
        movie_href = movies.find('div',class_='hd').find('a')['href']
        movie_rank = movies.find('div',class_='pic').text.replace('\n','')
        # movie_info = movies.find('div',class_ = 'bd').text.strip()
        try:
            movie_quote = movies.find('span', class_='inq').text
        except AttributeError:
            movie_quote = ''
        try:
            movie_rate = movies.find('span', class_='rating_num').text
        except AttributeError:
            movie_rate = ''
        movie_cell = [movie_rank,movie_name,movie_quote,movie_rate,movie_href]
        # moviePy.append(movie_cell)
        sheet.append(movie_cell)
wb.save('DoubanTopMovie.xlsx')


wb = openpyxl.load_workbook('DoubanTopMovie.xlsx')  #   读取已有文件
sheet = wb['Top250']
for row in sheet.rows:
    # for cell in row:
    #     print(cell)   #如需要遍历每个单元格
    print(row)
# for k in moviePy:
#     print(k)