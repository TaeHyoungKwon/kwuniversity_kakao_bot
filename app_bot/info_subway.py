#광운대역 지하철

import requests
from bs4 import BeautifulSoup



def info_subway():

    api = 'http://swopenAPI.seoul.go.kr/api/subway/435156415a6b74683131396b51665744/xml/realtimeStationArrival/0/4/광운대' 

    response = requests.get(api)
    inf = BeautifulSoup(response.text, 'html.parser')


    if inf.find("message").text == "해당하는 데이터가 없습니다.":
        message = "현재는 운행 시간이 아닙니다.\n"
        result = {"text":message}
        return result

    else:

        inf_dict_down1 = {}
        inf_dict_down2 = {}
        inf_dict_up1 = {}
        inf_dict_up2 = {}

        up = False
        down = False

        for a in inf.find_all("row"):

            if a.find("subwayid").text == '1001' and a.find("updnline").text=="상행" and up == False:
                inf_dict_up1["st_name"] = a.find("statnnm").text
                inf_dict_up1["st_updnline"] = a.find("updnline").text
                inf_dict_up1["st_trainlinenm"] = a.find("trainlinenm").text.split("-")[0]
                inf_dict_up1["st_recptndt"] = a.find("recptndt").text
                inf_dict_up1["st_arvlmsg2"] = a.find("arvlmsg2").text

                up = True

            if a.find("subwayid").text == '1001' and a.find("updnline").text=="상행" and up == True:
               
                inf_dict_up2["st_updnline"] = a.find("updnline").text
                inf_dict_up2["st_trainlinenm"] = a.find("trainlinenm").text.split("-")[0]
                inf_dict_up2["st_arvlmsg2"] = a.find("arvlmsg2").text


            if a.find("subwayid").text == '1001' and a.find("updnline").text=="하행" and down == False:
                inf_dict_down1["st_updnline"] = a.find("updnline").text
                inf_dict_down1["st_trainlinenm"] = a.find("trainlinenm").text.split("-")[0]
                inf_dict_down1["st_arvlmsg2"] = a.find("arvlmsg2").text
                down = True


            if a.find("subwayid").text == '1001' and a.find("updnline").text=="하행" and down == True:
                inf_dict_down2["st_trainlinenm"] = a.find("trainlinenm").text.split("-")[0]
                inf_dict_down2["st_arvlmsg2"] = a.find("arvlmsg2").text



        msg_intro = "{}역 지하철 실시간 도착정보 입니다.\n\n".format(inf_dict_up1['st_name'])
        msg_time = "기준 시각 : {}\n\n".format(inf_dict_up1['st_recptndt'])
        msg_info_up = ("# {}\n{} - {}\n{} - {}\n\n".format(

                inf_dict_up1['st_updnline'], 
                inf_dict_up1['st_trainlinenm'], inf_dict_up1['st_arvlmsg2'], 
                inf_dict_up2['st_trainlinenm'],inf_dict_up2['st_arvlmsg2']
        )

                   )
        msg_info_down = ("# {}\n{} - {}\n{} - {}\n\n".format(

                inf_dict_down1['st_updnline'], 
                inf_dict_down1['st_trainlinenm'], inf_dict_down1['st_arvlmsg2'], 
                inf_dict_down2['st_trainlinenm'],inf_dict_down2['st_arvlmsg2'])

                   )

        message = msg_intro + msg_time + msg_info_up + msg_info_down

        result = {"text":message}
        
        
        return result

if __name__ == "__main__":

    info_subway()
