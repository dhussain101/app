from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    r = requests.get('http://exp-api:8000/lottery-pane')
    lottery_list = r.json()
    context = {
        'lottery_list': lottery_list,
        'title': 'Home',
    }
    return render(request, 'index.html', context)


def lottery_detail(request, pk):
    r = requests.get('http://exp-api:8000/lottery-detail/' + pk)
    lottery_details = r.json()
    return render(request, 'lottery-detail.html', lottery_details)


def cards(request):
    r = requests.get('http://exp-api:8000/card-pane')
    cards_list = r.json()
    context = {
        'card_list': cards_list,
        'title': 'Cards',
    }
    return render(request, 'cards.html', context)


def card_detail(request, pk):
    r = requests.get('http://exp-api:8000/card-detail/' + pk)
    card_details = r.json()
    return render(request, 'card-detail.html', card_details)


def bad_url(request):
    return render(request, '404.html')
