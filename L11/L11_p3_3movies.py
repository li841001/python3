import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random

#邮箱账号信息
account = 'li841001@163.com'
psw = 'lijia841123'
receiver = 'pluslee@foxmail.com'

def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
    moviePy = []
    for i in range(0, 250, 25):
        res_href = 'https://movie.douban.com/top250?start=%s&filter=' % str(i)
        res = requests.get(res_href, headers=headers)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        movie_li_allocation = soup.find('div', class_='article')
        movie_li = movie_li_allocation.find_all('li')
        for movies in movie_li:
            movie_name = movies.find('div', class_='hd').find('span', class_='title').text.strip().replace('\n', '')
            movie_href = movies.find('div', class_='hd').find('a')['href']
            movie_rank = movies.find('div', class_='pic').text.replace('\n', '')
            # movie_info = movies.find('div',class_ = 'bd').text.strip()
            try:
                movie_quote = movies.find('span', class_='inq').text
            except AttributeError:
                movie_quote = ''
            try:
                movie_rate = movies.find('span', class_='rating_num').text
            except AttributeError:
                movie_rate = ''
            movie_cell = [movie_rank, movie_name, movie_quote, movie_rate, movie_href]
            
        moviePy.append(movie_cell)
    #   随机样本的方法，往上抄来的
    movies_random = random.sample(moviePy,3)
    temp = []
    for movies in movies_random:
        movie_3 = '排名：%s\n片名：%s\n简介：%s\n评分：%s\n链接：%s\n'%(movies[0],movies[1],movies[2],movies[3],movies[4])
        temp.append(movie_3)
    movie_3 = '\n\n'.join(temp)
    movie_3text = '已从豆瓣TOP250中随机挑选了3部电影：\n-------\n%s'%(movie_3)
    return movie_3text

# print(get_movies())

def send_email(content_txt):
    content = content_txt
    msg = MIMEText(content,'plain','utf-8')
    msg['From'] = Header(account)
    msg['To'] = Header(receiver)
    msg['Subject'] = Header('豆瓣电影随机三部','utf-8')
    mailhost = 'smtp.163.com'
    server = smtplib.SMTP()
    server.connect(mailhost,25)
    server.login(account,psw)
    try:
        server.sendmail(account,receiver,msg.as_string())
        print('发送成功')
    except:
        print('发送失败')

def job():
    print('开始')
    movies3 = get_movies()
    send_email(movies3)
    print('结束')

job()