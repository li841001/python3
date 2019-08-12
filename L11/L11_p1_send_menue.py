import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time


accout = 'li841001@163.com'
psw = 'lijia841123'
receiver = 'pluslee@foxmail.com'


def get_menu():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')

    list_all = []

    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text.strip()
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        list_all.append([name,URL,ingredients])

    list = []
    for i in list_all:
        list.append('\n'.join(i))
    list = '\n\n'.join(list)
    return list


def send_email(list):
    global accout,psw,receiver
    content = list
    msg = MIMEText(content,'plain','utf-8')    #   内容
    msg['From'] = Header(accout)                #   发件人
    msg['To'] = Header(receiver)                #   收件人
    msg['Subject'] = Header('本周菜单','utf-8')         #   主题
    mailhost = 'smtp.163.com'
    server = smtplib.SMTP()
    server.connect(mailhost, 25)
    server.login(accout, psw)
    try:
        server.sendmail(accout,receiver,content.as_string())
        print('发送成功')
    except:
        print('发送失败')
    # server.sendmail(accout,receiver,msg.as_string())
    server.quit()

def job():
    list = get_menu()
    send_email(list)
    print('任务完成')
job()
# schedule.every().friday.at('15:00').do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(10)