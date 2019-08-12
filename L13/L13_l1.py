from header import headers
headers = headers.headers

#导入所需的库和模块：

from gevent import monkey
monkey.patch_all()
#让程序变成异步模式。
import gevent,requests, bs4, csv,time
from gevent.queue import Queue
work = Queue()
# 创建队列对象，并赋值给work。
start = time.time()

# 前3个常见食物分类的前3页的食物记录的网址：
url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        work.put_nowait(real_url)
# 通过两个for循环，能设置分类的数字和页数的数字。
# 然后，把构造好的网址用put_nowait方法添加进队列里。

# 第11个常见食物分类的前3页的食物记录的网址：
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for x in range(1, 4):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)
# 通过for循环，能设置第11个常见食物分类的食物的页数。
# 然后，把构造好的网址用put_nowait方法添加进队列里。

food_list = []
def crawler():
#定义crawler函数

    while not work.empty():
    #当队列不是空的时候，就执行下面的程序。
        url = work.get_nowait()
        #用get_nowait()方法从队列里把刚刚放入的网址提取出来。
        res = requests.get(url, headers=headers)
        #用requests.get获取网页源代码。
        bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
        #用BeautifulSoup解析网页源代码。
        foods = bs_res.find_all('li', class_='item clearfix')
        #用find_all提取出<li class="item clearfix">标签的内容。
        for food in foods:
        #遍历foods
            food_name = food.find_all('a')[1]['title']
            #用find_all在<li class="item clearfix">标签下，提取出第2个<a>元素title属性的值，也就是食物名称。
            food_url = 'http://www.boohee.com' + food.find_all('a')[1]['href']
            #用find_all在<li class="item clearfix">元素下，提取出第2个<a>元素href属性的值，跟'http://www.boohee.com'组合在一起，就是食物详情页的链接。
            food_calorie = food.find('p').text
            #用find在<li class="item clearfix">标签下，提取<p>元素，再用text方法留下纯文本，也提取出了食物的热量。
            food_cell = [food_name,food_calorie,food_url]
            food_list.append(food_cell)

tasks_list = []
for i in range(8):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)
mid = time.time()
print(mid-start)
with open('食物热量表.csv','w',newline='',encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['食物名称','热量/100g','详情链接'])
    for row in food_list:
        writer.writerow(row)
end = time.time()
print(end-start)