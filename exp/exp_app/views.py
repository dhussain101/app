from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import get, forward_post


def lottery_pane(_):
    response = get('lotteries')['results']
    return JsonResponse(response, safe=False)


def card_pane(_):
    response = get('cards')['results']
    return JsonResponse(response, safe=False)


def lottery_detail(_, pk):
    response = get('lotteries', pk)
    if response:
        response['participants'] = list(map(
            lambda user: get('users', user),
            response['participants']))
    return JsonResponse(response, safe=False)


def card_detail(_, pk):
    response = get('cards', pk)
    if response:
        response['game'] = get('games', response['game'])
    return JsonResponse(response, safe=False)


@csrf_exempt
def lottery_create(request):
    return forward_post(request, 'lotteries', ['title', 'description', 'start_time', 'end_time'])
