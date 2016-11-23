import requests
from bs4 import BeautifulSoup
import json
import re
import time

#장소예약확인
def uc_reservation(num):
    payload = {
        'login_type' : '2',
        'redirect_url':"http://info.kw.ac.kr/webnote/rent_place/rent_index.php",
        'layout_opt' : "",
        'gubun_code' : '11',
        'member_no': '2010720059',
        'password': '5',

    }

    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    request_url = "https://info.kw.ac.kr/webnote/login/login_proc.php"

    with requests.Session() as s:
        s.post(request_url,headers={'User-Agent' : u_a,}  ,data=payload)
        s = s.get("http://info.kw.ac.kr/webnote/rent_place/rent_all_list.php",headers={'User-Agent':u_a})

    soup = BeautifulSoup(s.content, 'html.parser', from_encoding='utf-8')
    td_soup = soup.find_all("td")
    
    
    football_msg = ""
    cnt = 2

    for li in td_soup[2:]:

        if num in li :
            football_msg +=str(td_soup[cnt-4])+"\n" +  str(td_soup[cnt-3]) +" - " + str(td_soup[cnt-2]) + "\n" + str(td_soup[cnt-1]) + " - "+ str(td_soup[cnt+1]) + "\n\n"
        else:
            print("No number")
            
        cnt +=1    
        
    football_msg = re.sub('<[^<]+?>', '', str(football_msg))
    result = {"text":football_msg}
    return result
    
if __name__ == "__main__":
    start = time.time()
    uc_reservation("1234")
    end = time.time() - start
    print(end)

