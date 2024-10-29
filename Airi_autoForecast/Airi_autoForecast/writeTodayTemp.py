import re
import ssl
from hoshino import Service, priv
from hoshino.typing import CQEvent
from hoshino import R
ssl._create_default_https_context = ssl._create_unverified_context
from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Resampling
import datetime
import locale
import requests
import json
import time

sv = Service('writeTodayTemp', help_='''
自动写入
'''.strip())
    
@sv.scheduled_job('cron', hour='00', minute='00',second='00')
async def writeTodayTemp():
    data = ''
    data1_list = []
    data2_list = []
    with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/day2.txt", "r", encoding="utf-8") as f:
        data1 = f.read()
        data1_list = data1.split(',')
    with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/day2_temp.txt", "r", encoding="utf-8") as f:
        data2 = f.read()
        data2_list = data2.split(',')
    for i in data2_list:
        data = data + i + ','
    for j in range(3,int(len(data1_list))):
        data = data + data1_list[j]
        if j != int(len(data1_list)) - 1:
            data = data + ','
    
    with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/day2.txt", 'w', encoding="utf-8") as f:
        f.write(data)    