from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import get, forward_post
from elasticsearch import Elasticsearch



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


def search(_, pk):
    # pk = {'query': 'awesome lottery', 'size': 5, 'index':'lottery_index'}
    es = Elasticsearch(['es'])
    search_result = es.search(index=pk['index'], body={'query': {'query_string': {'query': pk['query']}}, 'size': pk['size']})
    return JsonResponse(search_result['hits']['hits'])



@csrf_exempt
def lottery_create(request):
    return forward_post(request, 'lotteries', ['title', 'description', 'start_time', 'end_time'])
