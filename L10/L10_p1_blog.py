from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)
#   查找填入账号的位置，输入账号
usr_login = driver.find_element_by_id('user_login')
usr_login.clear()
usr_login = driver.find_element_by_id('user_login')
usr_login.send_keys('spiderman')
#   查找填入密码的位置，输入密码
usr_psw = driver.find_element_by_id('user_pass')
usr_psw.clear()
usr_psw = driver.find_element_by_id('user_pass')
usr_psw.send_keys('crawler334566')
#   查找提交按钮
button = driver.find_element_by_id('wp-submit')
button.click()
time.sleep(2)

articles = driver.find_elements_by_tag_name('article')
article = articles[1].find_element_by_partial_link_text('未来已来（三）')
article.click()
time.sleep(2)

comment_input = driver.find_element_by_id('comment')
comment_input.send_keys('评论中必须要带有“selenium”这个词。')

submit = driver.find_element_by_id('submit')
submit.click()
#
# page_source = driver.page_source
# soup = BeautifulSoup(page_source,'html.parser')
# right_html = soup.find('div',class_='component-right-union-wrap')
#
# print(right_html.text)

driver.quit()


