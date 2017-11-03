from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from elasticsearch import Elasticsearch

from . import get, forward_post


def lottery_pane(_):
    response = get('lotteries')['results']
    return JsonResponse(response, safe=False)


def card_pane(_):
    response = get('cards')['results']
    return JsonResponse(response, safe=False)


def game_pane(_):
    response = get('games')['results']
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


def search(request):
    # pk = {'query': 'awesome lottery', 'size': 5, 'index':'lottery_index'}
    pk = {
        'fields': request.GET['fields'],
        'index': request.GET['indices'],
        'query': request.GET['q'],
        'size': request.GET['size'],
    }

    # temporary hard-coded test pk
    # pk = {'query': 'pokemon', 'size': 5, 'index': 'lottery_index'}
    try:
        es = Elasticsearch(['es'])
        search_result = es.search(index=pk['index'],
                                  body={'query': {'query_string': {'query': pk['query']}}, 'size': pk['size']})
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return JsonResponse({'error': message})
    return JsonResponse(search_result['hits']['hits'], safe=False)


@csrf_exempt
def lottery_create(request):
    return forward_post(request, 'lotteries', ['title', 'description', 'start_time', 'end_time'])


@csrf_exempt
def card_create(request):
    return forward_post(request, 'cards', ['game', 'lottery', 'title', 'description', 'value'])
