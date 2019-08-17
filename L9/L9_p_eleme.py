import requests,json

#   模拟登陆·方法
session = requests.session()
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
#   读取cookies
def cookies_read():
    cookies_text = open('cookies_ele.txt','r')
    cookies_dict = json.loads(cookies_text.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return cookies
#   登陆函数---包含了短信验证码、token获取，未做图形验证
def log_in():
    url_sendcode = ' https://h5.ele.me/restapi/eus/login/mobile_send_code'
    # url_get_token  = 'https://h5.ele.me/restapi/eus/login'
    usr_cellphone = input('请输入手机号码：')
    data_sendcode = {'captcha_hash': "",
            'captcha_value': "",
            'mobile': usr_cellphone,
            'scf': ""}
    #   获取校验token
    response = session.post(url_sendcode,headers=headers,data=data_sendcode)
    response_token = response.json()['validate_token']
    usr_token = input('请输入手机验证码：')
    url_login = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
    data_login = {'mobile': usr_cellphone,
                'scf': "ms",
                'validate_code': usr_token,
                'validate_token': response_token}
    login = session.post(url_login,headers=headers,data=data_login)
    #   写入cookies
    cookies_dict = requests.utils.dict_from_cookiejar(login.cookies)
    cookies_str  = json.dumps(cookies_dict)
    with open('cookies_ele.txt','w') as wf:
        wf.write(cookies_str)

#   选择地址
def location():
    url_location = 'https://www.ele.me/restapi/bgs/poi/search_poi_nearby'
    address = input('请输入你的位置：')
    params = {'geohash': 'wtmknpnr9yy3',
            'keyword': address,
            'latitude': '30.274151',
            'limit': '20',
            'longitude': '120.155151',
            'type': 'nearby'}
    location_res = requests.get(url_location,headers=headers,params=params)
    location_json = location_res.json()
    print('以下是--%s--有关的位置：\n'%address)
    i = 0
    for location in location_json:
        print('%d--%s--%s'%(i,location['name'],location['short_address']))
        i += 1
    chose_num = int(input('请选择您需要的位置所对应的序号：'))
    location_final = location_json[chose_num]
    print(location_final)
    return location_final

#   获取餐馆列表
def resturant(session):
    url_rst = 'https://www.ele.me/restapi/shopping/restaurants?'
    location_detail = location()
    geohash = location_detail['geohash']
    latitude = location_detail['latitude']
    longitude = location_detail['longitude']
    params = {'extras[]': 'activities',
            'geohash': geohash,
            'latitude': str(latitude),
            'limit': '24',
            'longitude': str(longitude),
            'offset': '0',
            'terminal': 'web'}
    res = session.get(url_rst,headers=headers,params=params)
    print(res.status_code)
    res_json = res.json()
    resturant_list = []
    for resturant in res_json:
        resturant_info = ['名称：'+resturant['name'],'评分：'+str(resturant['rating']),'简介：'+resturant['promotion_info'],'店铺链接：'+resturant['scheme']]
        resturant_list.append(resturant_info)
    return resturant_list

try:
    session.cookies = cookies_read()
except  FileNotFoundError:
    log_in()
    session.cookies = cookies_read()

rst_list = resturant(session)
for i in rst_list:
    # print(i)
    for k in i:
        print(k)
    print('\n\n')