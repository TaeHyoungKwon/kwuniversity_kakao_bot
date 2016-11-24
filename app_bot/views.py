from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from .kw_notice import kw_notice
from .kw_jobinfo import kw_jobinfo
from .kw_schedule import kw_schedule
from .kw_facilities import kw_facilities
from .kw_hamjimaru import kw_hamjimaru
from .kw_foodcourtmenu import kw_foodcourtmenu

from .uc_reservation import *

@csrf_exempt
def message(request):

    if request.method == "POST":

        content = json.loads(request.body.decode('utf-8'))
        
        if content['content'] == "@메뉴얼":
            textContent = { "text" : ('''안녕하세요 '광운대알림봇' 입니다.\n
##### 메뉴얼 보기 #####\n
- @메뉴얼\n= 해당 메세지를 다시 볼 수 있습니다.\n
##### 광운대 정보  #####\n
- @공지사항\n= 학교 공지사항 상위 30개를 보여줍니다.\n
- @취업정보\n= 학교 홈페이지 상의  취업정보 게시판을 보여줍니다.\n
- @학사일정\n= 학교 홈페이지 상의 학사일정을 보여줍니다.\n
- @편의시설\n= 학교 편의시설에 대한 정보를 보여줍니다.\n
- @학식식단\n= 함지마루 금주 식단을 보여줍니다.\n
-'KEYWORD'@푸코메뉴\n= KEYWORD = (중식,한식,일식,쌀국수) KEYWORD에 해당하는 메뉴와 가격을 보여줍니다.\n
ex) 한식@푸코메뉴 , 중식@푸코메뉴 ... 이렇게 치시면 됩니다.
##### 편의 기능 #####\n
- 확인번호@예약확인\n= 확인번호(예약자 폰번호 뒷자리)로 풋살장,학식,농구장 예약을 확인 할 수 있습니다.\n
ex)확인번호가 '1234' 일 경우, 1234@예약확인 이라고 치시면 됩니다.''')}
                                         

        elif content['content'] == "@공지사항":
            textContent = kw_notice()

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
         

        else:
            textContent = {"text":"잘못 누르셨습니다. 욕설및 도배는 자제해주세요.."}

        textMessage = {"message":textContent}
        return JsonResponse(textMessage)
"""
def initial_message(request):

   return JsonResponse(initial_message)
"""

    

def key(request):
    
    keyList = ["@메뉴얼"]
    keyboardList = {'type':'buttons', 'buttons': keyList}
    
   # textContent = { "text" : '''안녕하세요 광운대학교 풍물굿패 연합 봇 입니다.\n1. !소개\n= 광풍연 소개를 보실 수 있습니다.\n\n2. !홍보영상= 광풍연 홍보영상을 보실 수 있습니다.\n\n3. 각 월 마다, 광풍연 행사에 대해서 보실 수 있습니다.'''}
   # textMessage = {"type":"text","message" : textContent}
    
    return JsonResponse(keyboardList)

@csrf_exempt
def friend(request):
    content = json.loads(request.body.decode('utf-8'))
    content = content['user_key']
    response = HttpResponse("Ok!")

    return response

@csrf_exempt
def chat_room(request):
    print("chat_room")
    content = json.loads(request.body.decode('utf-8'))
    print(content)
    response = HttpResponse("Ok!")

    return response


