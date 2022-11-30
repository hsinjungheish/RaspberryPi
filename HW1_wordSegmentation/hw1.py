import os

def get_dictionary(file_path):
    dict = []
    with open(file_path,'r', encoding='UTF-8') as f:
        while(line := f.readline().strip()):
            if line:
                dict.append(line)
            else:
                break
    return dict 

def MaxMatch(sentence, dictionary):
    n = len(sentence)#先計算sentence長度
    if sentence == '':# 若sentence為空，回傳一個empty的list
        return []
    for i in range(n - 1):
        firstword = sentence[:n - i]#sentence中的前i個字符
        remainder = sentence[n - i:]#sentence剩下的字符們
        #若firstword在dict中orfirstword為英文字母（因預判斷的句子為中英混雜）
        if firstword in dictionary or firstword.isascii(): 
            return [firstword] + MaxMatch(remainder,dictionary)
    #沒有找到對應的字，自己成一個character
    firstword = sentence[0]
    remainder = sentence[1:]
    return [firstword] + MaxMatch(remainder,dictionary)
    

if __name__ == "__main__":
    dict=get_dictionary('dict_no_space.txt')
    sen="聯合國教科文組織的簡稱是UNESCO，旨在通過教育、科學及文化來促進各國合作，對和平與安全作出貢獻。"
    string=MaxMatch(sen,dict)
    print(string)
   

  



