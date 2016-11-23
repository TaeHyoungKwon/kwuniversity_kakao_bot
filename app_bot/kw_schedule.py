import requests
from bs4 import BeautifulSoup
import json

#학사일정
from collections import OrderedDict
from datetime import datetime

def kw_schedule():

    initial_text =[]
    result_text = []
    
    url = "http://www.kw.ac.kr/ko/life/bachelor_calendar.do?mode=view&articleNo=165"
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    response = requests.get(url, headers={"USER-AGENT":u_a})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    textarea_soup = soup.find("textarea")
    start = soup.find("input",{"id" : "startPeriodTime"})
    end = soup.find("input",{"id" : "endPeriodTime"})

    text = textarea_soup.text
    text = json.loads(text)
    text = OrderedDict(sorted(text.items(),key=lambda item: int(item[0].split("_")[1])))
    
    #현재 '달' 로 부터 +4 달 만큼의 일정을 보여준다.
    #str(datetime.today().month)
    
    bachelor_11 = text["bachelor_11"][0]
    
    result_11 = OrderedDict({

    "month" : "11월 학사일정 입니다.\n\n\n",
    "event1": str(bachelor_11["sd_11_0"]) + " - " +str(bachelor_11["ed_11_0"]) + "\n" + str(bachelor_11["con_11_0"]),
    "event2": str(bachelor_11["sd_11_1"]) +" -  " +str(bachelor_11["ed_11_1"]) + "\n" + str(bachelor_11["con_11_1"]),
    "event3": str(bachelor_11["sd_11_2"]) + " -  "+str(bachelor_11["ed_11_2"]) +"\n" + str(bachelor_11["con_11_2"])
        })
    
    
    result_11_str = result_11["month"] + result_11["event1"]+"\n\n" + result_11["event2"]+"\n\n" + result_11["event3"] + "\n\n\n"
    
    print(result_11_str)
    
    
    
    bachelor_12 = text["bachelor_12"][0]
    
    result_12 = OrderedDict({

    "month" : "12월 학사일정 입니다.\n\n\n",
    "event1": str(bachelor_12["sd_12_0"]) + " - " +str(bachelor_12["ed_12_0"]) + "\n" + str(bachelor_12["con_12_0"]),
    "event2": str(bachelor_12["sd_12_1"]) +" -  " +str(bachelor_12["ed_12_1"]) + "\n" + str(bachelor_12["con_12_1"]),
    "event3": str(bachelor_12["sd_12_2"]) + " -  "+str(bachelor_12["ed_12_2"]) +"\n" + str(bachelor_12["con_12_2"]),
    "event4": str(bachelor_12["sd_12_3"]) + " -  "+str(bachelor_12["ed_12_3"]) +"\n" + str(bachelor_12["con_12_3"]),
    "event5": str(bachelor_12["sd_12_4"]) + " -  "+str(bachelor_12["ed_12_4"]) +"\n" + str(bachelor_12["con_12_4"]),
        })
    
    
    result_12_str = (result_12["month"] + 
                     result_12["event1"]+"\n\n"+ 
                     result_12["event2"]+"\n\n"+ 
                     result_12["event3"]+"\n\n"+  
                     result_12["event4"]+"\n\n"+ 
                     result_12["event5"])
    
    message = result_11_str + result_12_str
    
    result = {"text":message}

    return result
    
    
if __name__ == "__main__":
    kw_schedule() 
