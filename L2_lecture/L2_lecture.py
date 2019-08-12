import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
local_file = res.content

with open('sipder-men5.0.html','wb') as lf:
    lf.write(local_file)