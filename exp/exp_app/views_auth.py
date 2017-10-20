from .views import get
from django.http import HttpResponseBadRequest


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
        return HttpResponseBadRequest

    return get(model_api, params=params)


def authenticate(request):
    return pass_through(request, 'authenticate', ['authenticator'])


def login(request):
    return pass_through(request, 'login', ['username', 'password'])


def logout(request):
    return pass_through(request, 'logout', ['authenticator'])


def register(request):
    return pass_through(request, 'register', ['username', 'password', 'first_name', 'last_name', 'birthday'])
