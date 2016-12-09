import requests
from bs4 import BeautifulSoup
import json

#함지마루 식단 

from collections import OrderedDict
from datetime import datetime


def date_modify(date,week):
    num = int(date[len(date) -2:])

    if week == "화요일":
        num += 1
    elif week == "수요일":
        num += 2
    elif week == "목요일":
        num +=3
    elif week == "금요일":
        num +=4
    date =date[:len(date) -2] + str(num)

    return date

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


    if text["dietLength"] == 1:
        
        diet_0 = text["diet_0"][0]

        result_yethyang = OrderedDict({

        "name" : "중식 - ",
        "price":" 3500원",
        "time" : str(diet_0['st']) + " ~ " + str(diet_0['et']) + "\n",
        "mon" : "금요일 - "+start['value'] + "\n" + diet_0['d1'],
        "tue" : "토요일 - "+ date_modify(start['value'],"화요일")  + "\n" + diet_0['d2']+"\n",
        "wed" : "일요일 - "+ date_modify(start['value'],"수요일")  + "\n" + diet_0['d3'] + "\n",
        "thu" : "월요일 - "+ date_modify(start['value'],"목요일")  + "\n" + diet_0['d4'] + "\n",
        "fri" : "화요일 - "+ date_modify(start['value'],"금요일")  + "\n" + diet_0['d5']
        })

        result_yethyang_str = (

        result_yethyang['name'] + 
        "(" + result_yethyang['price'] + ")" + "\n"+ 
        result_yethyang['time'] + "\n" +
        result_yethyang['mon'] + "\n\n" +
        result_yethyang['tue'] + "\n" +
        result_yethyang['wed'] + "\n" +
        result_yethyang['thu'] + "\n\n" +
        result_yethyang['fri'] + "\n"        
        )
        
        
        message = start['value'] + " ~ " + end['value']+ "\n함지마루(복지관 학생식당) 금주 식단 입니다."+ "\n"+"\n!!!해당 정보는 학교 홈피에서 받아 오고 있습니다. 업데이트 안되어있을시, 학교 복지처에 문의해 주세요.!!!\n\n" + result_yethyang_str
        print(message)
        result = {"text":message}
        
        return result
    
    else:

        '''''''''''''옛향 식단 시작'''''''''''''

        diet_0 = text["diet_0"][0]

        result_yethyang = OrderedDict({

        "name" : "옛향 - ",
        "price":" 2500원",
        "time" : str(diet_0['st']) + " ~ " + str(diet_0['et']) + "\n",
        "mon" : "월요일 - "+start['value'] + "\n" + diet_0['d1'],
        "tue" : "화요일 - "+ date_modify(start['value'],"화요일")  + "\n" + diet_0['d2'],
        "wed" : "수요일 - "+ date_modify(start['value'],"수요일")  + "\n" + diet_0['d3'],
        "thu" : "목요일 - "+ date_modify(start['value'],"목요일")  + "\n" + diet_0['d4'],
        "fri" : "금요일 - "+ end['value']  + "\n" + diet_0['d5']
        })

        result_yethyang_str = (

        result_yethyang['name'] + 
        "(" + result_yethyang['price'] + ")" + "\n"+ 
        result_yethyang['time'] + "\n" +
        result_yethyang['mon'] + "\n\n" +
        result_yethyang['tue'] + "\n\n" +
        result_yethyang['wed'] + "\n\n" +
        result_yethyang['thu'] + "\n\n" +
        result_yethyang['fri'] + "\n"        
        )

        '''''''''''''옛향 식단 끝'''''''''''''


        '''''''''''''푸드코트 식단 시작'''''''''''''

        diet_1 = text["diet_1"][0]

        result_court = OrderedDict({

        "name" : "푸드코트 - ",
        "price":" 3,000원 ~ 3,500원",
        "time" : str(diet_1['st']) + " ~ " + str(diet_1['et']) + "\n",
        "mon" : "월요일 - "+start['value'] + "\n" + diet_1['d1'],
        "tue" : "화요일 - "+ date_modify(start['value'],"화요일")  + "\n" + diet_1['d2'],
        "wed" : "수요일 - "+ date_modify(start['value'],"수요일")  + "\n" + diet_1['d2'],
        "thu" : "목요일 - "+ date_modify(start['value'],"목요일")  + "\n" + diet_1['d2'],

        })

        result_court_str = (

        "\n\n" + result_court['name'] + 
        "(" + result_court['price'] + ")" + "\n"+ 
        result_court['time'] + "\n\n" +
        result_court['mon'] + "\n\n" +
        result_court['tue'] + "\n\n" +
        result_court['wed'] + "\n\n" +
        result_court['thu'] + "\n\n"

        )

        '''''''''''''푸드코트 식단 끝'''''''''''''



        '''''''''''''석식 식단 시작'''''''''''''

        diet_2 = text["diet_2"][0]

        result_dinner = OrderedDict({

        "name" : "석식 - ",
        "price":" 2,500원",
        "time" : str(diet_2['st']) + " ~ " + str(diet_2['et']) + "\n",
        "mon" : "월요일 - "+start['value'] + "\n" + diet_2['d1'],
        "tue" : "화요일 - "+ date_modify(start['value'],"화요일")  + "\n" + diet_2['d2'],
        "wed" : "수요일 - "+ date_modify(start['value'],"수요일")  + "\n" + diet_2['d2'],
        "thu" : "목요일 - "+ date_modify(start['value'],"목요일")  + "\n" + diet_2['d2'],

        })

        result_dinner_str = (

        "\n\n" + result_dinner['name'] + 
        "(" + result_dinner['price'] + ")" + "\n"+ 
        result_dinner['time'] + "\n" +
        result_dinner['mon'] + "\n\n" +
        result_dinner['tue'] + "\n\n" +
        result_dinner['wed'] + "\n\n" +
        result_dinner['thu'] + "\n"

        )

        '''''''''''''석식 식단 끝'''''''''''''

        message = start['value'] + " ~ " + end['value']+ "\n함지마루(복지관 학생식당) 금주 식단 입니다."+ "\n"+"\n!!!해당 정보는 학교 홈피에서 받아 오고 있습니다. 업데이트 안되어있을시, 학교 복지처에 문의해 주세요.!!!\n\n" + result_yethyang_str+"===============" + result_court_str+"===============" + result_dinner_str
        result = {"text":message}

        return result

if __name__ == "__main__":
    kw_hamjimaru()
