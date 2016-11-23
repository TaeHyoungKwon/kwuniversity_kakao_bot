import requests
from bs4 import BeautifulSoup
import json

#푸드코트 메뉴
import re

def kw_foodcourtmenu():
    url1 = "http://foodcourt.kw.ac.kr/menu/menu_chinesefood.html"
    url2 = "http://foodcourt.kw.ac.kr/menu/menu_university.html"
    url3 = "http://foodcourt.kw.ac.kr/menu/menu_grilledfood.html"
    url4 = "http://foodcourt.kw.ac.kr/menu/menu_westernfood.html"
    url5 = "http://foodcourt.kw.ac.kr/menu/menu_snackfood.html"
    
    message = ""
    for url in [url1,url2,url3,url4,url5]:
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


