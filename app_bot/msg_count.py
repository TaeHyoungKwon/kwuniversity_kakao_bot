import sqlite3
import datetime
import json

def msg_count():

    con = sqlite3.connect("../db.sqlite3")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM app_bot_searchword;")
    
    total_cnt =0

    d = datetime.datetime.today()
    k = str(d.year) + "-" + str(d.month) + "-" + str(d.day)

    cnt=0
    print(cnt)
    for data in cursor:
        if data[2][:10] == k:
            cnt+=1
            total_cnt+=1
        else:
            total_cnt+=1

    message = "총 {}건 중에 금일 '{}'일은 {} 건 입니다.".format(total_cnt,k,cnt)

    result = {"text":message}        

    return result
