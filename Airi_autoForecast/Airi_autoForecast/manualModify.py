import requests
import json
import re
import ssl
from hoshino import Service, priv
from hoshino.typing import CQEvent
from hoshino import R
ssl._create_default_https_context = ssl._create_unverified_context

sv = Service('manualModify', bundle='手动修改', help_='''
手动修改
'''.strip())

@sv.on_prefix(('手动修改'))
async def manualModify(bot, ev: CQEvent):
    with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/data.json", "r", encoding="utf-8") as read_file:
        text = read_file.read()
    msg = f'{text}'
    await bot.send(ev, msg)
    
    
@sv.on_prefix(('规则'))
async def rule(bot, ev: CQEvent):   
    text = '''====天况代码一览表====
晴 100 晴一时云 101
晴一时雨 102 晴时雨 103
晴时雷雨 104

密云 200 云一时晴 201
云一时雨 202 云时雨 203
云时雷雨 240 阴 255

雨 300 雨时晴 301
雨时云 302 雷雨 350

大雨 500 大雷雨 550
暴风雨 700 暴风雷雨 750

======其他指令======
发送[手动更新]手动命令更新预报
发送[手动修改]获取json
发送[保存修改+json]保存修改后的json
    '''
    msg = f'{text}'
    await bot.send(ev, msg)

@sv.on_prefix(('保存修改'))
async def weatherS(bot, ev: CQEvent):
    text = str(ev.message).strip()
    strinfo = re.compile('&#91;')
    text2 = strinfo.sub('[',text)
    strinfo2 = re.compile('&#93;')
    text3 = strinfo2.sub(']',text2)
    #sv.logger.info(text3)
    with open('C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/data.json','w', encoding="utf-8") as f_write:
        f_write.write(text3)
    
    with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/data.json", "r") as read_file:
        text4 = json.load(read_file)
    text4 = text4["data"]
    day1_list = text4[0]
    day2_list = text4[1]
    day1_weather = day1_list['weatherImg']
    day1_TempMax = day1_list['MaxT']
    day1_TempMin = day1_list['MinT']
    prob_day1 = day1_list['prob']
    prob_day2 = day2_list['prob']
    prob_day1_1 = str(prob_day1[0])
    prob_day1_2 = str(prob_day1[1])
    prob_day1_3 = str(prob_day1[2])
    prob_day1_4 = str(prob_day1[3])
    prob_day2_1 = str(prob_day2[0])
    prob_day2_2 = str(prob_day2[1])
    prob_day2_3 = str(prob_day2[2])
    prob_day2_4 = str(prob_day2[3])
    
    day2_weather = day2_list['weatherImg']
    day2_TempMax = day2_list['MaxT']
    day2_TempMin = day2_list['MinT']    
        
    str_w = str(day1_TempMax) + ',' + str(day1_TempMin) + ',' + str(day1_weather) + ',' + prob_day1_1 + ',' + prob_day1_2 + ',' + prob_day1_3 + ',' + prob_day1_4 + ','+ prob_day2_1 + ',' + prob_day2_2 + ',' + prob_day2_3 + ',' + prob_day2_4 
    
    with open('C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/day2.txt','w', encoding="utf-8") as f_write:
        f_write.write(str_w)
    msg = f'更新成功'
    await bot.send(ev, msg)
    