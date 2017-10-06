from django.http import HttpResponse
from django.template import loader
import requests


def index(request):
    r = requests.get('http://exp-api:8000/lottery-pane')
    lotteries_list = r.json()
    template = loader.get_template('web_app/index.html')
    context = {
        'lotteries_list': lotteries_list,
    }
    return HttpResponse(template.render(context, request))


def lotteryDetail(request, pk):
    r = requests.get('http://exp-api:8000/lottery-detail/' + pk)
    lottery_details = r.json()
    template = loader.get_template('web_app/lottery' + pk + '.html')
    context = {
        'lotteries_details': lottery_details,
    }
    return HttpResponse(template.render(context, request))


def cards(request):
    r = requests.get('http://exp-api:8000/card-pane')
    cards_list = r.json()
    template = loader.get_template('web_app/cards.html')
    context = {
        'cards_list': cards_list,
    }
    return HttpResponse(template.render(context, request))


def cardDetail(request, pk):
    r = requests.get('http://exp-api:8000/card-detail/' + pk)
    card_details = r.json()
    template = loader.get_template('web_app/card' + pk + '.html')
    context = {
        'card_details': card_details,
    }
    return HttpResponse(template.render(context, request))
