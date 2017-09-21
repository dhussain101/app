from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *


def index(request):
    return HttpResponse("Hello, world. You're at the index of our lottery site.")


class PersonViewSet(viewsets.ModelViewSet):
    """
    This class provides list, retrieve, create, update,
    partial_update, and destroy operations for Person objects
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class LotteryViewSet(viewsets.ModelViewSet):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
