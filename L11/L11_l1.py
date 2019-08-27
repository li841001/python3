import requests
from bs4 import BeautifulSoup

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='http://www.weather.com.cn/weather/101210101.shtml'

res = requests.get(url,headers=headers)
res.encoding = 'utf-8'

html_text = BeautifulSoup(res.text,'html.parser')
# print(html_text)

temp = html_text.find(class_='tem')
wea = html_text.find(class_='wea')

print(temp.text)
print(wea.text)

import smtplib
from email.mime.text import MIMEText
from email.header import Header
#连接服务器
#smtplib是python的一个内置库，所以不需要用pip安装
mailhost='smtp.qq.com'
#把qq邮箱的服务器地址赋值到变量mailhost上
qqmail = smtplib.SMTP_SSL()
#实例化一个smtplib模块里的SMTP类的对象，这样就可以SMTP对象的方法和属性了
account = 'li841001@qq.com'
psw = input('请输入授权码：')
qqmail.connect(mailhost,465)
#连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
#以上，皆为连接服务器的代码


# psw = 'lijia841123'

qqmail.login(account,psw)

receiver = 'pluslee@foxmail.com'
#引入Header和MIMEText模块
content='今日天气：---\n天气：%s\n温度：\n'%(wea.text,temp.txt)
#输入你的邮件正文
message = MIMEText(content, 'plain', 'utf-8')
#实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码.
subject = '今日天气'
#用input()获取邮件主题
message['Subject'] = Header(subject, 'utf-8')
message['From'] = account
message['To'] = receiver
#在等号的右边，是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。
try:
    qqmail.sendmail(account, receiver, message.as_string())
    print ('邮件发送成功')
except:
    print ('邮件发送失败')
#发送邮件，调用了sendmail()方法，写入三个参数，分别是发件人，收件人，和字符串格式的正文。
qqmail.quit()
#退出邮箱(断连)


#   第三方库schedule的使用
# import schedule
# import time
# #引入schedule和time
#
# def job():
#     print("I'm working...")
# #定义一个叫job的函数，函数的功能是打印'I'm working...'
#
# schedule.every(10).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
# schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
# schedule.every().day.at("10:30").do(job) #部署在每天的10:30执行job()函数的任务
# schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
# schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
# #13-15都是检查部署的情况，如果任务准备就绪，就开始执行任务。