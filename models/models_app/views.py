from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *


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
