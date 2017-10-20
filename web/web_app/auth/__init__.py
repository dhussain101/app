__all__ = ['decorators', 'middleware', 'models', 'get', 'render', 'login', 'logout']

from django.shortcuts import render as django_render
from .models import User
import requests
EXP_URL = 'http://exp-api:8000'


def get(*paths, params={}):
    """
    Performs a get request on the experience API layer.
    For example, get('hello', 'world') will query http://exp-api:8000/hello/world
    :param paths: each sub-path entered as a separate argument
    :param params: URL parameters
    :return: JSON response from experience API
    """
    return requests.get(EXP_URL + ''.join('/{}' for _ in range(len(paths))).format(*paths), params=params).json()


def render(request, file, context):
    """
    Wrapper for django.shortcuts.render. Injects user information into context
    """
    context['user'] = request.user
    return django_render(request, file, context)


def login(request):
    """
    At the moment, sets the auth_token for future requests
    :param request: Request object
    """
    request.session['auth_token'] = request.user.authenticator


def logout(request):
    """
    At the moment, deletes the auth_token from future requests
    :param request: Request object
    """
    del request.session['auth_token']
    request.user = User(None)
