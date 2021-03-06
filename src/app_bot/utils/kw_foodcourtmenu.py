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

    elif menu == "철판":
        url = "http://foodcourt.kw.ac.kr/menu/menu_grilledfood.html"

    elif menu == "일식":
        url = "http://foodcourt.kw.ac.kr/menu/menu_westernfood.html"

    elif menu == "쌀국수":
        url = "http://foodcourt.kw.ac.kr/menu/menu_snackfood.html"
    else:
        text ="해당 {} 는 올바르지 않은 키워드 입니다.\n".format(menu)
        result = {"text":message}
        return result



                        
    message ="'" +  menu + "'" + "메뉴 정보 입니다.!(학생요금 / 일반요금)\n\n"

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


