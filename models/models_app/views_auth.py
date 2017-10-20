from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.contrib.auth.hashers import check_password
from .models import Authenticator, Person


def collect(request, params):
    acc = {}
    for param in params:
        p = request.GET.get(param, None)
        if p is None:
            return None
        acc[param] = p
    return acc


def reject_empty(request, fields):
    params = collect(request, fields)
    if params is None:
        # accumulate all fields not in response
        acc = tuple(filter(lambda field: not request.GET.get(field, False), fields))
        return JsonResponse(acc, safe=False, status=400)
    return params


def authenticator_response(user_id):
    authenticator = Authenticator(user_id_id=user_id)
    authenticator.save()
    return JsonResponse(authenticator.to_dict(), safe=False)


def authenticate(request):
    authenticator = request.GET.get('authenticator', None)
    if not authenticator:
        return HttpResponseBadRequest()
    try:
        authenticator = Authenticator.objects.get(authenticator=authenticator)
    except Authenticator.DoesNotExist:
        return HttpResponseBadRequest()
    return JsonResponse(authenticator.to_dict(), safe=False)


def login(request):
    fields = ('username', 'password')
    params = reject_empty(request, fields)
    if not isinstance(params, dict):
        # params is just the error response
        return params

    # Check for unknown username or wrong password
    errors = []
    user = None
    try:
        user = Person.objects.get(username=params['username'])
    except Person.DoesNotExist:
        errors.append('username')
    if user and not check_password(params['password'], user.password):
        errors.append('password')
    if errors:
        return JsonResponse(errors, safe=False, status=400)

    # at this point, we're valid
    # create and return authenticator
    return authenticator_response(user.id)


def logout(request):
    authenticator = request.GET.get('authenticator', None)
    if not authenticator:
        return HttpResponseBadRequest()
    try:
        authenticator = Authenticator.objects.get(authenticator=authenticator)
    except Authenticator.DoesNotExist:
        return HttpResponseBadRequest()

    # delete authenticator and return status 200
    authenticator.delete()
    return HttpResponse()


def register(request):
    fields = ('username', 'password', 'first_name', 'last_name', 'birthday')
    params = reject_empty(request, fields)
    if not isinstance(params, dict):
        # params is just the error response
        return params

    if Person.objects.filter(username=params['username']):
        # username already exists
        return JsonResponse(['username'], status=400, safe=False)
    # create person model
    user = Person(**params)
    user.save()
    return authenticator_response(user.id)
