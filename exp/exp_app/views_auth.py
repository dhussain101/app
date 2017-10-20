from django.shortcuts import render
from django.http import HttpResponseRedirect
from .views import get
import requests

from django.http import JsonResponse
import requests
MODEL_URL = 'http://models-api:8000'

def login(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    payload = {'username': username, 'password': password}
    response = get('login', params=payload)['results']
    return JsonResponse(response, safe=False)


def register(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    payload = {'username': username, 'password': password}
    response = get('register', params=payload)['results']
    return JsonResponse(response, safe=False)
