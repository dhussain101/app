from django.http import JsonResponse
import requests
MODEL_URL = 'http://models-api:8000'


def get(*paths):
    """
    Performs a get request on the models API layer.
    For example, get('hello', 'world') will query http://models-api:8000/hello/world
    :param paths: each sub-path entered as a separate argument
    :return: JSON response from models API
    """
    return requests.get(MODEL_URL + ''.join('/{}' for _ in range(len(paths))).format(*paths)).json()


def lottery_pane(request):
    response = get('lotteries')
    return JsonResponse(response, safe=False)


def card_pane(request):
    response = get('cards')
    return JsonResponse(response, safe=False)


def lottery_detail(request, pk):
    response = get('lotteries', pk)
    if response:
        response['participants'] = list(map(
            lambda user: get('users', user),
            response['participants']))
    return JsonResponse(response, safe=False)


def card_detail(request, pk):
    response = get('cards', pk)
    if response:
        response['game'] = get('games', response['game'])
    return JsonResponse(response, safe=False)
