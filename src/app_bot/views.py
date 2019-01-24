# views.py 리팩토링 완료

import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import SearchWord
from .utils import (
    kw_notice,
    kw_jobinfo,
    kw_schedule,
    kw_facilities,
    kw_hamjimaru,
    kw_foodcourtmenu,
    info_subway,
    info_bus,
    info_weather,
    info_library,
    uc_reservation,
    keyword,
    service
)


@csrf_exempt
def message(request):

    if request.method == "POST":
        content = json.loads(request.body.decode('utf-8'))
        keyword = content['content']

        if keyword == "@메뉴얼":
            result = keyword.menual_text

        elif keyword == "@공지사항":
            result = kw_notice.kw_notice()

        elif keyword == "@취업정보":
            result = kw_jobinfo.kw_jobinfo()

        elif keyword == "@학사일정":
            result = kw_schedule.kw_schedule()

        elif keyword == "@편의시설":
            result = kw_facilities.kw_facilities()

        elif keyword == "@학식식단":
            result = kw_hamjimaru.kw_hamjimaru()

        elif keyword == "@지하철":
            result = info_subway.info_subway()

        elif keyword == "@날씨":
            result = info_weather.info_weather()

        elif keyword == "@열람실":
            result = info_library.info_library()

        elif "푸코메뉴" in keyword:
            menu = service.split_at(content['content'])
            result = kw_foodcourtmenu.kw_foodcourtmenu(menu)

        elif "예약확인" in keyword:
            num = service.split_at(content['content'])
            result = uc_reservation.uc_reservation(num)

        elif "버스" in keyword:
            busstop = service.split_at(content['content'])
            result = info_bus.info_bus(busstop)

        else:
            result = error_text

        obj = SearchWord.objects.create(word=keyword)
        obj.save()
        textMessage = {"message": result}

        return JsonResponse(textMessage)


def key(request):
    if request.method == "GET":

        keyList = ["@메뉴얼"]
        keyboardList = {'type': 'buttons', 'buttons': keyList}

        return JsonResponse(keyboardList)


@csrf_exempt
def friend(request):
    if request.method == "DELETE":
        response = HttpResponse()
        return response

    elif request.method == "POST":
        response = HttpResponse()

        return response


@csrf_exempt
def chat_room(request):

    if request.method == "DELETE":
        response = HttpResponse()

    return response


def error404(request):
    return HttpResponse("No!")
