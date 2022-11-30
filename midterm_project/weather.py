import requests
import json
import image as emoji
import urllib
from gtts import gTTS
import animate as a
import text_oled as display
import os

city = ''
chinesecity = ''
def getWeather(city):
    apikey ='1a0354cc5b45800d1967843dbdf06147'
    path='https://api.openweathermap.org/data/2.5/find?q=%s&appid=%s'
    resp=requests.get(path%(city,apikey))
    data=json.loads(resp.text)
    main=data['list'][0]['main']
    description=data['list'][0]['weather'][0]['description']
    return main['temp'],main['feels_like'],main['humidity'],description
    #print(resp.text)

def main():
#if'__main__'==__name__:
    temp, feels_like, humidity, description = getWeather(city)
    print("溫度:%.2f 體感:%.2f 濕度:%d %% %s"%(temp-273.15,feels_like-273.15,humidity,description))
    test = '今日%s的氣溫是攝氏%.2f度 體感溫度為%.2f度 濕度為%d趴 天氣為 %s'%(chinesecity, temp-273.15,feels_like-273.15,humidity,description)
    print(test)

    while True:
        try:
            urllib.request.urlopen("http://www.google.com")
        except urllib.error.URLError:
            print("Fail to connect Internet...")
            os.system("")
            time.sleep(1)
        else:
            print("Connected")
            # change here
            tts = gTTS(text=test, lang='zh-tw')
            tts.save("test.mp3")
            print("回答: "+test)
            word = '今日%s的天氣為%s'%(chinesecity, description)
            display.display_text(word)
            print("情緒: "+description)
            print("\n\n")
            os.system("mpg123 test.mp3")
            emoji.emotion = description
            emoji.printWeather()
            break
    #getWeather('Taipei')
