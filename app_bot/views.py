from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from django.views.decorators.csrf import csrf_exempt

from .models import SearchWord

from .kw_notice import kw_notice
from .kw_jobinfo import kw_jobinfo
from .kw_schedule import kw_schedule
from .kw_facilities import kw_facilities
from .kw_hamjimaru import kw_hamjimaru
from .kw_foodcourtmenu import kw_foodcourtmenu

from .uc_reservation import *
from .info_subway import info_subway
from .info_bus import info_bus
from .info_weather import info_weather

from .msg_count import msg_count

import datetime

@csrf_exempt
def message(request):
    
    if request.method == "POST":

        message_button_check = False
        message_button = {}
        result = {}

        content = json.loads(request.body.decode('utf-8'))
        if content['content'] == "@메뉴얼":
            textContent = { "text" : ('''안녕하세요 '광운대알림봇' 입니다.\n
##### 메뉴얼 보기 #####\n
- @메뉴얼\n= 해당 메세지를 다시 볼 수 있습니다.\n
##### 광운대 정보  #####\n
- @공지사항\n= 학교 공지사항 상위 25개를 보여줍니다.\n
- @취업정보\n= 학교 홈페이지 상의  취업정보 게시판을 보여줍니다.\n
- @학사일정\n= 학교 홈페이지 상의 학사일정을 보여줍니다.\n
- @편의시설\n= 학교 편의시설에 대한 정보를 보여줍니다.\n
- @학식식단\n= 함지마루 금주 식단을 보여줍니다.\n
- KEYWORD@푸코메뉴\n= KEYWORD에 해당하는 메뉴와 가격을 보여줍니다.\nKEYWORD : (중식,한식,일식,쌀국수)\nex) 한식@푸코메뉴 , 중식@푸코메뉴,....\n
##### 편의 기능 #####\n
- 확인번호@예약확인\n= 확인번호(예약자 폰번호 뒷자리)로 풋살장,학식,농구장 예약을 확인 할 수 있습니다.\nex)확인번호가 '1234' 일 경우, 1234@예약확인 이라고 치시면 됩니다.\n
- @지하철\n= 광운대역 실시간 도착정보를 전송합니다.\n
- KEYWORD@버스\n= 광운대 주변, 석계역 주변 실시간 버스 도착정보를 전송합니다.\nKEYWORD : (광운대,석계,월계삼거리)\nex) 광운대@버스 , 석계@버스\n

''')}
                                         

        elif content['content'] == "@공지사항":
             
            text = kw_notice()
            
            message_button['label'] = "공지사항 보기"
            message_button['url'] = "http://www.kw.ac.kr/ko/life/notice.do"

            result['text'] = text
            result['message_button'] = message_button

            textContent = result

            message_button_check = True

        elif content['content'] =="@취업정보":
            textContent = kw_jobinfo()   
                   
        elif content['content'] == "@학사일정":
            textContent = kw_schedule()

        elif content['content'] == "@편의시설":
            textContent = kw_facilities()

        elif content['content'] == "@학식식단":
            textContent = kw_hamjimaru()

        elif "푸코메뉴" in content['content']:

            menu = content['content']

            menu = menu.split("@")[0]

            textContent = kw_foodcourtmenu(menu)

        elif "예약확인" in content['content']:
            num = content['content']

            num = num.split("@")[0]

            textContent = uc_reservation(num)

        elif content['content'] == "@지하철":
            textContent = info_subway()

        elif "버스" in content['content']:
            busstop = content['content']

            busstop = busstop.split("@")[0]

            textContent = info_bus(busstop)

        elif content['content'] == "@몇건":
            textContent = msg_count()
        elif content['content'] == "@날씨":
            textContent = info_weather()
            
        else:
            textContent = {"text":"잘못 누르셨습니다. 욕설및 도배는 자제해주세요.."}
            
        k =  content['content']

        obj = SearchWord.objects.create(word=k)
        obj.save()

        textMessage = {"message":textContent}
                    
        return JsonResponse(textMessage)
"""
def initial_message(request):

   return JsonResponse(initial_message)
"""

    

def key(request):
    if request.method == "GET":
    
        keyList = ["@메뉴얼"]
        keyboardList = {'type':'buttons', 'buttons': keyList}
    
   # textContent = { "text" : '''안녕하세요 광운대학교 풍물굿패 연합 봇 입니다.\n1. !소개\n= 광풍연 소개를 보실 수 있습니다.\n\n2. !홍보영상= 광풍연 홍보영상을 보실 수 있습니다.\n\n3. 각 월 마다, 광풍연 행사에 대해서 보실 수 있습니다.'''}
   # textMessage = {"type":"text","message" : textContent}
    
        return JsonResponse(keyboardList)

@csrf_exempt
def friend(request):
    if request.method == "DELETE":
        response = HttpResponse()
        return response
    
    elif request.method =="POST":
        response = HttpResponse()

        return response

@csrf_exempt
def chat_room(request):
    
    if request.method =="DELETE":
        response = HttpResponse()

    return response

def error404(request):
    return HttpResponse("No!")
