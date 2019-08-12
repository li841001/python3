import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')

content = res.text

with open('HTTP状态响应吗.txt','a+') as c:
    c.write(content)