import ssl
from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Resampling
from datetime import datetime
from datetime import timedelta
import locale
import json
from hoshino import Service, priv
from hoshino.typing import CQEvent
from hoshino import R
ssl._create_default_https_context = ssl._create_unverified_context
from hoshino.service import Service

sv = Service('drawPicture', bundle='画图', help_='''
画图
'''.strip())

@sv.on_prefix(('深圳天气','自动预报'))
async def drawPicture(bot, ev: CQEvent):
    flag_draw = 1
    time_h = int(datetime.now().strftime('%H'))
    time_m = int(datetime.now().strftime('%M'))
    time_s = int(datetime.now().strftime('%S'))
    if time_h == 0 and time_m == 0 and time_s < 50:
        flag_draw = 0
    
    if flag_draw == 0:
        msg = f'00:00:00-00:00:50为维护时间，请稍后再试'
        await bot.send(ev, msg)
    else:
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/data.json", "r") as read_file:
            text = json.load(read_file)
        text = text["data"]
        day1_list = text[0]
        day2_list = text[1]
        day1_weather = day1_list['weatherImg']
        day1_TempMax = day1_list['MaxT']
        day1_TempMin = day1_list['MinT']
        prob_day1 = day1_list['prob']
        prob_day2 = day2_list['prob']
        prob_day1_1 = prob_day1[0] + '%'
        prob_day1_2 = prob_day1[1] + '%'
        prob_day1_3 = prob_day1[2] + '%'
        prob_day1_4 = prob_day1[3] + '%'
        prob_day2_1 = prob_day2[0] + '%'
        prob_day2_2 = prob_day2[1] + '%'
        prob_day2_3 = prob_day2[2] + '%'
        prob_day2_4 = prob_day2[3] + '%'
        
        
        day2_weather = day2_list['weatherImg']
        day2_TempMax = day2_list['MaxT']
        day2_TempMin = day2_list['MinT']
        day3_list = text[2]
        day3_weather = day3_list['weatherImg']
        day3_TempMax = day3_list['MaxT']
        day3_TempMin = day3_list['MinT']
        prob_day3 = day3_list['prob']
        day4_list = text[3]
        day4_weather = day4_list['weatherImg']
        day4_TempMax = day4_list['MaxT']
        day4_TempMin = day4_list['MinT']
        prob_day4 = day4_list['prob']
        day5_list = text[4]
        day5_weather = day5_list['weatherImg']
        day5_TempMax = day5_list['MaxT']
        day5_TempMin = day5_list['MinT']
        prob_day5 = day5_list['prob']
        day6_list = text[5]
        day6_weather = day6_list['weatherImg']
        day6_TempMax = day6_list['MaxT']
        day6_TempMin = day6_list['MinT']
        prob_day6 = day6_list['prob']
        day7_list = text[6]
        day7_weather = day7_list['weatherImg']
        day7_TempMax = day7_list['MaxT']
        day7_TempMin = day7_list['MinT']
        prob_day7 = day7_list['prob']
        day8_list = text[7]
        day8_weather = day8_list['weatherImg']
        day8_TempMax = day8_list['MaxT']
        day8_TempMin = day8_list['MinT']
        prob_day8 = day8_list['prob']
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/renewTime.txt", "r",encoding="utf-8") as f:
            data_date = f.read()

        def weatherPicText(tag):
            str = ''
            if tag == '100':
                str = '晴'
            elif tag == '101':
                str = '晴一时云'
            elif tag == '102':
                str = '晴一时雨'
            elif tag == '103':
                str = '晴时雨'
            elif tag == '140':
                str = '晴时雷雨'
            elif tag == '200':
                str = '密云'
            elif tag == '201':
                str = '云一时晴'
            elif tag == '202':
                str = '云一时雨'
            elif tag == '203':
                str = '云时雨'
            elif tag == '240':
                str = '云时雷雨'
            elif tag == '255':
                str = '阴'
            elif tag == '300':
                str = '雨'
            elif tag == '301':
                str = '雨时晴'
            elif tag == '302':
                str = '雨时云'
            elif tag == '350':
                str = '雷雨'
            elif tag == '500':
                str = '大雨'
            elif tag == '550':
                str = '大雨'
            elif tag == '700':
                str = '暴风雨'
            elif tag == '750':
                str = '暴风雨'
            return str

        #---------------------------以下为固定部分--------------------------------------
        deta_h = 175
        yellowType = []
        redType = []
        purpleType = []
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoWarning/save.txt", 'r',
                  encoding="utf-8") as f_warn:
            data_warn = f_warn.read()
        data_save_list = data_warn
        if data_save_list[0] == '1':
            yellowType.append("冰雹")

        if data_save_list[1] == '1':
            yellowType.append('雷')

        if data_save_list[2] == '1':
            yellowType.append('大雨')
        elif data_save_list[2] == '2':
            redType.append('大雨')
        elif data_save_list[2] == '3':
            purpleType.append('大雨')

        if data_save_list[3] == '1':
            redType.append('土砂灾害')
        elif data_save_list[3] == '2':
            purpleType.append('土砂灾害')

        if data_save_list[4] == '1':
            yellowType.append('强风')
        elif data_save_list[4] == '2':
            redType.append('暴风')
        elif data_save_list[4] == '3':
            purpleType.append('暴风')

        if data_save_list[5] == '1':
            yellowType.append('干燥')

        if data_save_list[6] == '1':
            yellowType.append('波浪')
        elif data_save_list[6] == '2':
            redType.append('波浪')

        if data_save_list[7] == '1':
            yellowType.append('高温')
        elif data_save_list[7] == '2':
            yellowType.append('低温')
        elif data_save_list[7] == '3':
            yellowType.append('霜冻')

        if data_save_list[8] == '1':
            yellowType.append('高潮')
        elif data_save_list[8] == '2':
            redType.append('高潮')

        if data_save_list[9] == '1':
            yellowType.append('浓雾')

        flagy = flagr = flagp = 0
        if int(len(yellowType)) > 0:
            flagy = 1
        if int(len(redType)) > 0:
            flagr = 1
        if int(len(purpleType)) > 0:
            flagp = 1

        if flagy+flagr+flagp == 2:
            deta_h = deta_h + 50
        elif flagy+flagr+flagp == 3:
            deta_h = deta_h + 100
        img_background = Image.new('RGB', (1150, 760+deta_h), '#FFFFFF')
        img = ImageDraw.Draw(img_background)
        draw = ImageDraw.Draw(img_background)

        def addx(strW):
            if int(len(strW)) == 3:
                return 10
            elif int(len(strW)) == 2:
                return 18
            elif int(len(strW)) == 4:
                return 2

        draw.rectangle((20,360,1100,290+deta_h),outline ='#ABBACD',width =1)
        setFontJB = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 20)
        date_title = "深圳地区警报·注意报"
        draw.text((40, 378), date_title, font=setFontJB, fill="#05c", direction=None)

        def printstr(list):
            fellow = ''
            for i in range(0, int(len(list))):
                fellow = fellow + list[i]
                if i != int(len(list)) - 1:
                    fellow = fellow + '、'
            return fellow


        if flagy + flagr + flagp == 0:
            setFontNone = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
            date_title = "无警报发布"
            draw.text((55, 420), date_title, font=setFontNone, fill="#000000", direction=None)
        else:
            if flagy + flagr + flagp == 1:
                if flagy == 1:
                    color = '#ffd400'
                    textw = '注意报'
                    textc = '#000000'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 424), printstr(yellowType), font=setFontfellow, fill="#000000", direction=None)
                elif flagr == 1:
                    color = 'red'
                    textw = '警报'
                    textc = '#ffffff'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 424), printstr(redType), font=setFontfellow, fill="#000000", direction=None)
                elif flagp == 1:
                    color = '#7f0085'
                    textw = '特别警报'
                    textc = '#ffffff'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 424), printstr(purpleType), font=setFontfellow, fill="#000000", direction=None)
                draw.rectangle((40,420,140,450), fill=color,outline='white', width=0)
                setFontW = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                draw.text((55+addx(textw), 424), textw, font=setFontW, fill=textc, direction=None)

            elif flagy + flagr + flagp == 2:
                if flagy == flagr and flagy == 1:
                    color2 = '#ffd400'
                    color1 = 'red'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 474), printstr(yellowType), font=setFontfellow, fill="#000000", direction=None)
                    draw.text((155, 424), printstr(redType), font=setFontfellow, fill="#000000", direction=None)
                    text1 = '注意报'
                    text2 = '警报'
                    fill1 = '#000000'
                    fill2 = '#ffffff'
                elif flagy == flagp and flagy == 1:
                    color2 = '#ffd400'
                    color1 = '#7f0085'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 474), printstr(yellowType), font=setFontfellow, fill="#000000", direction=None)
                    draw.text((155, 424), printstr(purpleType), font=setFontfellow, fill="#000000", direction=None)
                    text2 = '特别警报'
                    text1 = '注意报'
                    fill1 = '#000000'
                    fill2 = '#ffffff'
                elif flagr == flagp and flagr == 1:
                    color2 = 'red'
                    color1 = '#7f0085'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 474), printstr(redType), font=setFontfellow, fill="#000000", direction=None)
                    draw.text((155, 424), printstr(purpleType), font=setFontfellow, fill="#000000", direction=None)
                    text2 = '特别警报'
                    text1 = '警报'
                    fill1 = '#ffffff'
                    fill2 = '#ffffff'
                draw.rectangle((40,420,140,450), fill=color1, outline='white', width=0)
                draw.rectangle((40,470,140,500), fill=color2, outline='white', width=0)
                draw.text((55 + addx(text1), 474), text1, font=setFontfellow, fill=fill1, direction=None)
                draw.text((55 + addx(text2), 424), text2, font=setFontfellow, fill=fill2, direction=None)
            elif flagy + flagr + flagp == 3:
                setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                draw.rectangle((40,420,140,450), fill='#7f0085', outline='white', width=0)
                draw.text((55 + addx('特别警报'), 424), '特别警报', font=setFontfellow, fill='#ffffff', direction=None)
                draw.text((155, 424), printstr(purpleType), font=setFontfellow, fill="#000000", direction=None)
                draw.rectangle((40, 470, 140, 500), fill='red', outline='white', width=0)
                draw.text((55 + addx('警报'), 474), '警报', font=setFontfellow, fill='#ffffff', direction=None)
                draw.text((155, 474), printstr(redType), font=setFontfellow, fill="#000000", direction=None)
                draw.rectangle((40, 520, 140, 550), fill='#ffd400', outline='white', width=0)
                draw.text((55 + addx('注意报'), 524), '注意报', font=setFontfellow, fill='#000000', direction=None)
                draw.text((155, 524), printstr(yellowType), font=setFontfellow, fill="#000000", direction=None)


        draw.rectangle((20,19,1100,20),fill ='#ABBACD',outline ='white',width =0)
        draw.rectangle((20,20,1100,60),fill ='#E5EEF7',outline ='white',width =0)
        draw.rectangle((20,309+deta_h,1100,310+deta_h),fill ='#ABBACD',outline ='white',width =0)
        draw.rectangle((20,310+deta_h,1100,350+deta_h),fill ='#E5EEF7',outline ='white',width =0)

        draw.rectangle((134,360+deta_h,1100,450+deta_h),fill ='#e9eefd',width =0)
        draw.rectangle((20,360+deta_h,134,720+deta_h),fill ='#eeeeee',width =0)
        draw.rectangle((20,70,1100,290+50),outline ='#ABBACD',width =1)
        draw.line((560,70,560,290+50), fill='#ABBACD', width=1)
        draw.rectangle((20,360+deta_h,1100,720+deta_h),outline ='#ABBACD',width =1)
        draw.line((20,450+deta_h,1100,450+deta_h), fill='#ABBACD', width=1)
        draw.line((20,540+deta_h,1100,540+deta_h), fill='#ABBACD', width=1)
        draw.line((20,630+deta_h,1100,630+deta_h), fill='#ABBACD', width=1)

        #e9eefd
        draw.line((134,360+deta_h,134,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*1,360+deta_h,134+161*1,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*2,360+deta_h,134+161*2,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*3,360+deta_h,134+161*3,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*4,360+deta_h,134+161*4,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*5,360+deta_h,134+161*5,720+deta_h), fill='#ABBACD', width=1)

        setFont10 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 20)
        date_title = "日期"
        draw.text((55, 391+deta_h), date_title, font=setFont10, fill="#000000", direction=None)
        weather_title = "天气"
        draw.text((55, 481+deta_h), weather_title, font=setFont10, fill="#000000", direction=None)
        temp_title = "气温(℃)"
        draw.text((41, 571+deta_h), temp_title, font=setFont10, fill="#000000", direction=None)
        rainpro_title = "降雨概率"
        draw.text((37, 645+deta_h), rainpro_title, font=setFont10, fill="#000000", direction=None)
        rainpro_title2 = "(%)"
        draw.text((60, 675+deta_h), rainpro_title2, font=setFont10, fill="#000000", direction=None)


        setFont1 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 20)
        textTitle = "深圳今日明日的天气"
        draw.text((30, 25), textTitle, font=setFont1, fill="#000000", direction=None)
        textRenewTime = data_date
        draw.text((845, 30), textRenewTime, font=ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17), fill="#000000", direction=None)
        textTitle = "一周天气"
        draw.text((30, 315+deta_h), textTitle, font=setFont1, fill="#000000", direction=None)

        draw.rectangle((40,200,540,235),fill='#f2f4fa')
        draw.rectangle((40,200,540,270),outline ='#ABBACD',width =1)
        draw.line((40,235,540,235), fill='#ABBACD', width=1)
        draw.line((140,200,140,270), fill='#ABBACD', width=1)

        draw.rectangle((580,200,1080,235),fill='#f2f4fa')
        draw.rectangle((580,200,1080,270),outline ='#ABBACD',width =1)
        draw.line((580,235,1080,235), fill='#ABBACD', width=1)
        draw.line((680,200,680,270), fill='#ABBACD', width=1)

        draw.line((240,200,240,270), fill='#ABBACD', width=1)
        draw.line((340,200,340,270), fill='#ABBACD', width=1)
        draw.line((440,200,440,270), fill='#ABBACD', width=1)

        draw.line((240+540,200,240+540,270), fill='#ABBACD', width=1)
        draw.line((340+540,200,340+540,270), fill='#ABBACD', width=1)
        draw.line((440+540,200,440+540,270), fill='#ABBACD', width=1)

        def addx(str):
            if str == '---':
                add = 20
            else:
                if len(str) == 2:
                    add = 20
                elif len(str) == 3:
                    add = 15
                elif len(str) == 4:
                    add = 9
            return add

        def addx2(str):
            if len(str) == 2:
                add = 16
            elif len(str) == 3:
                add = 14
            elif len(str) == 4:
                add = 8
            return add

        def addx3(str):
            if len(str) == 4:
                add = 26
            elif len(str) == 5:
                add = 20
            elif len(str) == 6:
                add = 14
            return add

        def addx4(str):
            if len(str) == 1:
                add = 30
            elif len(str) == 2:
                add = 20
            elif len(str) == 3:
                add = 10
            elif len(str) == 4:
                add = 0
            return add

        def addx5(str):
            if len(str) == 1:
                add = 33
            elif len(str) == 2:
                add = 25
            elif len(str) == 3:
                add = 18
            elif len(str) == 4:
                add = 10
            return add

        def addx6(str):
            if len(str) == 1:
                add = 28
            elif len(str) == 2:
                add = 21
            return add

        def addx7(str):
            if len(str) == 1:
                add = 37
            elif len(str) == 2:
                add = 31
            elif len(str) == 3:
                add = 25
            return add

        setFont4 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
        weather_time_title = "时间"
        draw.text((73, 207), weather_time_title, font=setFont4, fill="#000000", direction=None)
        weather_time_title = "时间"
        draw.text((613, 207), weather_time_title, font=setFont4, fill="#000000", direction=None)
        weather_pro_title = "降水"
        draw.text((73, 241), weather_pro_title, font=setFont4, fill="#000000", direction=None)
        weather_pro_title = "降水"
        draw.text((613, 241), weather_pro_title, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "0-6"
        draw.text((178, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "6-12"
        draw.text((273, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "12-18"
        draw.text((366, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "18-24"
        draw.text((466, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "0-6"
        draw.text((178+540, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "6-12"
        draw.text((273+540, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "12-18"
        draw.text((366+540, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "18-24"
        draw.text((466+540, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)

        #---------------------------以上为固定部分--------------------------------------


        now_time_hour = datetime.now()
        Today = now_time_hour.strftime('%H')
        dateHour = int(Today)
        data_wave = ''
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/waveTemp.txt", "r", encoding="utf-8") as f_wave:
            data_wave = f_wave.read()
        data_wave_list = data_wave.split(',')
        
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/wind.txt", "r", encoding="utf-8") as f_wind:
            data_wind = f_wind.read()
        data_wind_list = data_wind.split(',')
        
        def judgewind(wd,maxWs,minWs):
            wind_str = ''
            if float(minWs) > float(maxWs):
                temp = maxWs
                maxWs = minWs
                minWs = temp
            if maxWs == minWs:
                wind_str = wd+'风 '+minWs+' 级'
            else:
                wind_str = wd+'风 '+minWs+' - '+maxWs+' 级'
            return wind_str
        
        if deta_h != 0:
            
            day1_wind = judgewind(data_wind_list[0],data_wind_list[1],data_wind_list[2])
            day2_wind = judgewind(data_wind_list[3],data_wind_list[4],data_wind_list[5])
            day1_wave = data_wave_list[0]+' - '+data_wave_list[3]+' 米'
            day2_wave = data_wave_list[1]+' - '+data_wave_list[4]+' 米'
            
            
            draw.text((40, 280), '风：'+day1_wind, font=setFont4, fill="#000000", direction=None)
            draw.text((40+540, 280), '风：'+day2_wind, font=setFont4, fill="#000000", direction=None)
            draw.text((40, 310), '浪：'+day1_wave, font=setFont4, fill="#000000", direction=None)
            draw.text((40+540, 310), '浪：'+day2_wave, font=setFont4, fill="#000000", direction=None)
            
        if dateHour >= 6 :
            prob_day1_1 = '---'
        if dateHour >= 12:
            prob_day1_2 = '---'
        if dateHour >= 18:
            prob_day1_3 = '---'

        draw.text((160+addx(prob_day1_1), 241), prob_day1_1, font=setFont4, fill="#000000", direction=None)
        draw.text((260+addx(prob_day1_2), 241), prob_day1_2, font=setFont4, fill="#000000", direction=None)
        draw.text((360+addx(prob_day1_3), 241), prob_day1_3, font=setFont4, fill="#000000", direction=None)
        draw.text((460+addx(prob_day1_4), 241), prob_day1_4, font=setFont4, fill="#000000", direction=None)

        draw.text((160+addx(prob_day2_1)+540, 241), prob_day2_1, font=setFont4, fill="#000000", direction=None)
        draw.text((260+addx(prob_day2_2)+540, 241), prob_day2_2, font=setFont4, fill="#000000", direction=None)
        draw.text((360+addx(prob_day2_3)+540, 241), prob_day2_3, font=setFont4, fill="#000000", direction=None)
        draw.text((460+addx(prob_day2_4)+540, 241), prob_day2_4, font=setFont4, fill="#000000", direction=None)

        setFontProb = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 21)
        draw.text((170+addx7(prob_day3), 658+deta_h), prob_day3, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day4)+161*1, 658+deta_h), prob_day4, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day5)+161*2, 658+deta_h), prob_day5, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day6)+161*3, 658+deta_h), prob_day6, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day7)+161*4, 658+deta_h), prob_day7, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day8)+161*5, 658+deta_h), prob_day8, font=setFontProb, fill="#000000", direction=None)


        setFont3 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 22)
        weather_text1 = weatherPicText(day1_weather)
        draw.text((180+addx4(weather_text1), 130), weather_text1, font=setFont3, fill="#000000", direction=None)
        weather_text2 = weatherPicText(day2_weather)
        draw.text((720+addx4(weather_text2), 130), weather_text2, font=setFont3, fill="#000000", direction=None)
        setFont11 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 16)
        weather_text3 = weatherPicText(day3_weather)
        draw.text((170+addx5(weather_text3)+161*0, 510+deta_h), weather_text3, font=setFont11, fill="#000000", direction=None)
        weather_text4 = weatherPicText(day4_weather)
        draw.text((170+addx5(weather_text4)+161*1, 510+deta_h), weather_text4, font=setFont11, fill="#000000", direction=None)
        weather_text5 = weatherPicText(day5_weather)
        draw.text((170+addx5(weather_text5)+161*2, 510+deta_h), weather_text5, font=setFont11, fill="#000000", direction=None)
        weather_text6 = weatherPicText(day6_weather)
        draw.text((170+addx5(weather_text6)+161*3, 510+deta_h), weather_text6, font=setFont11, fill="#000000", direction=None)
        weather_text7 = weatherPicText(day7_weather)
        draw.text((170+addx5(weather_text7)+161*4, 510+deta_h), weather_text7, font=setFont11, fill="#000000", direction=None)
        weather_text8 = weatherPicText(day8_weather)
        draw.text((170+addx5(weather_text8)+161*5, 510+deta_h), weather_text8, font=setFont11, fill="#000000", direction=None)

        
        def changeTemp(day0_maxT,TempMax):
            a = TempMax - day0_maxT
            str1 = ''
            if a > 0:
                str1 = "[+" + str(a) + "]"
            elif a == 0:
                str1 = "[+0]"
            elif a < 0:
                str1 = "[" + str(a) + "]"
            return str1

        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/day0.json", "r") as read_file2:
            text2 = json.load(read_file2)

        day0_maxT = text2['Temp_max']
        day0_minT = text2['Temp_min']
        day0_maxT = round(day0_maxT)
        day0_minT = round(day0_minT)

        setFontTemp = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 21)
        setFontTempChange = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
        weather_TempMax1 = str(day1_TempMax)
        draw.text((282, 133), weather_TempMax1 + "℃" , font=setFontTemp, fill="#FF0000", direction=None)
        MaxTempChange1 = changeTemp(day0_maxT,day1_TempMax)
        draw.text((332, 136), MaxTempChange1 , font=setFontTempChange, fill="#FF0000", direction=None)

        weather_TempMin1 = str(day1_TempMin)
        draw.text((378, 133), weather_TempMin1 + "℃", font=setFontTemp, fill="#0000FF", direction=None)
        MinTempChange1 = changeTemp(day0_minT,day1_TempMin)
        draw.text((428, 136), MinTempChange1 , font=setFontTempChange, fill="#0000FF", direction=None)

        weather_TempMax2 = str(day2_TempMax)
        draw.text((822, 133), weather_TempMax2 + "℃", font=setFontTemp, fill="#FF0000", direction=None)
        MaxTempChange2 = changeTemp(day0_maxT,day2_TempMax)
        draw.text((872, 136), MaxTempChange2 , font=setFontTempChange, fill="#FF0000", direction=None)

        weather_TempMin2 = str(day2_TempMin)
        draw.text((918, 133), weather_TempMin2 + "℃", font=setFontTemp, fill="#0000FF", direction=None)
        MinTempChange2 = changeTemp(day0_minT,day2_TempMin)
        draw.text((968, 136), MinTempChange2 , font=setFontTempChange, fill="#0000FF", direction=None)

        setFontTemp2 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 20)
        weather_TempMax3 = str(day3_TempMax)
        draw.text((180+addx6(weather_TempMax3), 555+deta_h), weather_TempMax3, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin3 = str(day3_TempMin)
        draw.text((180+addx6(weather_TempMin3), 585+deta_h), weather_TempMin3, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax4 = str(day4_TempMax)
        draw.text((180+addx6(weather_TempMax4) + 161*1, 555+deta_h), weather_TempMax4, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin4 = str(day4_TempMin)
        draw.text((180+addx6(weather_TempMin4) + 161*1, 585+deta_h), weather_TempMin4, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax5 = str(day5_TempMax)
        draw.text((180+addx6(weather_TempMax5) + 161*2, 555+deta_h), weather_TempMax5, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin5 = str(day5_TempMin)
        draw.text((180+addx6(weather_TempMin5) + 161*2, 585+deta_h), weather_TempMin5, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax6 = str(day6_TempMax)
        draw.text((180+addx6(weather_TempMax6) + 161*3, 555+deta_h), weather_TempMax6, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin6 = str(day6_TempMin)
        draw.text((180+addx6(weather_TempMin6) + 161*3, 585+deta_h), weather_TempMin6, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax7 = str(day7_TempMax)
        draw.text((180+addx6(weather_TempMax7) + 161*4, 555+deta_h), weather_TempMax7, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin7 = str(day7_TempMin)
        draw.text((180+addx6(weather_TempMin7) + 161*4, 585+deta_h), weather_TempMin7, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax8 = str(day8_TempMax)
        draw.text((180+addx6(weather_TempMax8) + 161*5, 555+deta_h), weather_TempMax8, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin8 = str(day8_TempMin)
        draw.text((180+addx6(weather_TempMin8) + 161*5, 585+deta_h), weather_TempMin8, font=setFontTemp2, fill="#0000FF", direction=None)


        week_list = ["一","二","三","四","五","六","日"]
        locale.setlocale(locale.LC_CTYPE, 'chinese')
        setFont2 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 16)
        now_time = datetime.now()
        day = now_time.strftime('%m月%d日')
        date1 = day
        week1 = now_time.weekday()
        draw.text((114, 80), "("+week_list[week1]+")", font=setFont2, fill="#000000", direction=None)
        draw.text((40, 80), date1, font=setFont2, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=1)
        day = now_time.strftime('%m月%d日')
        date2 = day
        week2 = now_time.weekday()
        draw.text((654, 80), "("+week_list[week2]+")", font=setFont2, fill="#000000", direction=None)
        draw.text((580, 80), date2, font=setFont2, fill="#000000", direction=None)

        now_time = datetime.now() + timedelta(days=2)
        day = now_time.strftime('%m月%d日')
        date3 = day
        week3 = now_time.weekday()
        draw.text((196, 406+deta_h), "("+week_list[week3]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date3), 378+deta_h), date3, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=3)
        day = now_time.strftime('%m月%d日')
        date4 = day
        week4 = now_time.weekday()
        draw.text((196+161*1, 406+deta_h), "("+week_list[week4]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date4)+161*1, 378+deta_h), date4, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=4)
        day = now_time.strftime('%m月%d日')
        date5 = day
        week5 = now_time.weekday()
        draw.text((196+161*2, 406+deta_h), "("+week_list[week5]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date5)+161*2, 378+deta_h), date5, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=5)
        day = now_time.strftime('%m月%d日')
        date6 = day
        week6 = now_time.weekday()
        draw.text((196+161*3, 406+deta_h), "("+week_list[week6]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date6)+161*3, 378+deta_h), date6, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=6)
        day = now_time.strftime('%m月%d日')
        date7 = day
        week7 = now_time.weekday()
        draw.text((196+161*4, 406+deta_h), "("+week_list[week7]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date7)+161*4, 378+deta_h), date7, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=7)
        day = now_time.strftime('%m月%d日')
        date8 = day
        week8 = now_time.weekday()
        draw.text((196+161*5, 406+deta_h), "("+week_list[week8]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date8)+161*5, 378+deta_h), date8, font=setFont10, fill="#000000", direction=None)


        weather_img1 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day1_weather + "_day.png")
        img_background.paste(weather_img1, (21, 110))
        weather_img2 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day2_weather + "_day.png")
        img_background.paste(weather_img2, (561, 110))
        a = 0.6
        weather_img3 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day3_weather + "_day.png")
        weather_img3 = weather_img3.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img3, (167 + 161*0, 460+deta_h))
        weather_img4 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day4_weather + "_day.png")
        weather_img4 = weather_img4.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img4, (167 + 161*1, 460+deta_h))
        weather_img5 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day5_weather + "_day.png")
        weather_img5 = weather_img5.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img5, (167 + 161*2, 460+deta_h))
        weather_img6 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day6_weather + "_day.png")
        weather_img6 = weather_img6.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img6, (167 + 161*3, 460+deta_h))
        weather_img7 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day7_weather + "_day.png")
        weather_img7 = weather_img7.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img7, (167 + 161*4, 460+deta_h))
        weather_img8 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day8_weather + "_day.png")
        weather_img8 = weather_img8.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img8, (167 + 161*5, 460+deta_h))


        img_background.save('C:/Users/Administrator/Desktop/myBot/HoshinoBot/res/img/forecast.png')
        pic1 = R.img("forecast.png").cqcode
        msg = f'{pic1}'
        await bot.send(ev, msg)





@sv.on_prefix(('深圳天气日文','自动预报日文','深圳天气日语','自动预报日语'))
async def drawPictureJapan(bot, ev: CQEvent):
    flag_draw = 1
    time_h = int(datetime.now().strftime('%H'))
    time_m = int(datetime.now().strftime('%M'))
    time_s = int(datetime.now().strftime('%S'))
    if time_h == 0 and time_m == 0 and time_s < 50:
        flag_draw = 0
    
    if flag_draw == 0:
        msg = f'00:00:00-00:00:50为维护时间，请稍后再试'
        await bot.send(ev, msg)
    else:
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/data.json", "r") as read_file:
            text = json.load(read_file)
        text = text["data"]
        day1_list = text[0]
        day2_list = text[1]
        day1_weather = day1_list['weatherImg']
        day1_TempMax = day1_list['MaxT']
        day1_TempMin = day1_list['MinT']
        prob_day1 = day1_list['prob']
        prob_day2 = day2_list['prob']
        prob_day1_1 = prob_day1[0] + '%'
        prob_day1_2 = prob_day1[1] + '%'
        prob_day1_3 = prob_day1[2] + '%'
        prob_day1_4 = prob_day1[3] + '%'
        prob_day2_1 = prob_day2[0] + '%'
        prob_day2_2 = prob_day2[1] + '%'
        prob_day2_3 = prob_day2[2] + '%'
        prob_day2_4 = prob_day2[3] + '%'
        
        
        day2_weather = day2_list['weatherImg']
        day2_TempMax = day2_list['MaxT']
        day2_TempMin = day2_list['MinT']
        day3_list = text[2]
        day3_weather = day3_list['weatherImg']
        day3_TempMax = day3_list['MaxT']
        day3_TempMin = day3_list['MinT']
        prob_day3 = day3_list['prob']
        day4_list = text[3]
        day4_weather = day4_list['weatherImg']
        day4_TempMax = day4_list['MaxT']
        day4_TempMin = day4_list['MinT']
        prob_day4 = day4_list['prob']
        day5_list = text[4]
        day5_weather = day5_list['weatherImg']
        day5_TempMax = day5_list['MaxT']
        day5_TempMin = day5_list['MinT']
        prob_day5 = day5_list['prob']
        day6_list = text[5]
        day6_weather = day6_list['weatherImg']
        day6_TempMax = day6_list['MaxT']
        day6_TempMin = day6_list['MinT']
        prob_day6 = day6_list['prob']
        day7_list = text[6]
        day7_weather = day7_list['weatherImg']
        day7_TempMax = day7_list['MaxT']
        day7_TempMin = day7_list['MinT']
        prob_day7 = day7_list['prob']
        day8_list = text[7]
        day8_weather = day8_list['weatherImg']
        day8_TempMax = day8_list['MaxT']
        day8_TempMin = day8_list['MinT']
        prob_day8 = day8_list['prob']
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/renewTime.txt", "r",encoding="utf-8") as f:
            data_date = f.read()

        def weatherPicText(tag):
            str = ''
            if tag == '100':
                str = '晴れ'
            elif tag == '101':
                str = '晴時々曇'
            elif tag == '102':
                str = '晴一時雨'
            elif tag == '103':
                str = '晴時々雨'
            elif tag == '140':
                str = '晴時々雨'
            elif tag == '200':
                str = '曇り'
            elif tag == '201':
                str = '曇時々晴'
            elif tag == '202':
                str = '曇一時雨'
            elif tag == '203':
                str = '曇時々雨'
            elif tag == '240':
                str = '曇時々雨'
            elif tag == '255':
                str = '曇り'
            elif tag == '300':
                str = '雨'
            elif tag == '301':
                str = '雨時々晴'
            elif tag == '302':
                str = '雨時々曇'
            elif tag == '350':
                str = '雨'
            elif tag == '500':
                str = '大雨'
            elif tag == '550':
                str = '大雨'
            elif tag == '700':
                str = '暴風雨'
            elif tag == '750':
                str = '暴風雨'
            return str

        #---------------------------以下为固定部分--------------------------------------
        deta_h = 175
        yellowType = []
        redType = []
        purpleType = []
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoWarning/save.txt", 'r',
                  encoding="utf-8") as f_warn:
            data_warn = f_warn.read()
        data_save_list = data_warn
        if data_save_list[0] == '1':
            yellowType.append("雹")

        if data_save_list[1] == '1':
            yellowType.append('雷')

        if data_save_list[2] == '1':
            yellowType.append('大雨')
        elif data_save_list[2] == '2':
            redType.append('大雨')
        elif data_save_list[2] == '3':
            purpleType.append('大雨')

        if data_save_list[3] == '1':
            redType.append('土砂災害')
        elif data_save_list[3] == '2':
            purpleType.append('土砂災害')

        if data_save_list[4] == '1':
            yellowType.append('强風')
        elif data_save_list[4] == '2':
            redType.append('暴風')
        elif data_save_list[4] == '3':
            purpleType.append('暴風')

        if data_save_list[5] == '1':
            yellowType.append('干燥')

        if data_save_list[6] == '1':
            yellowType.append('波浪')
        elif data_save_list[6] == '2':
            redType.append('波浪')

        if data_save_list[7] == '1':
            yellowType.append('高温')
        elif data_save_list[7] == '2':
            yellowType.append('低温')
        elif data_save_list[7] == '3':
            yellowType.append('霜')

        if data_save_list[8] == '1':
            yellowType.append('高潮')
        elif data_save_list[8] == '2':
            redType.append('高潮')

        if data_save_list[9] == '1':
            yellowType.append('濃霧')

        flagy = flagr = flagp = 0
        if int(len(yellowType)) > 0:
            flagy = 1
        if int(len(redType)) > 0:
            flagr = 1
        if int(len(purpleType)) > 0:
            flagp = 1

        if flagy+flagr+flagp == 2:
            deta_h = deta_h + 50
        elif flagy+flagr+flagp == 3:
            deta_h = deta_h + 100
        img_background = Image.new('RGB', (1150, 760+deta_h), '#FFFFFF')
        img = ImageDraw.Draw(img_background)
        draw = ImageDraw.Draw(img_background)

        def addx(strW):
            if int(len(strW)) == 3:
                return 10
            elif int(len(strW)) == 2:
                return 18
            elif int(len(strW)) == 4:
                return 2

        draw.rectangle((20,360,1100,290+deta_h),outline ='#ABBACD',width =1)
        setFontJB = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 20)
        date_title = "深セン地方の警報 · 注意報"
        draw.text((40, 378), date_title, font=setFontJB, fill="#05c", direction=None)

        def printstr(list):
            fellow = ''
            for i in range(0, int(len(list))):
                fellow = fellow + list[i]
                if i != int(len(list)) - 1:
                    fellow = fellow + '、'
            return fellow


        if flagy + flagr + flagp == 0:
            setFontNone = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
            date_title = "発表なし"
            draw.text((55, 420), date_title, font=setFontNone, fill="#000000", direction=None)
        else:
            if flagy + flagr + flagp == 1:
                if flagy == 1:
                    color = '#ffd400'
                    textw = '注意報'
                    textc = '#000000'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 424), printstr(yellowType), font=setFontfellow, fill="#000000", direction=None)
                elif flagr == 1:
                    color = 'red'
                    textw = '警報'
                    textc = '#ffffff'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 424), printstr(redType), font=setFontfellow, fill="#000000", direction=None)
                elif flagp == 1:
                    color = '#7f0085'
                    textw = '特别警報'
                    textc = '#ffffff'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 424), printstr(purpleType), font=setFontfellow, fill="#000000", direction=None)
                draw.rectangle((40,420,140,450), fill=color,outline='white', width=0)
                setFontW = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                draw.text((55+addx(textw), 424), textw, font=setFontW, fill=textc, direction=None)

            elif flagy + flagr + flagp == 2:
                if flagy == flagr and flagy == 1:
                    color2 = '#ffd400'
                    color1 = 'red'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 474), printstr(yellowType), font=setFontfellow, fill="#000000", direction=None)
                    draw.text((155, 424), printstr(redType), font=setFontfellow, fill="#000000", direction=None)
                    text1 = '注意報'
                    text2 = '警報'
                    fill1 = '#000000'
                    fill2 = '#ffffff'
                elif flagy == flagp and flagy == 1:
                    color2 = '#ffd400'
                    color1 = '#7f0085'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 474), printstr(yellowType), font=setFontfellow, fill="#000000", direction=None)
                    draw.text((155, 424), printstr(purpleType), font=setFontfellow, fill="#000000", direction=None)
                    text2 = '特别警報'
                    text1 = '注意報'
                    fill1 = '#000000'
                    fill2 = '#ffffff'
                elif flagr == flagp and flagr == 1:
                    color2 = 'red'
                    color1 = '#7f0085'
                    setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                    draw.text((155, 474), printstr(redType), font=setFontfellow, fill="#000000", direction=None)
                    draw.text((155, 424), printstr(purpleType), font=setFontfellow, fill="#000000", direction=None)
                    text2 = '特别警報'
                    text1 = '警報'
                    fill1 = '#ffffff'
                    fill2 = '#ffffff'
                draw.rectangle((40,420,140,450), fill=color1, outline='white', width=0)
                draw.rectangle((40,470,140,500), fill=color2, outline='white', width=0)
                draw.text((55 + addx(text1), 474), text1, font=setFontfellow, fill=fill1, direction=None)
                draw.text((55 + addx(text2), 424), text2, font=setFontfellow, fill=fill2, direction=None)
            elif flagy + flagr + flagp == 3:
                setFontfellow = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
                draw.rectangle((40,420,140,450), fill='#7f0085', outline='white', width=0)
                draw.text((55 + addx('特别警報'), 424), '特别警報', font=setFontfellow, fill='#ffffff', direction=None)
                draw.text((155, 424), printstr(purpleType), font=setFontfellow, fill="#000000", direction=None)
                draw.rectangle((40, 470, 140, 500), fill='red', outline='white', width=0)
                draw.text((55 + addx('警報'), 474), '警報', font=setFontfellow, fill='#ffffff', direction=None)
                draw.text((155, 474), printstr(redType), font=setFontfellow, fill="#000000", direction=None)
                draw.rectangle((40, 520, 140, 550), fill='#ffd400', outline='white', width=0)
                draw.text((55 + addx('注意報'), 524), '注意報', font=setFontfellow, fill='#000000', direction=None)
                draw.text((155, 524), printstr(yellowType), font=setFontfellow, fill="#000000", direction=None)


        draw.rectangle((20,19,1100,20),fill ='#ABBACD',outline ='white',width =0)
        draw.rectangle((20,20,1100,60),fill ='#E5EEF7',outline ='white',width =0)
        draw.rectangle((20,309+deta_h,1100,310+deta_h),fill ='#ABBACD',outline ='white',width =0)
        draw.rectangle((20,310+deta_h,1100,350+deta_h),fill ='#E5EEF7',outline ='white',width =0)

        draw.rectangle((134,360+deta_h,1100,450+deta_h),fill ='#e9eefd',width =0)
        draw.rectangle((20,360+deta_h,134,720+deta_h),fill ='#eeeeee',width =0)
        draw.rectangle((20,70,1100,290+50),outline ='#ABBACD',width =1)
        draw.line((560,70,560,290+50), fill='#ABBACD', width=1)
        draw.rectangle((20,360+deta_h,1100,720+deta_h),outline ='#ABBACD',width =1)
        draw.line((20,450+deta_h,1100,450+deta_h), fill='#ABBACD', width=1)
        draw.line((20,540+deta_h,1100,540+deta_h), fill='#ABBACD', width=1)
        draw.line((20,630+deta_h,1100,630+deta_h), fill='#ABBACD', width=1)

        #e9eefd
        draw.line((134,360+deta_h,134,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*1,360+deta_h,134+161*1,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*2,360+deta_h,134+161*2,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*3,360+deta_h,134+161*3,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*4,360+deta_h,134+161*4,720+deta_h), fill='#ABBACD', width=1)
        draw.line((134+161*5,360+deta_h,134+161*5,720+deta_h), fill='#ABBACD', width=1)

        setFont10 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 20)
        date_title = "日付"
        draw.text((55, 391+deta_h), date_title, font=setFont10, fill="#000000", direction=None)
        weather_title = "天気"
        draw.text((55, 481+deta_h), weather_title, font=setFont10, fill="#000000", direction=None)
        temp_title = "気温(℃)"
        draw.text((41, 571+deta_h), temp_title, font=setFont10, fill="#000000", direction=None)
        rainpro_title = "降水確率"
        draw.text((37, 645+deta_h), rainpro_title, font=setFont10, fill="#000000", direction=None)
        rainpro_title2 = "(%)"
        draw.text((60, 675+deta_h), rainpro_title2, font=setFont10, fill="#000000", direction=None)


        setFont1 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 20)
        textTitle = "深セン今日明日の天気"
        draw.text((30, 25), textTitle, font=setFont1, fill="#000000", direction=None)
        data_date = data_date.replace('发布','発表')
        data_date = data_date.replace('时','時')
        textRenewTime = data_date
        draw.text((845, 30), textRenewTime, font=ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17), fill="#000000", direction=None)
        textTitle = "週間天気"
        draw.text((30, 315+deta_h), textTitle, font=setFont1, fill="#000000", direction=None)

        draw.rectangle((40,200,540,235),fill='#f2f4fa')
        draw.rectangle((40,200,540,270),outline ='#ABBACD',width =1)
        draw.line((40,235,540,235), fill='#ABBACD', width=1)
        draw.line((140,200,140,270), fill='#ABBACD', width=1)

        draw.rectangle((580,200,1080,235),fill='#f2f4fa')
        draw.rectangle((580,200,1080,270),outline ='#ABBACD',width =1)
        draw.line((580,235,1080,235), fill='#ABBACD', width=1)
        draw.line((680,200,680,270), fill='#ABBACD', width=1)

        draw.line((240,200,240,270), fill='#ABBACD', width=1)
        draw.line((340,200,340,270), fill='#ABBACD', width=1)
        draw.line((440,200,440,270), fill='#ABBACD', width=1)

        draw.line((240+540,200,240+540,270), fill='#ABBACD', width=1)
        draw.line((340+540,200,340+540,270), fill='#ABBACD', width=1)
        draw.line((440+540,200,440+540,270), fill='#ABBACD', width=1)

        def addx(str):
            if str == '---':
                add = 20
            else:
                if len(str) == 2:
                    add = 20
                elif len(str) == 3:
                    add = 15
                elif len(str) == 4:
                    add = 9
            return add

        def addx2(str):
            if len(str) == 2:
                add = 16
            elif len(str) == 3:
                add = 14
            elif len(str) == 4:
                add = 8
            return add

        def addx3(str):
            if len(str) == 4:
                add = 26
            elif len(str) == 5:
                add = 20
            elif len(str) == 6:
                add = 14
            return add

        def addx4(str):
            if len(str) == 1:
                add = 30
            elif len(str) == 2:
                add = 20
            elif len(str) == 3:
                add = 10
            elif len(str) == 4:
                add = 0
            return add

        def addx5(str):
            if len(str) == 1:
                add = 33
            elif len(str) == 2:
                add = 25
            elif len(str) == 3:
                add = 18
            elif len(str) == 4:
                add = 10
            return add

        def addx6(str):
            if len(str) == 1:
                add = 28
            elif len(str) == 2:
                add = 21
            return add

        def addx7(str):
            if len(str) == 1:
                add = 37
            elif len(str) == 2:
                add = 31
            elif len(str) == 3:
                add = 25
            return add

        setFont4 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
        weather_time_title = "時間"
        draw.text((73, 207), weather_time_title, font=setFont4, fill="#000000", direction=None)
        weather_time_title = "時間"
        draw.text((613, 207), weather_time_title, font=setFont4, fill="#000000", direction=None)
        weather_pro_title = "降水"
        draw.text((73, 241), weather_pro_title, font=setFont4, fill="#000000", direction=None)
        weather_pro_title = "降水"
        draw.text((613, 241), weather_pro_title, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "0-6"
        draw.text((178, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "6-12"
        draw.text((273, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "12-18"
        draw.text((366, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "18-24"
        draw.text((466, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "0-6"
        draw.text((178+540, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "6-12"
        draw.text((273+540, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "12-18"
        draw.text((366+540, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)
        weather_time_title1 = "18-24"
        draw.text((466+540, 207), weather_time_title1, font=setFont4, fill="#000000", direction=None)

        #---------------------------以上为固定部分--------------------------------------


        now_time_hour = datetime.now()
        Today = now_time_hour.strftime('%H')
        dateHour = int(Today)
        data_wave = ''
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/waveTemp.txt", "r", encoding="utf-8") as f_wave:
            data_wave = f_wave.read()
        data_wave_list = data_wave.split(',')
        
        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/wind.txt", "r", encoding="utf-8") as f_wind:
            data_wind = f_wind.read()
        data_wind_list = data_wind.split(',')
        
        def judgewind(wd,maxWs,minWs):
            wind_str = ''
            if float(minWs) > float(maxWs):
                temp = maxWs
                maxWs = minWs
                minWs = temp
            
            if int(maxWs) < 5:
                wind_str = wd+'の風'
            elif int(maxWs) >= 6 and int(maxWs) <= 8:
                wind_str = wd+'の風やや強く'
            elif int(maxWs) >= 9:
                wind_str = wd+'の風強い'
            wind_str = wind_str.replace('转','後')
            wind_str = wind_str.replace('西南','南西')
            wind_str = wind_str.replace('東南','南東')
            wind_str = wind_str.replace('西北','北西')
            wind_str = wind_str.replace('東北','北東')
            return wind_str
        
        if deta_h != 0:
            
            day1_wind = judgewind(data_wind_list[0],data_wind_list[1],data_wind_list[2])
            day2_wind = judgewind(data_wind_list[3],data_wind_list[4],data_wind_list[5])
            
            if abs(float(data_wave_list[0]) - float(data_wave_list[3])) < 0.5:
                day1_wave = str(round((float(data_wave_list[0])+float(data_wave_list[3]))/2//0.5*0.5+0.5,1)) + 'メートル'
            else:
                day1_wave = str(round((float(data_wave_list[0])+float(data_wave_list[3]))/2//0.5*0.5+0.5,1)) + 'メートルうねりを伴う'
            
            if abs(float(data_wave_list[1]) - float(data_wave_list[4])) < 0.5:
                day2_wave = str(round((float(data_wave_list[1])+float(data_wave_list[4]))/2//0.5*0.5+0.5,1)) + 'メートル'
            else:
                day2_wave = str(round((float(data_wave_list[1])+float(data_wave_list[4]))/2//0.5*0.5+0.5,1)) + 'メートルうねりを伴う'
            
            
            draw.text((40, 280), '風：'+day1_wind, font=setFont4, fill="#000000", direction=None)
            draw.text((40+540, 280), '風：'+day2_wind, font=setFont4, fill="#000000", direction=None)
            draw.text((40, 310), '波：'+day1_wave, font=setFont4, fill="#000000", direction=None)
            draw.text((40+540, 310), '波：'+day2_wave, font=setFont4, fill="#000000", direction=None)
            
        if dateHour >= 6 :
            prob_day1_1 = '---'
        if dateHour >= 12:
            prob_day1_2 = '---'
        if dateHour >= 18:
            prob_day1_3 = '---'

        draw.text((160+addx(prob_day1_1), 241), prob_day1_1, font=setFont4, fill="#000000", direction=None)
        draw.text((260+addx(prob_day1_2), 241), prob_day1_2, font=setFont4, fill="#000000", direction=None)
        draw.text((360+addx(prob_day1_3), 241), prob_day1_3, font=setFont4, fill="#000000", direction=None)
        draw.text((460+addx(prob_day1_4), 241), prob_day1_4, font=setFont4, fill="#000000", direction=None)

        draw.text((160+addx(prob_day2_1)+540, 241), prob_day2_1, font=setFont4, fill="#000000", direction=None)
        draw.text((260+addx(prob_day2_2)+540, 241), prob_day2_2, font=setFont4, fill="#000000", direction=None)
        draw.text((360+addx(prob_day2_3)+540, 241), prob_day2_3, font=setFont4, fill="#000000", direction=None)
        draw.text((460+addx(prob_day2_4)+540, 241), prob_day2_4, font=setFont4, fill="#000000", direction=None)

        setFontProb = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 21)
        draw.text((170+addx7(prob_day3), 658+deta_h), prob_day3, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day4)+161*1, 658+deta_h), prob_day4, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day5)+161*2, 658+deta_h), prob_day5, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day6)+161*3, 658+deta_h), prob_day6, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day7)+161*4, 658+deta_h), prob_day7, font=setFontProb, fill="#000000", direction=None)
        draw.text((170+addx7(prob_day8)+161*5, 658+deta_h), prob_day8, font=setFontProb, fill="#000000", direction=None)


        setFont3 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 22)
        weather_text1 = weatherPicText(day1_weather)
        draw.text((180+addx4(weather_text1), 130), weather_text1, font=setFont3, fill="#000000", direction=None)
        weather_text2 = weatherPicText(day2_weather)
        draw.text((720+addx4(weather_text2), 130), weather_text2, font=setFont3, fill="#000000", direction=None)
        setFont11 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 16)
        weather_text3 = weatherPicText(day3_weather)
        draw.text((170+addx5(weather_text3)+161*0, 510+deta_h), weather_text3, font=setFont11, fill="#000000", direction=None)
        weather_text4 = weatherPicText(day4_weather)
        draw.text((170+addx5(weather_text4)+161*1, 510+deta_h), weather_text4, font=setFont11, fill="#000000", direction=None)
        weather_text5 = weatherPicText(day5_weather)
        draw.text((170+addx5(weather_text5)+161*2, 510+deta_h), weather_text5, font=setFont11, fill="#000000", direction=None)
        weather_text6 = weatherPicText(day6_weather)
        draw.text((170+addx5(weather_text6)+161*3, 510+deta_h), weather_text6, font=setFont11, fill="#000000", direction=None)
        weather_text7 = weatherPicText(day7_weather)
        draw.text((170+addx5(weather_text7)+161*4, 510+deta_h), weather_text7, font=setFont11, fill="#000000", direction=None)
        weather_text8 = weatherPicText(day8_weather)
        draw.text((170+addx5(weather_text8)+161*5, 510+deta_h), weather_text8, font=setFont11, fill="#000000", direction=None)

        
        def changeTemp(day0_maxT,TempMax):
            a = TempMax - day0_maxT
            str1 = ''
            if a > 0:
                str1 = "[+" + str(a) + "]"
            elif a == 0:
                str1 = "[+0]"
            elif a < 0:
                str1 = "[" + str(a) + "]"
            return str1

        with open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/day0.json", "r") as read_file2:
            text2 = json.load(read_file2)

        day0_maxT = text2['Temp_max']
        day0_minT = text2['Temp_min']
        day0_maxT = round(day0_maxT)
        day0_minT = round(day0_minT)

        setFontTemp = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 21)
        setFontTempChange = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 17)
        weather_TempMax1 = str(day1_TempMax)
        draw.text((282, 133), weather_TempMax1 + "℃" , font=setFontTemp, fill="#FF0000", direction=None)
        MaxTempChange1 = changeTemp(day0_maxT,day1_TempMax)
        draw.text((332, 136), MaxTempChange1 , font=setFontTempChange, fill="#FF0000", direction=None)

        weather_TempMin1 = str(day1_TempMin)
        draw.text((378, 133), weather_TempMin1 + "℃", font=setFontTemp, fill="#0000FF", direction=None)
        MinTempChange1 = changeTemp(day0_minT,day1_TempMin)
        draw.text((428, 136), MinTempChange1 , font=setFontTempChange, fill="#0000FF", direction=None)

        weather_TempMax2 = str(day2_TempMax)
        draw.text((822, 133), weather_TempMax2 + "℃", font=setFontTemp, fill="#FF0000", direction=None)
        MaxTempChange2 = changeTemp(day0_maxT,day2_TempMax)
        draw.text((872, 136), MaxTempChange2 , font=setFontTempChange, fill="#FF0000", direction=None)

        weather_TempMin2 = str(day2_TempMin)
        draw.text((918, 133), weather_TempMin2 + "℃", font=setFontTemp, fill="#0000FF", direction=None)
        MinTempChange2 = changeTemp(day0_minT,day2_TempMin)
        draw.text((968, 136), MinTempChange2 , font=setFontTempChange, fill="#0000FF", direction=None)

        setFontTemp2 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 20)
        weather_TempMax3 = str(day3_TempMax)
        draw.text((180+addx6(weather_TempMax3), 555+deta_h), weather_TempMax3, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin3 = str(day3_TempMin)
        draw.text((180+addx6(weather_TempMin3), 585+deta_h), weather_TempMin3, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax4 = str(day4_TempMax)
        draw.text((180+addx6(weather_TempMax4) + 161*1, 555+deta_h), weather_TempMax4, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin4 = str(day4_TempMin)
        draw.text((180+addx6(weather_TempMin4) + 161*1, 585+deta_h), weather_TempMin4, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax5 = str(day5_TempMax)
        draw.text((180+addx6(weather_TempMax5) + 161*2, 555+deta_h), weather_TempMax5, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin5 = str(day5_TempMin)
        draw.text((180+addx6(weather_TempMin5) + 161*2, 585+deta_h), weather_TempMin5, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax6 = str(day6_TempMax)
        draw.text((180+addx6(weather_TempMax6) + 161*3, 555+deta_h), weather_TempMax6, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin6 = str(day6_TempMin)
        draw.text((180+addx6(weather_TempMin6) + 161*3, 585+deta_h), weather_TempMin6, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax7 = str(day7_TempMax)
        draw.text((180+addx6(weather_TempMax7) + 161*4, 555+deta_h), weather_TempMax7, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin7 = str(day7_TempMin)
        draw.text((180+addx6(weather_TempMin7) + 161*4, 585+deta_h), weather_TempMin7, font=setFontTemp2, fill="#0000FF", direction=None)
        weather_TempMax8 = str(day8_TempMax)
        draw.text((180+addx6(weather_TempMax8) + 161*5, 555+deta_h), weather_TempMax8, font=setFontTemp2, fill="#FF0000", direction=None)
        weather_TempMin8 = str(day8_TempMin)
        draw.text((180+addx6(weather_TempMin8) + 161*5, 585+deta_h), weather_TempMin8, font=setFontTemp2, fill="#0000FF", direction=None)


        week_list = ["月","火","水","木","金","土","日"]
        locale.setlocale(locale.LC_CTYPE, 'chinese')
        setFont2 = ImageFont.truetype("C:/windows/fonts/msyh.ttc", 16)
        now_time = datetime.now()
        day = now_time.strftime('%m月%d日')
        date1 = day
        week1 = now_time.weekday()
        draw.text((114, 80), "("+week_list[week1]+")", font=setFont2, fill="#000000", direction=None)
        draw.text((40, 80), date1, font=setFont2, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=1)
        day = now_time.strftime('%m月%d日')
        date2 = day
        week2 = now_time.weekday()
        draw.text((654, 80), "("+week_list[week2]+")", font=setFont2, fill="#000000", direction=None)
        draw.text((580, 80), date2, font=setFont2, fill="#000000", direction=None)

        now_time = datetime.now() + timedelta(days=2)
        day = now_time.strftime('%m月%d日')
        date3 = day
        week3 = now_time.weekday()
        draw.text((196, 406+deta_h), "("+week_list[week3]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date3), 378+deta_h), date3, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=3)
        day = now_time.strftime('%m月%d日')
        date4 = day
        week4 = now_time.weekday()
        draw.text((196+161*1, 406+deta_h), "("+week_list[week4]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date4)+161*1, 378+deta_h), date4, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=4)
        day = now_time.strftime('%m月%d日')
        date5 = day
        week5 = now_time.weekday()
        draw.text((196+161*2, 406+deta_h), "("+week_list[week5]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date5)+161*2, 378+deta_h), date5, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=5)
        day = now_time.strftime('%m月%d日')
        date6 = day
        week6 = now_time.weekday()
        draw.text((196+161*3, 406+deta_h), "("+week_list[week6]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date6)+161*3, 378+deta_h), date6, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=6)
        day = now_time.strftime('%m月%d日')
        date7 = day
        week7 = now_time.weekday()
        draw.text((196+161*4, 406+deta_h), "("+week_list[week7]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date7)+161*4, 378+deta_h), date7, font=setFont10, fill="#000000", direction=None)
        now_time = datetime.now() + timedelta(days=7)
        day = now_time.strftime('%m月%d日')
        date8 = day
        week8 = now_time.weekday()
        draw.text((196+161*5, 406+deta_h), "("+week_list[week8]+")", font=setFont10, fill="#000000", direction=None)
        draw.text((155+addx3(date8)+161*5, 378+deta_h), date8, font=setFont10, fill="#000000", direction=None)


        weather_img1 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day1_weather + "_day.png")
        img_background.paste(weather_img1, (21, 110))
        weather_img2 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day2_weather + "_day.png")
        img_background.paste(weather_img2, (561, 110))
        a = 0.6
        weather_img3 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day3_weather + "_day.png")
        weather_img3 = weather_img3.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img3, (167 + 161*0, 460+deta_h))
        weather_img4 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day4_weather + "_day.png")
        weather_img4 = weather_img4.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img4, (167 + 161*1, 460+deta_h))
        weather_img5 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day5_weather + "_day.png")
        weather_img5 = weather_img5.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img5, (167 + 161*2, 460+deta_h))
        weather_img6 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day6_weather + "_day.png")
        weather_img6 = weather_img6.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img6, (167 + 161*3, 460+deta_h))
        weather_img7 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day7_weather + "_day.png")
        weather_img7 = weather_img7.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img7, (167 + 161*4, 460+deta_h))
        weather_img8 = Image.open("C:/Users/Administrator/Desktop/myBot/HoshinoBot/hoshino/modules/Airi_autoForecast/pic/" + day8_weather + "_day.png")
        weather_img8 = weather_img8.resize((int(150*a),int(80*a)), Resampling.LANCZOS)
        img_background.paste(weather_img8, (167 + 161*5, 460+deta_h))


        img_background.save('C:/Users/Administrator/Desktop/myBot/HoshinoBot/res/img/forecast.png')
        pic1 = R.img("forecast.png").cqcode
        msg = f'{pic1}'
        await bot.send(ev, msg)
        