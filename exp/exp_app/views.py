from django.http import JsonResponse
import requests


def lotteryPane(request):
    r = requests.get('http://models-api:8000/lotteries')
    response = JsonResponse(r.json(), safe=False)
    return response


def cardPane(request):
    r = requests.get('http://models-api:8000/cards')
    response = JsonResponse(r.json(), safe=False)
    return response


def lotteryDetail(request, pk):
    r = requests.get('http://models-api:8000/lotteries/' + pk)
    response = JsonResponse(r.json(), safe=False)
    return response


def cardDetail(request, pk):
    r = requests.get('http://models-api:8000/cards/' + pk)
    response = JsonResponse(r.json(), safe=False)
    return response
