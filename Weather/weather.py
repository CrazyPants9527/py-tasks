import requests


def showmsg(weather_data):
    #显示时间
    date = weather_data['result']['realtime']
    print('地点:{0} 现在时间：{1} 农历：{2} {3}'.format(date['city_name'], date['date'],
                                              date['moon'], date['time']))
    #预报天气状况
    weather = weather_data['result']['weather']
    weinfo = weather[0]['info']
    for k, v in weinfo.items():
        print(k, ':', v)
    print()
    #显示污染指数
    pm = weather_data['result']['pm25']['pm25']
    print('今天污染指数：\npm25={0} pm10={1} 污染等级{2}:{3}\n生活建议：{4}'.format(
        pm['pm25'], pm['pm10'], pm['level'], pm['quality'], pm['des']))
    #显示生活建议
    info = weather_data['result']['life']['info']
    f = {
        'ziwaixian': '紫外线',
        'kongtiao': '空调',
        'wuran': '污染',
        'ganmao': '感冒',
        'xiche': '洗车',
        'yundong': '运动',
        'chuanyi': '穿衣'
    }
    for k, v in info.items():
        print(f[k], ':', v)


appkey = '2bcac5f5ad4e497eade7e600898e13f3'
city = input('请输入查询的地名：')
value = {'key': appkey, 'cityname': city}
url = 'http://api.avatardata.cn/Weather/Query'
s = requests.get(url, params=value)
weather_data = s.weather_dataon()
weather = weather_data['result']['weather']
weinfo = weather[0]['info']
showmsg(weather_data)
