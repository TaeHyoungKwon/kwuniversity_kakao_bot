import requests
from bs4 import BeautifulSoup
import json

#학사일정
from collections import OrderedDict
from datetime import datetime

def kw_schedule():

    initial_text =[]
    result_text = []

    #url = "http://www.kw.ac.kr/ko/life/bachelor_calendar.do?mode=view&articleNo=165"
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
                     result_3["event3"]+"\n\n\n"
)

    bachelor_4 = text["bachelor_4"][0]

    result_4 = OrderedDict({

    "month" : "##광운대 17년도 4월 학사일정 입니다.##\n\n",
    "event1": str(bachelor_4["sd_4_0"])+ " ~ " + bachelor_4["ed_4_0"] +"\n"+str(bachelor_4["con_4_0"]),
    "event2": str(bachelor_4["sd_4_1"])+ " ~ "+ bachelor_4["ed_4_1"] +"\n"+ str(bachelor_4["con_4_1"]),
    "event3": str(bachelor_4["sd_4_2"])+"\n"+ str(bachelor_4["con_4_2"]),
    "event4": str(bachelor_4["sd_4_3"])+ " ~ "+ bachelor_4["ed_4_3"] +"\n"+ str(bachelor_4["con_4_3"]),
    "event5": str(bachelor_4["sd_4_4"])+"\n"+ str(bachelor_4["con_4_4"]),
        })


    result_4_str = (result_4["month"] +
                     result_4["event1"]+"\n\n"+
                     result_4["event2"]+"\n\n"+
                     result_4["event3"]+"\n\n"+
                    result_4["event4"]+"\n\n"+
                    result_4["event5"]+"\n\n\n"
)

    bachelor_5 = text["bachelor_5"][0]

    result_5 = OrderedDict({

    "month" : "##광운대 17년도 5월 학사일정 입니다.##\n\n",
    "event1": str(bachelor_5["sd_5_0"])+ " ~ " + bachelor_5["ed_5_0"] +"\n"+str(bachelor_5["con_5_0"]),
    "event2": str(bachelor_5["sd_5_1"])+ " ~ "+ bachelor_5["ed_5_1"] +"\n"+ str(bachelor_5["con_5_1"]),
    "event3": str(bachelor_5["sd_5_2"])+"\n"+ str(bachelor_5["con_5_2"]),
    "event4": str(bachelor_5["sd_5_3"])+ " ~ "+ bachelor_5["ed_5_3"] +"\n"+ str(bachelor_5["con_5_3"]),
    "event5": str(bachelor_5["sd_5_4"])+"\n"+ str(bachelor_5["con_5_4"]),
        })


    result_5_str = (result_5["month"] +
                     result_5["event1"]+"\n\n"+
                     result_5["event2"]+"\n\n"+
                     result_5["event3"]+"\n\n"+
                    result_5["event4"]+"\n\n"+
                    result_5["event5"]+"\n\n\n"
)


    bachelor_6 = text["bachelor_6"][0]

    result_6 = OrderedDict({

    "month" : "##광운대 17년도 6월 학사일정 입니다.##\n\n",
    "event1": str(bachelor_6["sd_6_0"])+ " ~ " + bachelor_6["ed_6_0"] +"\n"+str(bachelor_6["con_6_0"]),
    "event2": str(bachelor_6["sd_6_1"])+ " ~ "+ bachelor_6["ed_6_1"] +"\n"+ str(bachelor_6["con_6_1"]),
    "event3": str(bachelor_6["sd_6_2"])+ " ~ "+ bachelor_6["ed_6_2"] +"\n"+ str(bachelor_6["con_6_2"]),
    "event4": str(bachelor_6["sd_6_3"])+"\n"+ str(bachelor_6["con_6_3"]),
    "event5": str(bachelor_6["sd_6_4"])+ " ~ "+ bachelor_6["ed_6_4"] +"\n"+ str(bachelor_6["con_6_4"]),

        })


    result_6_str = (result_6["month"] +
                     result_6["event1"]+"\n\n"+
                     result_6["event2"]+"\n\n"+
                     result_6["event3"]+"\n\n"+
                    result_6["event4"]+"\n\n"+
                    result_6["event5"]
)

    message = result_3_str + result_4_str + result_5_str + result_6_str
    result = {"text":message}

    return result


if __name__ == "__main__":
    kw_schedule()
