import requests
from bs4 import BeautifulSoup

def info_weather():
    api = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1135056000"
    response = requests.get(api)
    inf = BeautifulSoup(response.text, 'html.parser')


    weather = inf.find_all("data")

    result = []
    result_msg = ''

    for a in weather:
        seq = {}    
        if a.find("day").text == "0" or a.find("day").text == "1":
            seq['tmx'] = a.find("tmx").text
            seq['tmn'] = a.find("tmn").text
            seq['day'] = a.find("day").text
            seq['hour'] = a.find('hour').text
            seq['temp'] = a.find('temp').text
            seq['wfkor'] = a.find('wfkor').text
            seq['pop'] = a.find('pop').text
            result.append(seq)

    check_0 = False
    check_1 = False


    for a in result:
        if a['day'] == '0' and check_0 == False:
            msg ="\n*** 현재 시간 기준 금일 날씨 정보***\n(시간 / 온도 / 날씨)\n\n"
            check_0 = True
            result_msg += msg

        if a['day'] == '1' and check_1 == False:
            msg ="\n\n*** 현재 시간 기준 익일 날씨 정보***\n(시간 / 온도 / 날씨)\n\n"
            check_1 = True
            result_msg += msg

        msg = "{}시 / {}도 / {}\n".format(a['hour'],a['temp'],a['wfkor'])
        result_msg += msg

    result_msg = "광운대학교(월계1동) 날씨 정보 입니다.\n" + "기준 시각 : {}\n".format(inf.find("pubdate").text) +result_msg

    if "비" in result_msg:
        result_msg += "\n비가 올 수도 있으니, 우산을 준비하세요!"

    else:
        result_msg +="\n비 예보가 없습니다. 감사합니다!"
        
    res = {"text":result_msg}
    return res


if __name__ == "__main__":
    info_weather()
