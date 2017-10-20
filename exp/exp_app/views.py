from json import JSONDecodeError
from django.http import JsonResponse
import requests
MODEL_URL = 'http://models-api:8000'


def get(*paths, params={}):
    """
    Performs a get request on the models API layer.
    For example, get('hello', 'world') will query http://models-api:8000/hello/world
    :param paths: each sub-path entered as a separate argument
    :param params: URL parameters
    :return: JSON response from models API
    """
    try:
        return requests.get(MODEL_URL + ''.join('/{}' for _ in range(len(paths))).format(*paths), params=params).json()
    except JSONDecodeError:
        return {}


def lottery_pane(request):
    response = get('lotteries')['results']
    return JsonResponse(response, safe=False)


def card_pane(request):
    response = get('cards')['results']
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
