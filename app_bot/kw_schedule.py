import requests
from bs4 import BeautifulSoup
import json

#학사일정
from collections import OrderedDict
from datetime import datetime

def kw_schedule():

    initial_text =[]
    result_text = []
    url = "http://www.kw.ac.kr/ko/life/bachelor_calendar.do"
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
    
    bachelor_2 = text["bachelor_2"][0]
    
    result_2 = OrderedDict({

    "month" : "##광운대 17년도 2월 학사일정 입니다.##\n\n",
    "event1": str(bachelor_2["sd_2_0"]) + " - " +str(bachelor_2["ed_2_0"]) + "\n" + str(bachelor_2["con_2_0"]),
    "event2": str(bachelor_2["sd_2_1"]) +" -  " +str(bachelor_2["ed_2_1"]) + "\n" + str(bachelor_2["con_2_1"]),
    "event3": str(bachelor_2["sd_2_2"]) + " -  "+str(bachelor_2["ed_2_2"]) +"\n" + str(bachelor_2["con_2_2"]),

    "event4": str(bachelor_2["sd_2_3"]) + " - " +str(bachelor_2["ed_2_3"]) + "\n" + str(bachelor_2["con_2_3"]),
    "event5": str(bachelor_2["sd_2_4"]) +" -  " +str(bachelor_2["ed_2_4"]) + "\n" + str(bachelor_2["con_2_4"]),
    "event6": str(bachelor_2["sd_2_5"])  +"\n" + str(bachelor_2["con_2_5"]),
 
    "event7": str(bachelor_2["sd_2_6"])  +"\n" + str(bachelor_2["con_2_6"]),
    "event8": str(bachelor_2["sd_2_7"])  +"\n" + str(bachelor_2["con_2_7"].strip()),
    "event9": str(bachelor_2["sd_2_8"]) +"\n" + str(bachelor_2["con_2_8"]),
 
    "event10": str(bachelor_2["sd_2_9"]) + " - " +str(bachelor_2["ed_2_9"]) + "\n" + str(bachelor_2["con_2_9"])
 
        })
    
    
    
    result_2_str = (
            result_2["month"] + 
            result_2["event1"]+"\n\n" + 
            result_2["event2"]+"\n\n" + 
            result_2["event3"] + "\n\n" + 
            
            result_2["event4"]+"\n\n" + 
            result_2["event5"]+"\n\n" + 
            result_2["event6"] + "\n\n" + 
            
            result_2["event7"]+"\n\n" + 
            result_2["event8"]+"\n\n" + 
            result_2["event9"] + "\n\n" + 
            
            result_2["event10"]+"\n\n\n"
            
            )
    
    
    bachelor_3 = text["bachelor_3"][0]
    
    result_3 = OrderedDict({

    "month" : "##광운대 17년도 3월 학사일정 입니다.##\n\n",
    "event1": str(bachelor_3["sd_3_0"]) +"" + str(bachelor_3["con_3_0"]),
    "event2": str(bachelor_3["sd_3_1"]) +"\n"+ str(bachelor_3["con_3_1"]),
    "event3": str(bachelor_3["sd_3_2"])+"\n"+ str(bachelor_3["con_3_2"]),
        })
    
    
    result_3_str = (result_3["month"] + 
                     result_3["event1"]+"\n"+ 
                     result_3["event2"]+"\n\n"+ 
                     result_3["event3"]
)
    
    message = result_2_str + result_3_str
    
    result = {"text":message}
    
    return result
    
    
if __name__ == "__main__":
    kw_schedule() 
