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

sv = Service('autoRenew2daysWave', help_='''
自动预报2daysWave
'''.strip())

@sv.scheduled_job('cron', hour='00', minute='00',second='35')
async def autoRenew2daysWave():
    def get_ua():
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
        ]
        user_agent = random.choice(user_agents)  # 随机抽取对象
        return user_agent


    ua = get_ua()
    headers = {
        'User-Agent': ua,
    }
    data ={
        "code":"325"
    }
    try:
        url = 'https://www.oceanguide.org.cn/hyyj2/fisheryport/meshingAging'
        getdata = requests.post(url=url, headers=headers,data = data)
        wave_data_info = getdata.text
        wave_data_json = json.loads(wave_data_info)
        wave_data_json = wave_data_json["obj"]
        updateDate = ''
        maxWaveList=[]
        minWaveList=[]

        for data in wave_data_json:
            maxWaveList.append(data['maxWaveHeight'])
            minWaveList.append(data['minWaveHeight'])
        wave_str = ''
        
        for i in range(0,int(len(minWaveList))):
            if float(minWaveList[i]) - 0.7 > 0:
                minWaveList[i] = str(float(minWaveList[i]) - 0.7)
            wave_str = wave_str + str(round(float(minWaveList[i]),1)) + ','
        for i in range(0,int(len(maxWaveList))):
            if float(maxWaveList[i]) - 0.7 > 0 and float(maxWaveList[i]) - 0.7 > float(minWaveList[i]):
                maxWaveList[i] = str(float(maxWaveList[i]) - 0.7)
            wave_str = wave_str + str(round(float(maxWaveList[i]),1))
            if i != int(len(minWaveList)) - 1:
                wave_str = wave_str+','

        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/waveTemp.txt", 'w',
                  encoding="utf-8") as f:
            f.write(wave_str)
    except Exception as e:
        bot = nonebot.get_bot()
        await bot.send_private_msg(user_id=2864309367, message=f'【报错信息】浪高出错\n原因:{e}')        
        sv.logger.info('============浪高出错============')    
        
        