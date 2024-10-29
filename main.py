# This is a sample Python script.
#弹出"Run context configuration' is not available during indexin"，应该是在下载东西，没法运行
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#数据爬取和处理
import pandas as pd
from lxml import html
import requests
from texttable import Texttable
import openpyxl
#信息推送
#...

etree=html.etree
url='http://tianqi.2345.com/'
r=requests.get(url=url)
r.encoding='utf-8'
page_text=r.text
#抓取到目标页面html的text内容
tree=etree.HTML(page_text)
#抓取天气栏目下并列的天气数据
li_list=tree.xpath('//div[@id="J_bannerList"]/div')
#创建空列表，后续存取对应天气信息
datelist=[]
weeklist=[]
temperature=[]
weather=[]
#抓取每一天天气预报栏目下的信息，并将换行符去掉，存入事先创建好的列表
for li in li_list:
    weeklist.append(li.xpath('./div[1]/text()')[0].strip())
    datelist.append(li.xpath('./div[2]/text()')[0].strip())
    weather.append(li.xpath('./div[4]/text()')[0])
    temperature.append(li.xpath('./div[5]/text()')[0])

pd.set_option('display.max_rows',None)
data=pd.DataFrame({
    "Date":datelist,
    "Week":weeklist,
    "Temperature":temperature,
    "Weather":weather
})
#将DataFrame内爬取到的天气数据写入csv文件
#...
data.to_excel("prediction.xlsx",index=None,sheet_name="近八天天气预报",engine='openpyxl')
#为DataFrame画表
tb = Texttable()
#各列分别设置为居中对齐
tb.set_cols_align(['c','c','c','c'])
#将每列的数据类型转换为't'一文本
tb.set_cols_dtype(['t','t','t','t'])
tb.header(['Date','Week','Temperature','Weather'])
#此处的False表示不将第一参数的第一行作为标题
tb.add_rows(data.values, header=False)
#输出栏显示未来天气
print(tb.draw())