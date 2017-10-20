from django.http import HttpResponseRedirect
from django.urls import reverse
from requests import HTTPError
from . import get, render
from .models import User
from ..forms import *
from .. import auth


def response_valid(response):
    try:
        response.raise_for_error()
    except HTTPError:
        return False
    return True


def collect(data, params):
    acc = {}
    for param in params:
        if param not in data:
            return None
        acc[param] = data[param]
    return acc


def add_errors(form, fields, errors):
    for field in ('username', 'password'):
        if field in errors:
            form.add_error(field, '{} is invalid'.format(field))


def login(request):
    redirect = HttpResponseRedirect(request.GET.get('next', reverse('index')))

    # disallow re-logging in
    if request.user.is_authenticated:
        return redirect

    form = None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            fields = ('username', 'password')
            # process the data in form.cleaned_data as required
            params = collect(form.cleaned_data, fields)
            # Send validated information to our experience layer
            response = get('login', params=params)

            # redirect to a new URL:
            if response_valid(response):
                auth.login(request, User(response.json()))
                return redirect

            add_errors(form, fields, response.json())
        # invalid form so return to login page

    # if a GET (or any other method) we'll create a blank form
    if not form:
        form = LoginForm()

    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    # Ignore bad authenticators (exp layer returns 400)
    get('logout', params={'authenticator': request.user.authenticator})
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    # disallow re-logging in
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    form = None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            fields = ('username', 'password', 'first_name', 'last_name', 'birthday')
            # process the data in form.cleaned_data as required
            params = collect(form.cleaned_data, fields)

            # Send validated information to our experience layer
            response = get('register', params=params)

            if response_valid(response):
                # redirect to a new URL:
                return HttpResponseRedirect(reverse('index'))

            add_errors(form, fields, response.json())
        # invalid form so return to register page

    # if a GET (or any other method) we'll create a blank form
    if not form:
        form = RegisterForm()

    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'register-user.html', context)
