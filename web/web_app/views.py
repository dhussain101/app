from .auth import get, render
from .forms import *


def index(request):
    lottery_list = get('lottery-pane')
    card_list = get('card-pane')
    context = {
        'lottery_list': lottery_list,
        'card_list': card_list,
        'title': 'Home',
    }
    return render(request, 'index.html', context)


def lotteries(request):
    lottery_list = get('lottery-pane')
    context = {
        'lottery_list': lottery_list,
        'title': 'Lotteries',
    }
    return render(request, 'lotteries.html', context)


def lottery_create(request):
    context = {
        'title': 'Create Lottery',
        'form': LotteryForm,
    }
    return render(request, 'lottery-create.html', context)


def lottery_detail(request, pk):
    lottery_details = get('lottery-detail', pk)
    return render(request, 'lottery-detail.html', lottery_details)


def cards(request):
    card_list = get('card-pane')
    context = {
        'card_list': card_list,
        'title': 'Cards',
    }
    return render(request, 'cards.html', context)


def card_detail(request, pk):
    card_details = get('card-detail', pk)
    return render(request, 'card-detail.html', card_details)


def bad_url(request):
    return render(request, '404.html')
