from django.http import HttpResponseRedirect
from django.urls import reverse
from .auth import render
from .auth.views import collect, add_errors
from .auth.decorators import login_required
from .forms import *
from . import get, post


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
    form = None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LotteryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            fields = ('title', 'description', 'start_time', 'end_time')
            # process the data in form.cleaned_data as required
            params = collect(form.cleaned_data, fields)
            if params is not None:
                # Send validated information to our experience layer
                response = post('lottery-create', data=params)
                if response.status_code == 201:
                    return HttpResponseRedirect(reverse('lotteries'))
                # invalid form so return to register page

    # if a GET (or any other method) we'll create a blank form
    if not form:
        form = LotteryForm()

    context = {
        'title': 'Create Lottery',
        'form': form,
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
