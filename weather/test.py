#数据爬取和处理
import pandas as pd
from lxml import html
import requests
from texttable import Texttable
import openpyxl


etree=html.etree
url='https://meteologix.com/cn/weather/7001342-xinqu/'
r=requests.get(url=url)
r.encoding='utf-8'
page_text=r.text
#抓取到目标页面html的text内容
tree=etree.HTML(page_text)
print(r.text)