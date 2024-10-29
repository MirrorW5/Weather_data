
#数据爬取和处理
import pandas as pd
from lxml import html
import requests
from texttable import Texttable
import openpyxl
#信息推送
#...

etree=html.etree
#进行UA伪装
headers = {
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'
}
url='https://meteologix.com/cn/weather/7001342-xinqu/'
r = requests.get(url=url, headers=headers)
print("打印状态码:",r.status_code)
r.encoding='utf-8'
page_text=r.text
#抓取到目标页面html的text内容
print(page_text)
tree=etree.HTML(page_text)
#抓取forecast下并列的天气数据
#
#//*[@id="weather-overview-nexthoursdays"]/div[4]/div[1]/div
#//*[@id="weather-overview-nexthoursdays"]/div[4]/div[1]
#//*[@id="weather-overview-nexthoursdays"]/div[4]
#//*[@id="weather-overview-nexthoursdays"]
#li_list=tree.xpath('//*[@id="weather-overview-nexthoursdays"]')
li_list=tree.xpath('//*[@id="weather-overview-nexthoursdays"]/div[4]/div[1]/div/div[2]/div[4]/div[1]')

#创建空列表，后续存取对应天气信息

# morninglist=[]
# noonlist=[]
# nightlist=[]
# risklist=[]#风险天气

datelist=[10]
maxtemperature=[]
mintemperature=[]
sustainedwind=[7]#持续风
gustwind=[6]#阵风
precipitation=[5]#降水量


#抓取每一天天气预报栏目下的信息，并将换行符去掉，存入事先创建好的列表
for li in li_list:
    #获取图片
    #//*[@id="weather-overview-nexthoursdays"]/div[4]/div[1]/div/div[2]/div[1]/img
    # morninglist.append(li.xpath('//*[@id="weather-overview-nexthoursdays"]/div[4]/div[1]/div/div[2]/div[1]/img')[0].strip())
    # noonlist.append(li.xpath('//*[@id="weather-overview-nexthoursdays"]/div[4]/div[1]/div/div[2]/div[2]/img')[0].strip())
    # nightlist.append(li.xpath('//*[@id="weather-overview-nexthoursdays"]/div[4]/div[1]/div/div[2]/div[3]/img')[0].strip())
    # risklist.append(li.xpath('//*[@id="weather-overview-nexthoursdays"]/div[4]/div[1]/div/div[2]/div[5]/div[1]/div[2]/img')[0])

    #获取数值
    #//*[@id="weather-overview-nexthoursdays"]/div[4]/div[1]/div/div[1]/text()[2]
    #datelist.append(li.xpath('./div[4]/div[1]/div/div[1]/text()[2]'))
    maxtemperature.append(li.xpath('./div[1].text()'))
    mintemperature.append(li.xpath('./div[2].text()'))
    # sustainedwind.append(li.xpath('./div[4]/div[1]/div/div[2]/div[5]/div[2]/div[1]/text()'))
    # gustwind.append(li.xpath('./div[4]/div[1]/div/div[2]/div[5]/div[2]/div[2]/text()'))
    # precipitation.append(li.xpath('./div[4]/div[1]/div/div[2]/div[5]/div[2]/div[3]/text()'))

pd.set_option('display.max_rows',None)
data=pd.DataFrame({

    "Max":maxtemperature,
    "Min":mintemperature

})
#将DataFrame内爬取到的天气数据写入csv文件
#...
data.to_excel("prediction.xlsx",index=None,sheet_name="明天天气预报",engine='openpyxl')
#为DataFrame画表
tb = Texttable()
#各列分别设置为居中对齐
#tb.set_cols_align(['c','c','c','c','c','c'])
tb.set_cols_align(['c','c'])
#将每列的数据类型转换为't'一文本,'a'——自动匹配最适文本
#tb.set_cols_dtype(['a','a','a','a','a','a'])
tb.set_cols_dtype(['a','a'])
# tb.header(['Date','Max','Min','Sustained','Gust','Precipitation'])
tb.header(['Max','Min'])
#此处的False表示不将第一参数的第一行作为标题
tb.add_rows(data.values, header=False)
#输出栏显示未来天气
print(tb.draw())