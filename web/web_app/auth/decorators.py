from django.http import HttpResponseRedirect
from django.urls import reverse


def login_required(view):
    """
    Replace django.contrib.auth.login_required
    """
    def wrap(request, *args, **kwargs):
        # check if user is authenticated
        if request.user:
            return view(request, *args, **kwargs)
        # TODO: redirect
        return HttpResponseRedirect(reverse('login'))
    return wrap
