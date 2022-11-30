import requests

def askForService(query:str, token:str) -> dict:
    '''
    Do sentiment analysis
    '''
    response = requests.post("http://140.116.245.157:9526", data={"inputtext":query, "token":token})
    if response.status_code == 200:
        return {"status":True, "result": response.text.strip()}
    else:
        return {"status":False, "result": None}
    



if __name__ == "__main__":
    query = "明天要去唱歌，好期待"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJ2ZXIiOjAuMSwiaWF0IjoxNjY0ODUxOTY2LCJ1c2VyX2lkIjoiNDI0IiwiaWQiOjU1Miwic2NvcGVzIjoiMCIsInN1YiI6IiIsImlzcyI6IkpXVCIsInNlcnZpY2VfaWQiOiIzMCIsImF1ZCI6IndtbWtzLmNzaWUuZWR1LnR3IiwibmJmIjoxNjY0ODUxOTY2LCJleHAiOjE4MjI1MzE5NjZ9.RYz99Yo6bO1asAgWykKe2D8V-N0sgoeQhYXH9Ek_njfG0nkKX-_LnMIz_Wx3WKGtqAzGK4wmlLJY00f-XTJkpDDyJBLMtDubQ1CKdKB7SA7q9HT0uCTpgI3oADWbBuBFZ0HPdm5gfu_l5y71vuFOFDQmIYlDGrhfMnoqB15P9No"
    r = askForService(query, token)
    print(r)
    emotion=r['result']
    print("情緒: "+emotion)