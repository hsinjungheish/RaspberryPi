from gtts import gTTS
import socket
import urllib
import os
from aiy.voice.audio import play_wav

choice  = ''

def ch_tts(text, file_):
    tts = gTTS(text, lang = 'zh-tw')
    tts.save(file_ + '.wav')

def askmusic():
    
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
            tts = gTTS(text='請問你想聽甚麼音樂', lang='zh-tw')
            tts.save("test.mp3")
            os.system("mpg123 test.mp3")
            break

def askquestion():
    
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
            tts = gTTS(text='請提問', lang='zh-tw')
            tts.save("test.mp3")
            os.system("mpg123 test.mp3")
            break

def askweather():
    
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
            tts = gTTS(text='請說出你想查詢的城市', lang='zh-tw')
            tts.save("test.mp3")
            os.system("mpg123 test.mp3")
            break

def playmusic():
    if choice == 'classic':
        play_wav("piano.wav")
    elif choice =='happy':
        play_wav("happy.wav")
    elif choice == 'popular':
        play_wav("popular.wav")
    elif choice == 'sad':
        play_wav("sad.wav")

    

if __name__ == "__main__":
    askmusic()
