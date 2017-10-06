from django.http import HttpResponse
from django.template import loader
import requests


def index(request):
    r = requests.get('http://exp-api:8000/lottery-pane')
    print(r)
    lotteries_list = r.json()
    template = loader.get_template('web_app/index.html')
    context = {
        'lotteries_list': lotteries_list,
    }
    return HttpResponse(template.render(context, request))
