# !/usr/bin/env python
# _*_coding:utf-8_*_

# 給任何使用這支程式的人：這支程式是新版台語台羅語音合成的API的client端。具體上會發送最下方變數data的台羅
# 給伺服器，並接收一個回傳的wav檔，output.wav
# 接受之台羅為教育部羅馬拼音，非教會羅馬拼音，請注意。
# 接受格式為UTF-8台羅，不是帶數字的。即請用類似"phái-sè"而非"phai2-se3"這種
# 不同port可以有不同格式，詳見下面的[注意]

#客戶端 ，用來呼叫service_Server.py
import socket
import random
import sys
import struct
from aiy.voice.audio import play_wav
### Don't touch
def askForService(token, data, model="M12_5"):
    # HOST, PORT 記得修改
    global HOST
    global PORT
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    received = ""
    try:
        sock.connect((HOST, PORT))
        msg = bytes(token+"@@@"+data+"@@@"+model, "utf-8")
        msg = struct.pack(">I", len(msg)) + msg
        sock.sendall(msg)
        
        with open('output.wav','wb') as f:
            while True:
                # print("True, wait for 15sec")
                # time.sleep(15)
                
                l = sock.recv(8192)
                # print('Received')
                if not l: break
                f.write(l)
        print("File received complete")
    finally:
        sock.close()
    return "OK"
### Don't touch

def process(token,data):
    # 可在此做預處理

    # 送出
    result = askForService(token,data)
    # 可在此做後處理
    return result

def main():
    global HOST
    global PORT
    ######### 注意：以下數字，10008為原版，10010套用實驗室變調版，10012則是接受中文輸入，即多套一個中文轉台羅
    ### ***10008以及10010接受台羅，10012接受中文
    HOST, PORT = "140.116.245.146", 10012
    token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3OTEyOTMxMzMsImlhdCI6MTYzMzYxMzEzMywic3ViIjoiIiwiYXVkIjoid21ta3MuY3NpZS5lZHUudHciLCJpc3MiOiJKV1QiLCJ1c2VyX2lkIjoiMjkwIiwibmJmIjoxNjMzNjEzMTMzLCJ2ZXIiOjAuMSwic2VydmljZV9pZCI6IjI0IiwiaWQiOjM5Niwic2NvcGVzIjoiMCJ9.XtqCCNnmc6tiNIOvcCsY6_vX-IjQFreYQWeU3BqXAvhZYCnjRUZvkcQcRLo-FjUikviipwRRYZhBGXK2Pd2xK8gfNu7LKRGh9V3sPvHIHn4MxC-YzV0tjQItGyIDW2w708YJQffx3v4A7wxnj3sjkxDxHIS8LApRcgk7Cd3Rdig"
    # data = "I kú-kú tsiah lâi tsi̍t pái"
    #data = "lîm--sian--sinn ê tsa-bóo-kiánn、 tíng-kò-gue̍h tsò--lâng āu--ji̍t 、tio̍h beh kè--lâng"
    #data = "台灣風景上蓋讚，一工一暝講袂完，安平古堡西仔灣，日月潭和阿里山，礁溪溫泉在宜蘭，新竹廟口吃貢丸，台灣美景名聲傳，大家歡喜由台灣。"

    choice = random.randint(1,6)

    if choice == 1:
        data = "台灣風景上蓋讚，一工一暝講袂完，安平古堡西仔灣，日月潭和阿里山，礁溪溫泉在宜蘭，新竹廟口吃貢丸，台灣美景名聲傳，大家歡喜由台灣。"
    elif choice == 2:
        data = "好地方，在哪裡。頭前轉角那就是，那有sui花kah魚池，阿公常去那下棋。"
    elif choice == 3:
        data ="阿伯本底是司機，退休了後閒閒無代誌，想欲排擔來賣餅，先去買鼎學煎餅。"
    elif choice == 4:
        data ="我有鉛筆幾若枝，這枝來寫字，彼枝畫圖較趣味，畫一隻貓咪咧吃魚，在畫一隻狗仔送阿姨。"
    elif choice == 5:
        data ="一隻狗仔吃兩碗飯，三隻雞仔生四粒卵，五隻貓仔很愛玩，從半夜玩到天亮。"
    elif choice == 6:
        data ="阿爸阿母把我當作寶，怕我生病，怕我跌倒，給我吃飽，穿好，健康大漢無煩惱。"


    for i in range(1):
        print("Client : ",process(token,data))

    play_wav("output.wav")
