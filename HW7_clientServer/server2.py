#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

HOST = '192.168.0.21'
PORT = 50

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    while True:
        question = conn.recv(1024)
        answer = ''
        if len(question) == 0: # connection closed
            conn.close()
            print('client closed connection.')
            break
        print('recv: ' + question.decode())
        question = question.decode()
        if question=='哪些台灣人曾獲諾貝爾獎':
            answer = ('李遠哲、丁肇中、李振道、楊振寧')
        elif question=='國立故宮博物院館藏文物有多少':
            answer = ('國立故宮博物院館藏文物計有698,649件冊')
        elif question=='斐陶斐獎獲選資格':
            answer = ('品學特優者，每一學院每屆得推選三人')
        elif question=='台灣補教業佔GDP比例為多少':
            answer = ('占GDP國內生產毛額比重 4.66%')
        elif question=='全球大學電腦科學系排名前五':
            answer = ('史丹佛大學、麻省理工學院、英國牛津大學、蘇黎世聯邦理工學院、劍橋大學') 
        elif question=='養一個小孩從出生到大學畢業要花多少錢':
            answer = ('養大一個孩子的最低花費為 500 萬，建議父母在子女教育基金約在整個家庭資產配置的中的 10～20%')  
        elif question=='多少美國總統是哈佛大學校友':
            answer = ('8名美國總統，他們分別是：約翰·亞當斯、約翰·昆西·亞當斯、拉瑟福德·伯查德·海斯、狄奧多·羅斯福、富蘭克林·德拉諾·羅斯福、約翰·甘迺迪、喬治·沃克·布希及巴拉克·歐巴馬。') 
        elif question=='台灣共有多少所大學':
            answer = ('我國大專校院學校數共計149所，其中大學126所、學院11所、專科學校12所') 
        elif question=='我國12歲以下學童近視比例':
            answer = ('66%') 
        elif question=='國中教育會考成績計算方式':
            answer = ('詳情請洽:https://www.go100.com.tw/article_junior_senior_01.php')   
        elif question=='台南十大網美景點':
            answer = ('台南藍晒圖文創園區、台南安平德陽艦園區、台南山上花園水道博物館、台南西拉雅官田遊客中心、台南美術二館、台南學甲老塘湖藝術村、大魚的祝福、台南七股遊客中心、蝸牛巷、台南柳營德元埤荷蘭村')            
        elif question=='台灣五星級飯店密度最高的縣市':
            answer = ('宜蘭縣')
        elif question=='下載量最高的社群軟體為何':
            answer = ('Tik Tok')
        elif question=='台南棒球場門票價格是多少錢':
            answer = ('平日:內野全票350元、半票250元外野200元  假日:內野全票450元、半票350元外野300元')
        elif question=='影史票房最高的是哪部電影':
            answer = ('阿凡達 $2,879,059,572美元')
        elif question=='台北信義區有哪些夜店':
            answer = ('Babe18、池畔酒吧、18号房间、Electro、Chess Taipei、IKON Taipei')
        elif question=='錢櫃KTV夜唱一晚要花多少錢':
            answer = ('799元/5H')
        elif question=='美國哪些州已開放大麻合法化':
            answer = ('阿拉斯加州、亞利桑那州、加利福尼亞州、科羅拉多州、伊利諾伊州、緬因州、馬薩諸塞州、密歇根州、內華達州、俄勒岡州、華盛頓州')
        elif question=='台灣最大的遊樂園在哪個縣市':
            answer = ('新竹-六福村主題遊樂園')
        elif question=='台中有哪些outlet':
            answer = ('台中港三井OUTLET、麗寶Outlet Mall')
        elif question=='葉克膜副作用有哪些':
            answer = ('出血、腎衰竭、中風')
        elif question=='台灣可施打到哪些廠牌的COVID-19疫苗':
            answer = ('高端、AZ、莫德納、BNT、嬌生')
        elif question=='台灣醫院如何分級':
            answer = ('「診所」、「地區醫院」、「區域醫院」與「醫學中心」4級')
        elif question=='帕金森氏症初級症狀為何':
            answer = ('認知障礙、行為失常的症狀')
        elif question=='抽菸可能造成的健康危害':
            answer = ('抽菸有害健康，對身心健康罄竹難書，詳情請查看:https://www.cmuh.cmu.edu.tw/NewsInfo/NewsArticle?no=7223')
        elif question=='哪個縣市的醫療資源最為匱乏':
            answer = ('金門縣')
        elif question=='可能導致失眠的因素有哪些':
            answer = ('焦慮、憂鬱、適應障礙常是失眠的主因')
        elif question=='2021國人十大死因榜首為何':
            answer = ('惡性腫瘤（癌症)')
        elif question=='可治療漸凍人的藥物有哪些':
            answer = ('銳利得（Riluzole）、依達拉奉（Edaravone）、COX-II 抑制劑')
        elif question=='標準的CPR流程是什麼':
            answer = ('叫叫CAB')
        elif question=='紅景天對人體的具體幫助為何':
            answer = ('有益憂鬱症、有益不穩定型心絞痛、有益身心疲勞、預防急性高山病、有益壓力緩解')
        elif question=='多吃芝麻真的有助於減少白頭髮嗎':
            answer = ('不會，但建議多攝取維生素E')
        elif question=='適合銀髮族的運動有哪些':
            answer = ('快走、自行車、游泳、太極拳')
        elif question=='每日攝取維生素D對身體的幫助':
            answer = ('促進骨骼、牙齒健康、協助維持肺功能與心血管健康')
        elif question=='長期睡眠不足會影響哪些身體機能':
            answer = ('情緒容易反應過度、注意力不集中、心血管疾病風險增加50％、容易罹患乳癌')
        elif question=='過度飲水對健康帶來的危害':
            answer = ('水中毒，水中毒會造成血液裡鈉離子偏低，進而出現視力模糊、頭暈、頭痛、全身無力嘔吐、肌肉抽筋，嚴重時，甚至會引起癲癇發作、昏迷及死亡。')
        elif question=='防止骨質疏鬆有哪些方法':
            answer = ('加強補充鈣、走路與負重運動')
        elif question=='多吃什麼有助於保養視力':
            answer = ('攝取深綠色蔬菜和黃色水果，及多吃新鮮魚類，並適度補充莓果和堅果')
        elif question=='做什麼運動對青少年骨骼發育有負面影響':
            answer = ('若可做到的最大重量為 RM，訓練的重量建議落在60～80％的 RM，可以降低受傷的機率')
        elif question=='哪些生活習慣有益於預防老年失智':
            answer = ('有氧運動、減少攝取高糖高油食物')
        elif question=='這附近有沒有日式料理?':
            answer = ('川田日本料理, 地址: 700台南市中西區北門路一段9號')
        elif question=='宵夜應該吃甚麼比較不會胖?':
            answer = ('堅果、雞蛋、優格、豆漿、牛奶')
        elif question=='如何製作鬆餅?':
            answer = ('1.將牛奶跟雞蛋以打蛋器充分混合。\n2.不需過篩直接倒入鬆餅粉在液體內。\n3.均勻攪拌不需要使勁地打，讓麵粉不會結塊即可。\n4.在平底鍋內放入一小塊奶油，如果是使用不沾鍋可以不放。 不過有放奶油的鬆餅香氣會更濃厚，緩緩倒入麵糊。\n5.接著轉小火煎3分鐘，翻面再煎2分鐘熟透就能起鍋。')
        elif question=='台南有哪些好吃的傳統小吃?':
            answer = ('碗粿、米糕、鹹粥、擔仔麵、杏仁豆腐冰')
        elif question=='哪些披薩店有外送的服務?':
            answer = ('拿坡里、必勝客、搖滾披薩、比薩屋、丹尼披薩')
        elif question=='請問茶跟果汁哪個比較能解渴?':
            answer = ('茶相較於果汁較解渴, 建議飲用無糖茶更能達到解渴效果。')
        elif question=='感染腸胃炎能夠吃甚麼比較適合?':
            answer = ('建議選擇好消化又能補充能量的香蕉、白飯、蘋果醬、吐司等食物。')
        elif question=='麥當勞跟肯德基的薯條哪個熱量比較低?':
            answer = ('麥當勞: 小薯265 Kcal/ 中薯376 Kcal/ 大薯 529 Kcal。\n肯德基: 香酥脆薯 中份 185 Kcal')
        elif question=='太陽餅裡面為甚麼沒有太陽?':
            answer = ('就與是車輪餅裡面沒有車輪同樣道理')
        elif question=='哪些食材屬於火鍋料?':
            answer = ('炸豆皮、百頁豆腐、魚包蛋、貢丸、起士麻糬燒、蛋餃、蟹肉棒、魚餃')
        elif question=='襯衫適合搭配甚麼褲子?':
            answer = ('牛仔褲、西裝褲')
        elif question=='為甚麼冰鋒衣穿比不穿還涼?':
            answer = ('冰鋒衣運用涼感布料快乾科技，透過吸濕時的物理變化，快速散熱透氣，經實驗證明，能有效減少身體表面溫度')
        elif question=='緊身褲在運動時有甚麼效用?':
            answer = ('運動時穿著彈力緊身褲，有助於觀察確認動作的正確性，並達到穩定關節的效果')
        elif question=='羽絨衣怎麼達到保暖效果的?':
            answer = ('“羽絨” 是個很好的絕緣體，原理是利用羽絨能在外套間造成空隙，並抓住暖空氣將熱量保留下來，因此就算外面的空氣再冷，你的體溫也不容易散發出去以藉此達到保暖作用。')
        elif question=='毛衣起毛球時該如何處理?':
            answer = ('1.除毛球機、毛球修剪器 這是最簡單也最方便的方法\n2.拿出寬版的透明膠帶，用黏性就可以將毛球黏起去除\n3.使用拋棄式的刮鬍刀，原理就與毛球修剪器相同，將毛球減下。')
        elif question=='洗衣服時把衛生紙放在口袋裡會不會被媽媽罵?':
            answer = ('衣服洗完後都會被衛生紙屑污染, 肯定被罵')
        elif question=='為甚麼深色衣服會顯瘦?':
            answer = ('深色顯瘦的原因是因為，在色彩心理學中，它們屬於收縮色。')
        elif question=='泳衣是用甚麼材質做成的?':
            answer = ('大部分的泳裝材質，都會使用80%尼龍+20彈性纖維的混和材料來製作泳衣。')
        elif question=='日本與韓國的和服差別是甚麼?':
            answer = ('韓服的一個特點是裙子看起來非常的蓬鬆，而且上衣會在腰部以上並且會在交界的地方有一個很大的系帶可以打成蝴蝶結。\n漢服一般都是交領右衽，裙子看起來是自然下垂的不會顯得蓬蓬的。')
        elif question=='面試的時候怎麼穿比較有禮貌?':
            answer = ('上身：內搭淺色正式襯衫，外穿深色系（黑、深藍、灰）正式西裝外套。\n下身：配合上衣，穿深色西裝褲；女生可以選擇穿及膝西裝裙。\n鞋子：皮鞋或低跟鞋。')
        elif question=='金融大樓裡通常都會有甚麼防盜裝置?':
            answer = ('在辦公區域的大門，一般都會設有門鎖，或經過保全人員的身分確認才可通行，而公共進出的通道會有明顯的標示說明，在無人的區域則設置防盜系統或監視器等。')
        elif question=='台南最高的房子是幾層樓?':
            answer = ('香格里拉台南遠東國際大飯店: 38層樓')
        elif question=='房屋架構該如何達到防震?':
            answer = ('1. 鋼筋搭接處絕對要避免搭接在容易破壞的地方，而且要「錯位搭接」，才能平均分散地震的力量。\n2. 黏滯型「阻尼器」減少建築搖晃\n3. 調質阻尼器是一顆大型金屬球，會把地震、風力等外力吸收，減少房屋擺動。')
        elif question=='台北市的房價與東京都的房價何者較貴?':
            answer = ('台北市一坪平均房價，大概將近190萬，東京110萬，而且東京是實坪制，等於台北市的一坪房價，平均比東京高出80萬。')
        elif question=='房子甚麼樣的格局會導致風水不順?':
            answer = ('兩臥室內有拐角，戶型不方正，兩臥室之間不是承重牆，隔音效果差，廁所對著廚房風水不佳。')
        elif question=='如何把比大門還更大的鋼琴搬進屋內?':
            answer = ('需以吊車作業方式, 吊掛鋼琴入顧客新址前陽台。')
        elif question=='如何清洗床墊?':
            answer = ('建議可以將小蘇打、酒精、肥皂水、醋、清水等清潔用品混合使用，若局部污漬頑強，可重複清洗，後續使用除濕機、冷風吹風機吹乾。\n若床墊沾上血漬，可使用肥皂水或雙氧水清潔，用牙刷、抹布刷洗擦拭床墊。')
        elif question=='通常車位會佔房屋的幾坪空間?':
            answer = ('大車位為4.12坪（250㎝×550㎝）、小車位為3.83坪（230㎝×550㎝）')
        elif question=='該如何改善屋內的不通風?':
            answer = ('可在窗戶下加裝氣窗來解決室內空氣流動問題，如此就算關著窗也有風進入。')
        elif question=='屋外磁磚因下雨導致生鏽該怎麼辦?':
            answer = ('透過簡單的牙膏、醋搭配清潔劑，就可能將鏽斑擦去，讓家恢復如新！')
        elif question=='為甚麼台灣只有四個縣市有捷運?':
            answer = ('其他縣市人口密度不夠、自償性不夠')
        elif question=='為甚麼台南交通那麼混亂?':
            answer = ('因台南圓環太多且道路狹小')
        elif question=='為甚麼各縣市的公用腳踏車不同樣使用Ubike的名字就好了?':
            answer = ('那是youbike公司自行決定的')
        elif question=='輕軌跟捷運的差別是甚麼?':
            answer = ('輕軌運輸車輛一般長度約為30 公尺長，載客量約為250 人，並可雙車以上聯結營運\n公車捷運車輛一般長度約18 公尺長，載客量約為150 人，僅能以單車營運。')
        elif question=='台灣一天平均有幾個飛機班次?':
            answer = ('一年大約二十萬班/一天大約五百')
        elif question=='直升機與熱氣球發生事故的頻率何者較高?':
            answer = ('沒有相符的搜尋結果')
        elif question=='星期幾買機票最便宜?':
            answer = ('星期二買機票是一週內最便宜的日期，由於部分航空公司會選在週二提供一些機票的優惠價。')
        elif question=='租一整天的遊艇價格大約是多少?':
            answer = ('從幾十萬到幾千萬不等，大型豪華遊艇一般都上千萬元，中型遊艇在二百萬以上，小型遊艇從幾十萬到二百萬之間，隨著遊艇的尺寸、裡面裝潢豪華程度的增加，價格也隨之增長。')
        elif question=='沒有車牌的自製車行駛在道路上是合法的嗎?':
            answer = ('法律上有規定可以將無牌車沒入(就是俗稱的扣車)')
        elif question=='如果看到警車紅燈右轉可以抓他嗎?':
            answer = ('可以檢舉警察, 警員也應要收到罰單後, 提出自己在執行任務而違規, 循正常管道申訴。')
        

        outdata = 'echo ' + answer
        conn.send(outdata.encode())