import requests
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# 根据获取歌词位置的Headers重写地址
headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }


for i in range(5):
    i += 1

    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'remoteplace':'txt.yqq.lyric',
        'searchid': '107733233079104790',
        'aggr': '0',
        'catZhida': '1',
        'lossless': '0',
        'sem': '1',
        't': '7',
        'p': str(i),
        'n': '5',
        'w': '周杰伦',
        'g_tk': '1827005009',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf - 8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
        }
    #   根据点击歌词后的网络请求信息重写了params，经测试p为页数

    res_lyric = requests.get(url,headers=headers,params=params)
    print(res_lyric.status_code)
    # 发起请求
    lyric_jason = res_lyric.json()
    #   获取json
    lyric_list = lyric_jason['data']['lyric']['list']
    #   获取歌词列表
    for lyric_item in lyric_list:
        lyric = lyric_item['content']
        print(lyric.replace('\\n','\n').replace('<em>','').replace('</em>',''),'\n','--------','\n')