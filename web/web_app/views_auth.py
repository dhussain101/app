from django.http import HttpResponseRedirect
from .auth import get, render
from .forms import *
from . import auth


def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            payload = {'username': username, 'password': password}
            # Send validated information to our experience layer
            response = get('login', params=payload)

            # TODO: the following...
            # - check if username exists, if not error
            # - check if password valid, if not error

            # redirect to a new URL:
            return HttpResponseRedirect('/')
        # invalid form so return to login page
        else:
            form = LoginForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    # TODO: send logout request to exp layer
    auth.logout(request)


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            payload = {'username': username, 'password': password}
            # Send validated information to our experience layer
            response = get('login', params=payload)

            # TODO: the following...
            # - error if username exists
            # - error if password invalid

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'register-user.html', context)
