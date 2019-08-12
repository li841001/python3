from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
from bs4 import BeautifulSoup
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行


driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
time.sleep(2)

button = driver.find_element_by_class_name('js_get_more_hot') # 根据类名找到【点击加载更多】
button.click() # 点击
time.sleep(2) # 等待两秒

pageSource = driver.page_source # 获取Elements中渲染完成的网页源代码
soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
comments = soup.find('ul',class_='js_hot_list').find_all('li',class_='js_cmt_li') # 使用bs提取元素
print(len(comments)) # 打印comments的数量

for comment in comments: # 循环
    sweet_name = comment.find('h4').find('a')
    sweet = comment.find('p') # 提取评论
    print ('%s 评论：%s\n ---\n'%(sweet_name.text,sweet.text)) # 打印评论
driver.close() # 关闭浏览器 # 关闭浏览器