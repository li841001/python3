from gevent import monkey
monkey.patch_all()

import gevent,requests,time,csv
from gevent.queue import Queue
from bs4 import BeautifulSoup

start = time.time()
#   地址列表组合
url_1 = 'http://www.mtime.com/top/tv/top100/'
url_list = [url_1]
for i in range(2,11):
    url_rest = url_1+'index-%d.html'%i
    url_list.append(url_rest)

#   把地址放进队列
work = Queue()
for url in url_list:
    work.put_nowait(url)

#   任务队列循环
tv_info_list = []
def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        tv_list = soup.find(class_='top_list').find_all('li')
        for tv in tv_list:
            tv_rank = int(tv.find(class_='number').find('em').text)
            tv_name = tv.find(class_='mov_con').find('h2').text.replace('&nbsp', '/').replace('\xa0','/')
            tv_href = tv.find(class_='mov_con').find('h2').find('a')['href']
            tv_rating = tv.find(class_='point').find(class_='total').text.strip() + tv.find(class_='point').find(
                class_='total2').text.strip()
            try:
                tv_brief = tv.find(class_='mov_con').find(class_='mt3').text
            except:
                tv_brief = '暂无简介'
            tv_info = [tv_rank, tv_name, tv_rating, tv_brief, tv_href]
            tv_info_list.append(tv_info)

#   任务协程执行
tasks_list = []
for i in range(5):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)
end = time.time()
print(end-start)

tv_info_list.sort()
print(tv_info_list)

with open('Top100_movie.csv','w',newline='',encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['排名',
                     '片名',
                     '评分',
                     '简介',
                     '链接'])
    for row in tv_info_list:
        writer.writerow(row)




