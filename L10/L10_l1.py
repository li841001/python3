# 本地Chrome浏览器设置方法
from selenium import  webdriver
import time
#   本地浏览器设置实例
driver = webdriver.Chrome()

# chrome_options.add_argument('--headless') # 对浏览器的设置
# driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 声明浏览器对象

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 等待2秒
labels = driver.find_elements_by_tag_name('label') # 解析网页并提取第一个<lable>标签
source_code = driver.page_source
print(type(source_code))
# print(source_code)
for label in labels:
    print(label.text) # 打印label的文本

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('步摇碧莲')
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('卡西最棒')
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(1)
driver.close() # 关闭浏览器

# 以下方法都可以从网页中提取出'你好，蜘蛛侠！'这段文字

# find_element_by_tag_name：通过元素的名称选择
# # 如<h1>你好，蜘蛛侠！</h1>
# # 可以使用find_element_by_tag_name('h1')
#
# find_element_by_class_name：通过元素的class属性选择
# # 如<h1 class="title">你好，蜘蛛侠！</h1>
# # 可以使用find_element_by_class_name('title')
#
# find_element_by_id：通过元素的id选择
# # 如<h1 id="title">你好，蜘蛛侠！</h1>
# # 可以使用find_element_by_id('title')
#
# find_element_by_name：通过元素的name属性选择
# # 如<h1 name="hello">你好，蜘蛛侠！</h1>
# # 可以使用find_element_by_name('hello')
#
# #以下两个方法可以提取出超链接
#
# find_element_by_link_text：通过链接文本获取超链接
# # 如<a href="spidermen.html">你好，蜘蛛侠！</a>
# # 可以使用find_element_by_link_text('你好，蜘蛛侠！')
#
# find_element_by_partial_link_text：通过链接的部分文本获取超链接
# # 如<a href="https://localprod.pandateacher.com/python-manuscript/hello-spiderman/">你好，蜘蛛侠！</a>
# # 可以使用find_element_by_partial_link_text('你好')
