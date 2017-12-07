from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from elasticsearch import Elasticsearch

from . import get, forward_post, kafka_add


def lottery_pane(_):
    response = get('lotteries')['results']
    return JsonResponse(response, safe=False)


def card_pane(_):
    response = get('cards')['results']
    return JsonResponse(response, safe=False)


def game_pane(_):
    response = get('games')['results']
    return JsonResponse(response, safe=False)


def lottery_detail(request, pk):
    lottery_details = get('lotteries', pk)
    if not lottery_details:
        return HttpResponseBadRequest()

    # once we've verified the user is logged in
    # send page view data to kafka consumer
    user_id = request.GET['user_id']
    if user_id != '':
        kafka_add('new_view', (user_id, pk))

    lottery_details['participants'] = list(map(
        lambda user: get('users', user),
        lottery_details['participants'],
    ))

    recommendations = get('recommendations', pk)
    # it's okay if there are no recommendations
    if recommendations and 'recommended' in recommendations:
        lottery_details['recommendations'] = list(map(
            lambda lottery: get('lotteries', lottery),
            recommendations['recommended'],
        ))
    return JsonResponse(lottery_details, safe=False)


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
        'sort': request.GET['sort'],
    }

    sort_type = [{'_score': {'order': 'desc'}}]
    if pk['sort'] == 'alphabetical':
        sort_type = [{'title': {'order': 'asc'}}]

    # temporary hard-coded test pk
    # pk = {'query': 'pokemon', 'size': 5, 'index': 'lottery_index'}
    try:
        es = Elasticsearch(['es'])
        search_result = es.search(index=pk['index'],
                                  body={'query': {'query': {
                                      'query_string': {'fields': pk['fields'].split(','), 'query': pk['query']}}},
                                        'size': pk['size'], 'sort': sort_type})
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


def lottery_recommendations(_, pk):
    response = get('recommendations', pk)
    if not response:
        return HttpResponseBadRequest()
    response['recommended'] = list(map(
        lambda lottery: get('lotteries', lottery),
        response['recommended'],
    ))
    return JsonResponse(response)
