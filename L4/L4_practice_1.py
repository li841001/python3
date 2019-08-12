import requests
from bs4 import BeautifulSoup
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
        movie_name = movies.find('div',class_='hd').text.strip().replace('\n','')
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
        moviePy.append(movie_cell)

for k in moviePy:
    print(k)