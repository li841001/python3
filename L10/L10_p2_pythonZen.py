from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_argument('--headless')#  浏览器静默模式--headless
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

form_input1 = driver.find_element_by_id('teacher')
form_input1.send_keys('吴枫')

form_input2 = driver.find_element_by_id('assistant')
form_input2.send_keys('卡西')

button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(2)

#   使用selenium方法查找文章内容
def selenium_content():
    contents = driver.find_elements_by_class_name('content')
    article = {}
    for content in contents:
        h = content.find_element_by_tag_name('h1')
        p = content.find_element_by_id('p')
        article.update({h.text:p.text})
    return article

def bs4_content():
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    contents = soup.find_all('div',class_='content')
    article_bs ={}
    for content in contents:
        h = content.find('h1').text
        p = content.find('p').text
        article_bs.update({h:p})
    return article_bs

result_a = selenium_content()
result_b = bs4_content()
for a_key,a_result in result_a.items():
    print(a_key,'\n',a_result.replace('\n','\n'),'\n-----\n')
for b_key,b_result in result_b.items():
    print(b_key,'\n',b_result.replace('\n','\n'),'\n-----\n')

driver.quit()