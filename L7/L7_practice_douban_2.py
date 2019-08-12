import requests,csv
from bs4 import BeautifulSoup

    #   csv文件操作
with open('DoubanTopMovie.csv','w',newline='',encoding='utf-8') as csv_file:

    writer = csv.writer(csv_file)
    #   写入首行作为表头
    writer.writerow(['排名',
                     '片名',
                     '简介',
                     '评分',
                     '电影链接'])


    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
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
            writer.writerow(movie_cell)




csv_file = open('DoubanTopMovie.csv','r',newline='',encoding='utf-8')
reader = csv.reader(csv_file)
for row in reader:
    print(row)