from django.shortcuts import render
import requests


def index(request):
    r = requests.get('http://exp-api:8000/lottery-pane')
    lotteries_list = r.json()
    context = {
        'lotteries_list': lotteries_list,
    }
    return render(request, 'index.html', context)


def lotteryDetail(request, pk):
    print(pk)
    r = requests.get('http://exp-api:8000/lottery-detail/' + pk)
    lottery_details = r.json()
    context = {
        'lotteries_details': lottery_details,
    }
    return render(request, 'lottery-detail.html', context)


def cards(request):
    r = requests.get('http://exp-api:8000/card-pane')
    cards_list = r.json()
    context = {
        'cards_list': cards_list,
    }
    return render(request, 'cards.html', context)


def cardDetail(request, pk):
    r = requests.get('http://exp-api:8000/card-detail/' + pk)
    card_details = r.json()
    context = {
        'card_details': card_details,
    }
    return render(request, 'card-detail.html', context)
