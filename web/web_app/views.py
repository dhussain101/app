from django.shortcuts import render
import requests


def index(request):
    r = requests.get('http://exp-api:8000/lottery-pane')
    lotteries_list = r.json()
    context = {
        'lotteries_list': lotteries_list,
    }
    return render(request, 'index.html', context)
