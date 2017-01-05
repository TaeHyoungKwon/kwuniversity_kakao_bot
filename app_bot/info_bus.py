import requests
import requests_cache
from bs4 import BeautifulSoup
import time

def info_bus(busstop):

    requests_cache.install_cache('demo_cache',expire_after=30)
    start = time.time()
    if busstop =="광운대":
        api_1 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=vuKP%2B0q5LtoAn%2BTiURtQJFJwxEpHibYAJdYckWAp1NeXGb4PhnZp%2FJJGdTAaAdVQlnYwZCmUhv22IK9rOXRUog%3D%3D&arsId=11285&numOfRows=5&pageSize=999&pageNo=1&startPage=1"
        api_2 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=vuKP%2B0q5LtoAn%2BTiURtQJFJwxEpHibYAJdYckWAp1NeXGb4PhnZp%2FJJGdTAaAdVQlnYwZCmUhv22IK9rOXRUog%3D%3D&arsId=11335&numOfRows=5&pageSize=999&pageNo=1&startPage=1"
    
    elif busstop =="석계":
        api_1 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=vuKP%2B0q5LtoAn%2BTiURtQJFJwxEpHibYAJdYckWAp1NeXGb4PhnZp%2FJJGdTAaAdVQlnYwZCmUhv22IK9rOXRUog%3D%3D&arsId=11457&numOfRows=5&pageSize=999&pageNo=1&startPage=1"
        api_2 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=vuKP%2B0q5LtoAn%2BTiURtQJFJwxEpHibYAJdYckWAp1NeXGb4PhnZp%2FJJGdTAaAdVQlnYwZCmUhv22IK9rOXRUog%3D%3D&arsId=11594&numOfRows=5&pageSize=999&pageNo=1&startPage=1"
    
    elif busstop == "월계삼거리":
        api_1 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=vuKP%2B0q5LtoAn%2BTiURtQJFJwxEpHibYAJdYckWAp1NeXGb4PhnZp%2FJJGdTAaAdVQlnYwZCmUhv22IK9rOXRUog%3D%3D&arsId=11286&numOfRows=5&pageSize=999&pageNo=1&startPage=1"
        api_2 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=vuKP%2B0q5LtoAn%2BTiURtQJFJwxEpHibYAJdYckWAp1NeXGb4PhnZp%2FJJGdTAaAdVQlnYwZCmUhv22IK9rOXRUog%3D%3D&arsId=11336&numOfRows=5&pageSize=999&pageNo=1&startPage=1"

    else:
        message = "잘못된 단어를 입력했습니다. 메뉴얼에 나온 그대로 다시 입력해주세요."
        result = {"text":message}
        return result

    cnt =0
    try:
        retry = True
        while retry:

            try:
                cnt+=1
                start1 = time.time()

                response1 = requests.get(api_1,timeout=1)
                end1 = time.time() - start1

                print("end1 {}".format(end1))
                
                start2 = time.time()
                response2 = requests.get(api_2,timeout=1)
                end2 = time.time() -start2
                print("end2 {}".format(end2))

                retry = False
                print(cnt)


            except requests.exceptions.Timeout:
                print("error")

        

            inf1 = BeautifulSoup(response1.text, 'html.parser')
            inf2 = BeautifulSoup(response2.text, 'html.parser')

            inf_dict1 = {}
            inf_dict2 = {}

        for a in inf1.find_all("itemlist"):

            if a.find("busrouteid").text == "100100043":
                inf_dict1["bus_1"] = "261"
                inf_dict1["arrmsgsec1_1"] = a.find("arrmsgsec1").text
                inf_dict1["arrmsgsec2_1"] = a.find("arrmsgsec2").text

            elif a.find("busrouteid").text == "100100152":
                inf_dict1["bus_2"] = "1137"
                inf_dict1["arrmsgsec1_2"] = a.find("arrmsgsec1").text
                inf_dict1["arrmsgsec2_2"] = a.find("arrmsgsec2").text

            elif a.find("busrouteid").text == "100100130":
                inf_dict1["bus_3"] = "1017"
                inf_dict1["arrmsgsec1_3"] = a.find("arrmsgsec1").text
                inf_dict1["arrmsgsec2_3"] = a.find("arrmsgsec2").text

        for a in inf2.find_all("itemlist"):

            if a.find("busrouteid").text == "100100043":
                inf_dict2["bus_1"] = "261"
                inf_dict2["arrmsgsec1_1"] = a.find("arrmsgsec1").text
                inf_dict2["arrmsgsec2_1"] = a.find("arrmsgsec2").text

            elif a.find("busrouteid").text == "100100152":
                inf_dict2["bus_2"] = "1137"
                inf_dict2["arrmsgsec1_2"] = a.find("arrmsgsec1").text
                inf_dict2["arrmsgsec2_2"] = a.find("arrmsgsec2").text

            elif a.find("busrouteid").text == "100100130":
                inf_dict2["bus_3"] = "1017"
                inf_dict2["arrmsgsec1_3"] = a.find("arrmsgsec1").text
                inf_dict2["arrmsgsec2_3"] = a.find("arrmsgsec2").text

            elif a.find("busrouteid").text == "100100155":
                inf_dict2["bus_4"] = "1140"
                inf_dict2["arrmsgsec1_4"] = a.find("arrmsgsec1").text
                inf_dict2["arrmsgsec2_4"] = a.find("arrmsgsec2").text

            elif a.find("busrouteid").text == "110900006":
                inf_dict2["bus_5"] = "노원09"
                inf_dict2["arrmsgsec1_5"] = a.find("arrmsgsec1").text
                inf_dict2["arrmsgsec2_5"] = a.find("arrmsgsec2").text


        if  busstop == "석계":
            msg_top =  "실시간 버스 도착정보 입니다.\n\n\n석계역(쥬시 앞) -> 광운대 방향\n\n"
            msg_bus1 ="* {}\n{}\n{}\n\n\n".format(inf_dict1['bus_1'], inf_dict1['arrmsgsec1_1'], inf_dict1['arrmsgsec2_1'])

            msg_middle =  "석계(이디야커피 앞) -> 광운대 방향\n\n"
            msg_bus2 ="* {}\n{}\n{}\n\n\n".format(inf_dict2['bus_5'],inf_dict2['arrmsgsec1_5'],inf_dict2['arrmsgsec2_5'])

            message = msg_top + msg_bus1 + msg_middle + msg_bus2


        elif busstop == "광운대":
            msg_top =  "실시간 버스 도착정보 입니다.\n\n\n광운대(신축 도서관 앞) -> 월계삼거리 방향\n\n"
            msg_bus1 ="* {}\n{}\n{}\n\n".format(inf_dict1['bus_1'], inf_dict1['arrmsgsec1_1'], inf_dict1['arrmsgsec2_1'])
            msg_bus2 ="* {}\n{}\n{}\n\n".format(inf_dict1['bus_2'], inf_dict1['arrmsgsec1_2'], inf_dict1['arrmsgsec2_2'])
            msg_bus3 ="* {}\n{}\n{}\n\n\n".format(inf_dict1['bus_3'], inf_dict1['arrmsgsec1_3'], inf_dict1['arrmsgsec2_3'])

            msg_middle =  "광운대 (동해문화예술관 앞)-> 광운공고, 장위동 방향\n\n"
            msg_bus4 ="* {}\n{}\n{}\n\n".format(inf_dict2['bus_1'],inf_dict2['arrmsgsec1_1'],inf_dict2['arrmsgsec2_1'])
            msg_bus5 ="* {}\n{}\n{}\n\n".format(inf_dict2['bus_2'],inf_dict2['arrmsgsec1_2'],inf_dict2['arrmsgsec2_2'])
            msg_bus6 ="* {}\n{}\n{}\n\n".format(inf_dict2['bus_3'],inf_dict2['arrmsgsec1_3'],inf_dict2['arrmsgsec2_3'])
            msg_bus7 ="* {}\n{}\n{}\n\n".format(inf_dict2['bus_4'],inf_dict2['arrmsgsec1_4'],inf_dict2['arrmsgsec2_4'])   

            message = msg_top + msg_bus1 +  msg_bus2 +  msg_bus3  + msg_middle + msg_bus4 +  msg_bus5 +  msg_bus6 +  msg_bus7
        
        elif busstop == "월계삼거리":
            msg_top =  "실시간 버스 도착정보 입니다.\n\n\n월계삼거리 -> 월계 방향 or 광운대역 방향\n\n"
            msg_bus1 ="* {}\n{}\n{}\n\n".format(inf_dict1['bus_1'], inf_dict1['arrmsgsec1_1'], inf_dict1['arrmsgsec2_1'])
            msg_bus2 ="* {}\n{}\n{}\n\n".format(inf_dict1['bus_2'], inf_dict1['arrmsgsec1_2'], inf_dict1['arrmsgsec2_2'])
            msg_bus3 ="* {}\n{}\n{}\n\n\n".format(inf_dict1['bus_3'], inf_dict1['arrmsgsec1_3'], inf_dict1['arrmsgsec2_3'])

            msg_middle =  "월계삼거리(에뽕버거 앞) -> 광운대 정문 방향  \n\n"
            msg_bus4 ="* {}\n{}\n{}\n\n".format(inf_dict2['bus_1'],inf_dict2['arrmsgsec1_1'],inf_dict2['arrmsgsec2_1'])
            msg_bus5 ="* {}\n{}\n{}\n\n".format(inf_dict2['bus_2'],inf_dict2['arrmsgsec1_2'],inf_dict2['arrmsgsec2_2'])
            msg_bus6 ="* {}\n{}\n{}\n\n".format(inf_dict2['bus_3'],inf_dict2['arrmsgsec1_3'],inf_dict2['arrmsgsec2_3'])
            msg_bus7 ="* {}\n{}\n{}\n\n".format(inf_dict2['bus_4'],inf_dict2['arrmsgsec1_4'],inf_dict2['arrmsgsec2_4'])   
            
            
            message = msg_top + msg_bus1 +  msg_bus2 +  msg_bus3  + msg_middle + msg_bus4 +  msg_bus5 +  msg_bus6 +  msg_bus7

        result = {"text":message}
        end = time.time() - start
        print(end)

        return result
    
    except (requests.exceptions.ConnectionError,OSError) as e:
        return e

        

if __name__ == "__main__":
    info_bus("광운대")
