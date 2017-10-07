from django.http import JsonResponse
import requests


def lottery_pane(request):
    r = requests.get('http://models-api:8000/lotteries')
    response = JsonResponse(r.json(), safe=False)
    return response


def card_pane(request):
    r = requests.get('http://models-api:8000/cards')
    response = JsonResponse(r.json(), safe=False)
    return response


def lottery_detail(request, pk):
    r = requests.get('http://models-api:8000/lotteries/' + pk)
    response = JsonResponse(r.json(), safe=False)
    return response


def card_detail(request, pk):
    r = requests.get('http://models-api:8000/cards/' + pk)
    response = JsonResponse(r.json(), safe=False)
    return response
