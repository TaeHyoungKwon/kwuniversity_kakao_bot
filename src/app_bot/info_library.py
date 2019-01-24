import requests
from bs4 import BeautifulSoup
import re
import datetime


def info_library():

    url = "http://mobileid.kw.ac.kr/seatweb/domian5.asp"
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

    response = requests.get(url, headers={"USER-AGENT":u_a})
    soup= BeautifulSoup(response.content,'html.parser')

    td_soup = soup.find_all('td',attrs={"align" :"CENTER"})

    library = []

    for a in td_soup:
        library.append(re.sub('<[^<]+?>', '', str(a)))

    now = datetime.datetime.now()
    nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')

    intro = "*** 광운대 중앙도서관 실시간 좌석 정보 ***\n\n"

    nowDateTime =" 현재 시각 '{}' 입니다.\n\n".format(str(nowDateTime))
    row1 = " 열람실 명   / 전  체 / 사용 중 / 남은좌석 /이용률 \n\n"
    row2 = "{}  /  {:>3}  / {:>3} / {:>3} / {:.2f} %\n".format(library[0],library[1],library[2],library[3],int(library[2])/int(library[1]) * 100)
    row3 = "{}  /  {:>3}  / {:>3} / {:>3} / {:.2f} %\n".format(library[4],library[5],library[6],library[7],float(float(library[6])/float(library[5]) * 100))
    row4 = "{}  /  {:>3}  / {:>3} / {:>3} / {:.2f} %\n\n".format(library[8],library[9],library[10],library[11],int(library[10])/int(library[9]) * 100)
    outro = "*** 본 정보는 1분 단위로 갱신 됩니다. ***\n\n"
    end = "*** 상세 현황 ***\n\n1열람실 : http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no=1\n2열람실 : http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no=2\n3열람실 : http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no=1\n\n"

    message =   intro + nowDateTime + row1 + row2 + row3 + row4 + end + outro
    result = {"text":message}

    return result

if __name__ == "__main__":
    info_library()
