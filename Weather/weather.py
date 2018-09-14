import requests
import argparse
import sys


#显示当天天气预报
def showmsg(weather_data):
    #显示时间
    date = weather_data.get('result').get('realtime')
    print('地点:{0} 现在时间：{1} 农历：{2} 获取该信息时间：{3}'.format(
        date['city_name'], date['date'], date['moon'], date['time']))
    #预报天气状况
    weather = weather_data.get('result').get('weather')
    weinfo = weather[0].get('info')
    a = {'dawn': '早晨', 'day': '白天', 'night': '晚上'}
    for k, v in weinfo.items():
        print('今天{0},天气{1},{2},{3}，平均温度是{4}'.format(a[k], v[1], v[3], v[4],
                                                    v[2]))
    print()
    #显示污染指数
    pm = weather_data.get('result').get('pm25').get('pm25')
    print('今天污染指数：\npm25={0} pm10={1} 污染等级{2}:{3}\n生活建议：{4}'.format(
        pm.get('pm25'), pm.get('pm10'), pm.get('level'), pm.get('quality'),
        pm.get('des')))
    #显示生活建议
    info = weather_data.get('result').get('life').get('info')
    f = {
        'ziwaixian': '紫外线的辐射程度是：',
        'kongtiao': '空调开还是不开好，我们觉得：',
        'ganmao': '人群流感频率：',
        'xiche': '洗车适宜程度：',
        'yundong': '运动适宜程度：',
        'chuanyi': '天气：'
    }
    for k, v in info.items():
        if k in f:
            print("-" * 100)
            print(f[k], ':', v[0])
            print("对此我们的建议是：今天%s" % v[1])


#预报未来四天天气状况
def future_weather(weather_data):
    weather = weather_data.get('result').get('weather')
    for i in range(1, len(weather)):
        print("未来第{0}天，日期是{1}，天气预计如下：".format(i,
                                              weather[i].get('date')))  #未来的时间
        weinfo = weather[i].get('info')
        a = {'dawn': '早晨', 'day': '白天', 'night': '晚上'}
        count = 1
        for k, v in weinfo.items():
            print('{0},天气{1},{2},{3}，平均温度是{4}'.format(a[k], v[1], v[3], v[4],
                                                      v[2]))
            if count % 3 == 0:
                print("-" * 80, '\n')
            count += 1


#接收一个城市名，返回api对该城市的所有天气预报信息
def weather_info(city,
                 appkey='2bcac5f5ad4e497eade7e600898e13f3',
                 url='http://api.avatardata.cn/Weather/Query'):
    p = {'key': appkey, 'cityname': city}
    s = requests.get(url, params=p)
    weather_data = s.json()
    err = weather_data.get('error_code') #获取异常代码
    error(err)
    return weather_data


#判断异常
def error(err):
    error_dict = {
        1: '参数错误',
        10001: '错误的请求KEY',
        10002: '该KEY无请求权限',
        10003: 'KEY过期',
        10004: '错误的OPENID',
        10005: '应用未审核超时，请提交认证',
        10006: '未知的请求源',
        10007: '被禁止的IP',
        10008: '被禁止的KEY',
        10009: '当前IP请求超过限制',
        10010: '请求超过次数限制，请购买套餐',
        10011: '账户余额不足，请充值',
        10012: '测试KEY超过请求限制',
        10013: '请求错误，请重试',
        10014: '接口维护',
        10015: '接口停用',
        10016: '当日调用次数到达上限，请明日重试或联系我们申请更多上限次数',
    }
    for k, v in error_dict.items():
        if err == k:
            print(v)
            exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("city", type=str, help="输入一个城市名")
    parser.add_argument(
        "-f", "--future", action="store_true", help="输入-f,显示该城市未来四天天气预报")
    args = parser.parse_args()
    weather_data = weather_info(args.city)
    if args.future:
        future_weather(weather_data)
    else:
        showmsg(weather_data)
