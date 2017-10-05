from django.http import HttpResponse
from django.template import loader


def index(request):
    # FIXME: this should query the experience API, but for now it is left blank
    lotteries_list = []
    template = loader.get_template('web_app/index.html')
    context = {
        'lotteries_list': lotteries_list,
    }
    return HttpResponse(template.render(context, request))
