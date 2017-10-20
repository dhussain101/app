from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from .models import Authenticator, Person


def collect(request, params):
    acc = {}
    for param in params:
        p = request.GET.get(param, None)
        if not p:
            return None
        acc[param] = p
    return acc


def reject_empty(request, fields):
    params = collect(request, fields)
    if params is None:
        acc = []
        for field in fields:
            if not request.GET.get(field, False):
                acc.append(field)
        return JsonResponse(acc, safe=False, status=400)
    return params


def authenticate(request):
    authenticator = request.GET.get('authenticator', None)
    if not authenticator:
        return HttpResponseBadRequest
    # TODO: does this work?
    authenticator = Authenticator.objects.all().filter(authenticator=authenticator)
    return JsonResponse(authenticator, safe=False)


def login(request):
    fields = ('username', 'password')
    params = reject_empty(request, fields)
    if not isinstance(params, dict):
        # params is just the error response
        return params

    # Check for unknown username or wrong password
    errors = []
    # TODO: does this work?
    user = Person.objects.all().filter(username=params['username'])
    if not user:
        errors.append('username')
    elif not user.check_password(params['password']):
        errors.append('password')
    if errors:
        return JsonResponse(errors, safe=False, status=400)

    # at this point, we're valid
    # create and return authenticator
    authenticator = Authenticator(user_id_id=user.id)
    return JsonResponse(authenticator, safe=False)


def logout(request):
    authenticator = request.GET.get('authenticator', None)
    if not authenticator:
        return HttpResponseBadRequest
    # TODO: does this work?
    authenticator = Authenticator.objects.all().filter(authenticator=authenticator)
    if not authenticator:
        return HttpResponseBadRequest

    # delete authenticator and return status 200
    authenticator.delete()
    return HttpResponse()


def register(request):
    fields = ('username', 'password', 'first_name', 'last_name', 'birthday')
    params = reject_empty(request, fields)
    if not isinstance(params, dict):
        # params = error response
        return params

    # TODO: does this work?
    user = Person.objects.all().filter(username=params['username'])
    if user:
        return JsonResponse(['username'], status=400)
    # create person model
    Person(params)
    # defer to login routine to send authenticator
    return login(request)
