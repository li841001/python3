from gevent import monkey
#   从gevent库里倒入monkey模块
monkey.patch_all()
#   moneky.patch_all()能把程序变成协作式运行，即可以帮助程序实现异步
import gevent,time,requests

start = time.time()

url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

def crawler(url):
#   定义一个crawler（）函数
    r = requests.get(url)
    print(url,time.time()-start,r.status_code)

tasks_list = []
#   创建空的任务列表
for url in url_list:
    task = gevent.spawn(crawler,url)
    #   用个 gevent.spawn()函数创建任务
    tasks_list.append(task)
    #   往任务列表里添加任务
gevent.joinall(tasks_list)
#   执行任务列表里面的所有任务，让爬虫以写成方式开始爬取网站
end = time.time()
print(end-start)