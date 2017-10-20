from rest_framework import viewsets, filters
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from .serializers import *
from .models import *


def login(request):
    # if check password works:
    # create new Authenticator
    # else return error
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    user = Person.objects.all().filter(username=username)
    if user.check_passwordk(password):
        auth_token = Authenticator(user_id=user)
        auth_token.save()
        payload = {'auth_token': auth_token}
        return JsonResponse(payload, safe=False)
    else:
        return HttpResponse('Unauthorized', status=401)

class PersonViewSet(viewsets.ModelViewSet):
    """
    This class provides list, retrieve, create, update,
    partial_update, and destroy operations for Person objects
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'username')


class AuthenticatorViewSet(viewsets.ModelViewSet):
    queryset = Authenticator.objects.all()
    serializer_class = AuthenticatorSerializer


class LotteryViewSet(viewsets.ModelViewSet):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('end_time', 'start_time')
    ordering = ('end_time',)
    filter_fields = {
        'title': ('contains',),
        'description': ('contains',),
    }


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_fields = {
        'title': ('contains',),
    }


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('title',)
    ordering = ('title',)
    filter_fields = {
        'game': ('exact',),
        'title': ('contains',),
    }
