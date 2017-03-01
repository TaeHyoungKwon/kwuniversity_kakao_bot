
# coding: utf-8

# In[114]:

#17년 3월 수정

import requests
from bs4 import BeautifulSoup
import json
import datetime

#함지마루 식단 

from collections import OrderedDict


def date_modify(start_date,week):
    result = datetime.datetime.strptime(start_date,'%Y.%m.%d').date()
    
    if week == "화요일":
        result = result + datetime.timedelta(days=1)
    elif week =="수요일":
        result = result + datetime.timedelta(days=2)
    elif week =="목요일":
        result = result + datetime.timedelta(days=3)
    elif week =="금요일":
        result = result + datetime.timedelta(days=4)
    
    return str(result)



def kw_hamjimaru():

    url = "http://www.kw.ac.kr/ko/life/facility11.do"
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    response = requests.get(url, headers={"USER-AGENT":u_a})
    soup = BeautifulSoup(response.text, 'html.parser')

    textarea_soup = soup.find("textarea")
    start = soup.find("input",{"id" : "startPeriodTime"})
    end = soup.find("input",{"id" : "endPeriodTime"})

    text = textarea_soup.text
    text = json.loads(text)
    
    diet_0 = text["diet_0"][0]
    
    k ="원산지-쌀:국내산/\n배추,고춧가루:중국산"
    
    result_breaklaunch = OrderedDict({

        "name" : "조중식 - ",
        "price":" 2500원",
        "time" : str(diet_0['st']) + " ~ " + str(diet_0['et']) + "\n",
        "mon" : "월요일 - "+ start['value'] + "\n" + diet_0['d1']+"\n",
        "tue" : "화요일 - "+date_modify(start['value'],'화요일') +"\n" +diet_0['d2'].replace("\n\n\n","\n").replace(k,'')+"\n",
        "wed" : "수요일 - "+date_modify(start['value'],'수요일') +"\n" +diet_0['d3'].replace("\n\n\n","\n").replace(k,'')+"\n",
        "thu" : "목요일 - "+date_modify(start['value'],'목요일') +"\n" +diet_0['d4'].replace("\n\n\n","\n").replace(k,'')+"\n",
        "fri" : "금요일 - "+end['value']  + "\n" + diet_0['d5'].replace("\n\n\n","\n").replace(k,'')
      })
    
    
    result_breaklaunch_str = (

        result_breaklaunch['name'] + 
        "(" + result_breaklaunch['price'] + ")" + "\n\n\n"+ 
        result_breaklaunch['time'] + "\n\n\n" +
        result_breaklaunch['mon'] + "\n" +
        result_breaklaunch['tue'] + "\n" +
        result_breaklaunch['wed'] + "\n" +
        result_breaklaunch['thu'] + "\n" +
        result_breaklaunch['fri'] + "\n"        
        )

    
    diet_1 = text["diet_1"][0]
    

    
    
    result_foodcourt = OrderedDict({

        "name" : "푸드코트 - ",
        "price":" 3000원~3500원",
        "time" : str(diet_1['st']) + " ~ " + str(diet_1['et']) + "\n",
        "mon" : "월요일 - "+ start['value'] + "\n" + diet_1['d1']+"\n",
        "tue" : "화요일 - "+date_modify(start['value'],'화요일') +"\n" +diet_1['d2'].replace("\n\n\n","\n")+"\n",
        "wed" : "수요일 - "+date_modify(start['value'],'수요일') +"\n" +diet_1['d3'].replace("\n\n\n","\n")+"\n",
        "thu" : "목요일 - "+date_modify(start['value'],'목요일') +"\n" +diet_1['d4'].replace("\n\n\n","\n").replace(k,'')+"\n",
        "fri" : "금요일 - "+end['value']  + "\n" + diet_1['d5'].replace("\n\n\n","\n")
      })
    
    
    result_foodcourt_str = (

        result_foodcourt['name'] + 
        "(" + result_foodcourt['price'] + ")" + "\n\n\n"+ 
        result_foodcourt['time'] + "\n\n\n" +
        result_foodcourt['mon'] + "\n" +
        result_foodcourt['tue'] + "\n" +
        result_foodcourt['wed'] + "\n" +
        result_foodcourt['thu'] + "\n" +
        result_foodcourt['fri'] + "\n"        
        )
    
    
    
    diet_2 = text["diet_2"][0]    
    
    result_dinner = OrderedDict({

        "name" : "석식 - ",
        "price":" 2500원",
        "time" : str(diet_2['st']) + " ~ " + str(diet_2['et']) + "\n",
        "mon" : "월요일 - "+ start['value'] + "\n" + diet_2['d1']+"\n",
        "tue" : "화요일 - "+date_modify(start['value'],'화요일') +"\n" +diet_2['d2'].replace("\n\n\n","\n")+"\n",
        "wed" : "수요일 - "+date_modify(start['value'],'수요일') +"\n" +diet_2['d3'].replace("\n\n\n","\n")+"\n",
        "thu" : "목요일 - "+date_modify(start['value'],'목요일') +"\n" +diet_2['d4'].replace("\n\n\n","\n").replace(k,'')+"\n",
        "fri" : "금요일 - "+end['value']  + "\n" + diet_2['d5'].replace("\n\n\n","\n")
      })
    
    
    result_dinner_str = (

        result_dinner['name'] + 
        "(" + result_dinner['price'] + ")" + "\n\n\n"+ 
        result_dinner['time'] + "\n\n\n" +
        result_dinner['mon'] + "\n" +
        result_dinner['tue'] + "\n" +
        result_dinner['wed'] + "\n" +
        result_dinner['thu'] + "\n" +
        result_dinner['fri'] + "\n"        
        )
    
    message = start['value'] + " ~ " + end['value']+ "\n함지마루(복지관 학생식당) 금주 식단 입니다."+ "\n"+"\n!!!해당 정보는 학교 홈피에서 받아 오고 있습니다. 업데이트 안되어있을시, 학교 복지처에 문의해 주세요.!!!\n\n\n" + result_breaklaunch_str+"===============\n" + result_foodcourt_str+"===============\n" + result_dinner_str
    message = message.replace("\n\n","\n")
    result = {"text":message}
    
    return result


if __name__ == "__main__":
    kw_hamjimaru()


# In[ ]:



