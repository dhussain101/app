from json import JSONDecodeError
from django.http import JsonResponse, HttpResponseBadRequest
from requests import get
from .views import MODEL_URL


def collect(request, params):
    acc = {}
    for param in params:
        p = request.GET.get(param, None)
        if not p:
            return None
        acc[param] = p
    return acc


def pass_through(request, model_api, params):
    params = collect(request, params)
    if params is None:
        # missing a required parameter
        return HttpResponseBadRequest()

    response = get(MODEL_URL + '/' + model_api, params=params)
    try:
        return JsonResponse(response.json(), safe=False, status=response.status_code)
    except JSONDecodeError:
        return HttpResponseBadRequest()


def authenticate(request):
    return pass_through(request, 'authenticate', ['authenticator'])


def login(request):
    return pass_through(request, 'login', ['username', 'password'])


def logout(request):
    return pass_through(request, 'logout', ['authenticator'])


def register(request):
    return pass_through(request, 'register', ['username', 'password', 'first_name', 'last_name', 'birthday'])
