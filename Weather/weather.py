import requests
import argparse


#显示当天天气预报
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


#预报未来四天天气状况
def future_weather(weather_data):
    weather = weather_data['result']['weather']
    for i in range(1, len(weather)):
        print(weather[i]['date'])  #未来的时间
        weinfo = weather[i]['info']
        for k, v in weinfo.items():
            print(k, ':', v)


#接收一个城市名，返回api对该城市的所有天气预报信息
def weather_info(city):
    appkey = '2bcac5f5ad4e497eade7e600898e13f3'
    url = 'http://api.avatardata.cn/Weather/Query'
    p = {'key': appkey, 'cityname': city}
    s = requests.get(url, params=p)
    weather_data = s.json()
    return weather_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("city", type=str, help="输入一个城市名")
    parser.add_argument("-f", "--future", help="输入-f,显示该城市未来四天天气预报")
    args = parser.parse_args()
    weather_data = weather_info(args.city)
    if args.future:
        future_weather(weather_data)
    else:
        showmsg(weather_data)
