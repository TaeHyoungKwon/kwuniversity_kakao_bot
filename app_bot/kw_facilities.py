import requests
from bs4 import BeautifulSoup
import json

#편의시설

def kw_facilities():

    url = "http://www.kw.ac.kr/ko/life/facility09.do"
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    response = requests.get(url, headers={"USER-AGENT":u_a})

    soup = BeautifulSoup(response.text, 'html.parser')
    
    div_soup = soup.find("section",{"class":"h3_contents-block"}).text
    k = div_soup.split("\n")
    
    for a in k[:]:
        if a == "":
            k.remove(a)  
    cnt=0
    message1 = ""
    message2 = ""
    message3 = "\n"
    for a in k[1:19]:
        message1 += a +"\n"
        cnt+=1
        if cnt % 6 == 0:
            message1 +="\n"
            
    for a in k[19:34]:
        message2 += a +"\n"
        for b in ["주요상품 : 전공서적, 교재, 책, 잡지 등","영업시간 : 개장시간 보러가기","금융업무 안함","영업시간 : 09:00~18:00"]:
            if b in a:
                message2 += "\n"

    for a in k[34:]:
        message3 += a + "\n"
    
    message = message1 + message2 + message3
    
    result = {"text":message}

    return result

if __name__ == "__main__":
    kw_facilities()


