from rest_framework import serializers
from .models import *


class PersonSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Person
        fields = ('id',
                  'first_name',
                  'last_name',
                  'username',
                  'birthday',
                  'currency',
                  'date_created')
        read_only_fields = ('date_created',)


class LotterySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Lottery
        fields = ('id',
                  'title',
                  'description',
                  'participants',
                  'start_time',
                  'start_time',
                  'end_time')
        read_only_fields = ('date_created',)


class BidSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bid
        fields = ('id',
                  'lottery',
                  'person',
                  'value',
                  'date_created')
        read_only_fields = ('date_created',)


class GameSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Game
        fields = ('id',
                  'title')


class CardSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Card
        fields = ('id',
                  'lottery',
                  'title',
                  'description',
                  'value')
