from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import requests


def lotteryPane(request):
    r = requests.get('http://models-api:8000/lottery')
    response = JsonResponse(r.json(), safe=False)
    return response
