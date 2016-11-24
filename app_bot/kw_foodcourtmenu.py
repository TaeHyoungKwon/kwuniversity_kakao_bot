import requests
from bs4 import BeautifulSoup
import json

#푸드코트 메뉴
import re

def kw_foodcourtmenu(menu):

    if menu == "중식":
        url = "http://foodcourt.kw.ac.kr/menu/menu_chinesefood.html"

    elif menu == "한식":
        url = "http://foodcourt.kw.ac.kr/menu/menu_university.html"

        pass
    elif menu == "철판":
        url = "http://foodcourt.kw.ac.kr/menu/menu_grilledfood.html"

        pass
    elif menu == "일식":
        url = "http://foodcourt.kw.ac.kr/menu/menu_westernfood.html"

        pass
    elif menu == "쌀국수":
        url = "http://foodcourt.kw.ac.kr/menu/menu_snackfood.html"


                        
    message ="'" +  menu + "'" + "메뉴 정보 입니다.!\n\n"

    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    response = requests.get(url, headers={"USER-AGENT":u_a})
    soup = BeautifulSoup(response.text, 'html.parser')

    table_soup = soup.find("table",{"class" : "line00"})
    td = soup.find_all("td",{"class":"board-td6"})
    
    cnt = 0
    for menu in td:
        menu = re.sub('<[^<]+?>', '', str(menu))
        message += menu + "\n"
        cnt += 1
        if cnt % 3 ==0:
            message += "\n"
    cnt = 0
    result = {"text":message}

    return result

if __name__ == "__main__":
    kw_foodcourtmenu()


