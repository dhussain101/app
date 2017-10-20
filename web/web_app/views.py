from django.http import HttpResponseRedirect
from django.urls import reverse
from .auth import get, render
from .auth.decorators import login_required
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


@login_required
def lottery_create(request):
    context = {
        'title': 'Create Lottery',
        'form': LotteryForm,
    }
    return render(request, 'lottery-create.html', context)


def lottery_detail(request, pk):
    lottery_details = get('lottery-detail', pk)
    if not lottery_details:
        return HttpResponseRedirect(reverse('lotteries'))
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
    if not card_details:
        return HttpResponseRedirect(reverse('cards'))
    return render(request, 'card-detail.html', card_details)


def bad_url(request):
    return render(request, '404.html', {})
