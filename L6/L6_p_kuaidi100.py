import requests

#   访问地址
url =   'https://www.kuaidi100.com/query'

#   头文件
headers =   {'origin':'https://www.kuaidi100.com/',
             'referer':'https://www.kuaidi100.com/',
             'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    }

#   单号信息输入
postid_num  =   input('请输入要查询的快递单号：\n')

#   判断快递公司
params_type = {
    'resultv2': '1',
    'text': postid_num
    }
url_type = 'https://www.kuaidi100.com/autonumber/autoComNum'
res_type = requests.get(url_type,headers=headers,params=params_type)
type_json = res_type.json()
companies = type_json['auto'][0]['comCode']
print('快递公司为：',companies)
#   顺丰需要填入手机尾号后四位
phone = ''
if companies == 'shunfeng':
    phone = input('请输入手机尾号后四位：')
else:
    phone = ''

params_main = {
    'type': companies,
    'postid': str(postid_num),
    'temp': '0',
    'phone': str(phone)
    }

res = requests.get(url,headers=headers,params=params_main)
res_json = res.json()
info = res_json['data']
if info == []:
    print(res_json['message'])
else:
    for info_print in info:
        print(info_print['time'],info_print['context'],'\n')