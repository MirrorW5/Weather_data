import re
import ssl
from hoshino import Service, priv
from hoshino.typing import CQEvent
from hoshino import R
ssl._create_default_https_context = ssl._create_unverified_context
from datetime import datetime
from datetime import timedelta
import locale
import requests
import json
import random
import nonebot

sv = Service('autoRenewTomorrow', help_='''
自动预报第一天
'''.strip())

temp_max = []
temp_min = []
sun = []
rain = []
weather = []
gusts = []
date = []
prob = []
thunder = []

date_szmb = []
temp_max_szmb = []
temp_min_szmb = []

@sv.scheduled_job('cron', hour='18', minute='00',second='40')
async def autoRenewTomorrow():
    headers = {
        'authority':'meteologix.com' ,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
        'accept-language': 'zh-CN,zh;q=0.9' ,
        'cache-control': 'max-age=0' ,
        'sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' ,
        'sec-ch-ua-mobile':'?0' ,
        'sec-ch-ua-platform':'"Windows"' ,
        'sec-fetch-dest':'document' ,
        'sec-fetch-mode':'navigate' ,
        'sec-fetch-site':'none' ,
        'sec-fetch-user':'?1' ,
        'upgrade-insecure-requests':'1' ,
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 '
    }
    
  
    try:

        def temp_max_modify(sun,temp_max):
            temp_max_f = (float(sun)/10) * 2 + float(temp_max)
            temp_max_f = round(temp_max_f,1)
            return temp_max_f

        def temp_min_modify(temp_min):
            temp_min_f = float(temp_min)
            if temp_min_f <= 5:
                temp_min_f = temp_min_f + 2
            elif temp_min_f > 5 and temp_min_f <= 8:
                temp_min_f = temp_min_f + 1.8
            elif temp_min_f > 8 and temp_min_f <= 12:
                temp_min_f = temp_min_f + 1.5
            elif temp_min_f > 12 and temp_min_f <= 16:
                temp_min_f = temp_min_f + 1.2
            elif temp_min_f > 16 and temp_min_f <= 20:
                temp_min_f = temp_min_f + 1
            elif temp_min_f > 20:
                temp_min_f = temp_min_f + 0.5
            temp_min_f = round(temp_min_f,1)
            return temp_min_f

        def handle(data_str):
            data_str = data_str.replace(' ', '')
            data_str = data_str.replace(',null', '')
            data_str = data_str.replace('data:[', '')
            data_str = data_str.replace('\n', '')
            data_str = data_str.replace('\'', '')
            data_str = data_str.replace(']', '')
            return data_str

        def judgeWeather(sun,prec,gusts,thunder):
            totalClouds = 100 - sun/10*100
            totalTag = '000'
            if prec >= 50:
                if gusts > 70 :
                    if thunder == 1:
                        totalTag = '750' #
                    else:
                        totalTag = '700'
                else:
                    if thunder == 1:
                        totalTag = '550'
                    else:
                        totalTag = '500'
            elif prec >= 25 and prec < 50:
                if prec < 35:
                    totalTag = '302'
                elif prec >= 35:
                    if thunder == 1:
                        totalTag = '350'
                    else:
                        totalTag = '300'
            elif prec < 25:
                if totalClouds < 20:
                    if prec < 1:
                        totalTag = '100'
                    elif prec >= 1 and prec < 10:
                        totalTag = '102'
                    elif prec >= 10:
                        if thunder == 1:
                            totalTag = '140'
                        else:
                            totalTag = '103'
                elif totalClouds >= 20 and totalClouds < 50:
                    if prec < 1:
                        totalTag = '101'
                    else:
                        totalTag = '301'
                elif totalClouds >= 50 and totalClouds < 80:
                    if prec < 1:
                        totalTag = '201'
                    elif prec >= 1 and prec < 10:
                        totalTag = '202'
                        if prec >= 3 and thunder == 1:
                            totalTag = '240'
                    elif prec >= 10:
                        if thunder == 1:
                            totalTag = '240'
                        else:
                            totalTag = '203'
                elif totalClouds >= 80 and totalClouds < 90:
                    if prec < 1:
                        totalTag = '200'
                    elif prec >= 1 and prec < 10:
                        totalTag = '202'
                        if prec >= 3 and thunder == 1:
                            totalTag = '240'
                    elif prec >= 10:
                        if thunder == 1:
                            totalTag = '240'
                        else:
                            totalTag = '203'
                elif totalClouds >= 90:
                    if prec < 1:
                        totalTag = '255'
                    elif prec >= 1 and prec < 10:
                        totalTag = '202'
                        if prec >= 3 and thunder == 1:
                            totalTag = '240'
                    elif prec >= 10:
                        if thunder == 1:
                            totalTag = '240'
                        else:
                            totalTag = '203'
            return totalTag

        def getSzmbMessage():
            global date_szmb,temp_max_szmb,temp_min_szmb
            url_szmb = 'https://weather.121.com.cn/data_cache/szWeather/sz10day_new.js'
            getdata_szmb = requests.get(url_szmb, headers=headers)
            info_szmb = getdata_szmb.text
            index1 = info_szmb.find('[')
            index2 = info_szmb.find(']')
            info_szmb = info_szmb[index1:index2+1]
            info_szmb_list = json.loads(info_szmb)
            for i in range(0,int(len(info_szmb_list))):
                info_szmb_str = json.dumps(info_szmb_list[i])
                weather_dic = json.loads(info_szmb_str)
                temp_min_szmb.append(float(weather_dic['minT']))
                temp_max_szmb.append(float(weather_dic['maxT']))
                date_szmb.append(weather_dic['reportTime'][5:10])

        def findIndex(find_str,list):
            i = 0
            for k in list:
                if k == find_str:
                    return i
                else:
                    i = i + 1
            return -1

        def getWeatherMessage():
            url_mete_7days = 'https://meteologix.com/cn/ajax_pub/weathertrend14days?city_id=1795565'
            getdata_mete_7days = requests.get(url_mete_7days, headers=headers)
            info_mete_7days = getdata_mete_7days.text

            global temp_max,temp_min,date,prob,thunder

            index = info_mete_7days.find('hc_data_14days_xaxis')
            info_mete_7days = info_mete_7days[index:]
            index1 = info_mete_7days.find('[')
            index2 = info_mete_7days.find(']')
            date_str = info_mete_7days[index1+1:index2]
            date_str = handle(date_str)
            date_str = date_str.replace('/', '-')
            date = date_str.split(',')

            index = info_mete_7days.find('hc_data_14days_maxmin')
            info_mete_7days = info_mete_7days[index:]

            index = info_mete_7days.find('Tmax')
            info_mete_7days = info_mete_7days[index:]
            index1 = info_mete_7days.find('data')
            index2 = info_mete_7days.find(']')
            temp_str = info_mete_7days[index1:index2]
            temp_str = handle(temp_str)
            temp_max = temp_str.split(',')
            del temp_max[8:]
            info_mete_7days = info_mete_7days[index2:]

            index = info_mete_7days.find('Tmin')
            info_mete_7days = info_mete_7days[index:]
            index1 = info_mete_7days.find('data')
            index2 = info_mete_7days.find(']')
            temp_str = info_mete_7days[index1:index2]
            temp_str = handle(temp_str)
            temp_min = temp_str.split(',')
            del temp_min[8:]
            info_mete_7days = info_mete_7days[index2:]

            index = info_mete_7days.find('Sonnenscheindauer')
            info_mete_7days = info_mete_7days[index:]
            index1 = info_mete_7days.find('data')
            index2 = info_mete_7days.find(']')
            sun_str = info_mete_7days[index1:index2]
            sun_str = handle(sun_str)
            
            global sun
            sun = sun_str.split(',')
            for i in range(0,int(len(sun))):
                if sun[i] == 'null':
                    sun[i] = '0'
            info_mete_7days = info_mete_7days[index2:]

            index = info_mete_7days.find('Niederschlagsmenge')
            info_mete_7days = info_mete_7days[index:]
            index1 = info_mete_7days.find('data')
            index2 = info_mete_7days.find(']')
            rain_str = info_mete_7days[index1:index2]
            rain_str = handle(rain_str)
            rain = rain_str.split(',')
            info_mete_7days = info_mete_7days[index2:]

            index = info_mete_7days.find('hc_data_14days_wind')
            info_mete_7days = info_mete_7days[index+20:]
            index1 = info_mete_7days.find('data')
            index2 = info_mete_7days.find(']')
            gusts_str = info_mete_7days[index1:index2]
            gusts_str = handle(gusts_str)
            gusts = gusts_str.split(',')
            info_mete_7days = info_mete_7days[index2:]


            index = info_mete_7days.find('hc_data_14days_tsym')
            info_mete_7days = info_mete_7days[index:]
            index1 = info_mete_7days.find('[')
            index2 = info_mete_7days.find(']')
            thunder_str = info_mete_7days[index1 + 1:index2]
            thunder_temp = thunder_str.split(",")
            for i in thunder_temp:
                if i == "'null'":
                    thunder.append(0)
                elif i == "'1'":
                    thunder.append(1)



            for i in range(0,int(len(temp_min))):
                temp_min[i] = float(temp_min_modify(temp_min[i]))
            for i in range(0,int(len(temp_max))):
                if float(temp_max_modify(sun[i],temp_max[i])) > float(temp_min[i]):
                    temp_max[i] = float(temp_max_modify(sun[i],temp_max[i]))
                else:
                    temp_max[i] = float(temp_min[i]) + 1

            for i in range(0,8):
                weather.append(judgeWeather(float(sun[i]), float(rain[i]), float(gusts[i]), thunder[i]))


        getSzmbMessage()
        getWeatherMessage()

        temp_max_mean = []
        temp_min_mean = []
        
        global sun
        
        index = findIndex(date[0],date_szmb)
        for i in range(0,int(len(temp_max))):
            temp_max_mean.append(round(temp_max[i]*0.4 + temp_max_szmb[i+index]*0.6,0))
            temp_min_mean.append(round(temp_min[i]*0.4 + temp_min_szmb[i+index]*0.6,0))


        str_day0 = str(temp_max_mean[0])+','+str(temp_min_mean[0])+','+str(weather[0])

        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/day2_temp.txt", 'w',
                  encoding="utf-8") as f:
            f.write(str_day0)
        
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/add_temp.txt", 'w',
                  encoding="utf-8") as f:
            f.write(sun[1])
            
        bot = nonebot.get_bot()
        await bot.send_private_msg(user_id=2864309367, message=f'成功更新day0到temp')        
            
            
    except Exception as e:
        bot = nonebot.get_bot()
        await bot.send_private_msg(user_id=2864309367, message=f'【报错信息】更新day0到temp出错\n原因:{e}')        
        sv.logger.info('============更新day0到temp出错============')