import requests,json

post_url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
content = input('输入需要word2vec提取的文字信息：（不得少于30字）\n')
data = {'content':content}
post = requests.post(post_url,headers = headers,data=data)

for item in post.json()['w2vlist']:
    print(item)