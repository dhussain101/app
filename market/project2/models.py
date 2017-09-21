from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=32, unique=True)
    birthday = models.DateField()
    currency = models.IntegerField()


class Lottery(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    users = models.ManyToManyField(Person)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Bid(models.Model):
    lottery = models.ForeignKey(Lottery, models.CASCADE)
    user = models.ForeignKey(Person, models.CASCADE)
    value = models.IntegerField()


class Card(models.Model):
    lottery = models.ForeignKey(Lottery, models.SET_NULL, null=True)
    game = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
