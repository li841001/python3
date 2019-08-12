import requests,json

api_url = 'http://openapi.tuling123.com/openapi/api/v2'
api_key = '9e724cde8c1e404da00012d12a7ca975'
userId = 'Demo'
img_url = 'imageUrl'
location = { "city": "杭州",
            "province": "浙江",
            "street": "东宁路"}
#   图灵API调用
class turing:
    def __init__(self):
        usrinput = input('用户--%s：\n'%userId)

        data = {
                    "reqType":0,
                    "perception": {
                        "inputText": {
                            "text": usrinput
                        },
                        "inputImage": {
                            "url": img_url
                        },
                        "selfInfo": {
                            "location": location
                        }
                    },
                    "userInfo": {
                        "apiKey": api_key,
                        "userId": userId
                    }
                }
        data_json = json.dumps(data).encode('utf-8')
        post = requests.post(api_url,headers={'Content-Type':'application/json'},data=data_json)
        response_json = post.json()

        #   返回状态信息：
        self.code = response_json['intent']['code']
        #   返回内容：
        self.results = response_json['results']

result_types = ['text','voice','video','image','news']
results = turing().results
for result in results:
    for result_type in result_types:
        if result['resultType'] == result_type:
            print(result['values'][result_type])