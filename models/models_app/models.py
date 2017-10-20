from django.db import models
import uuid


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=32, unique=True)
    birthday = models.DateField()
    currency = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join(['(username)', self.username, '(currency)', str(self.currency)])


class Authenticator(models.Model):
    authenticator = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Person, models.PROTECT, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join(map(str, [self.authenticator, self.user_id]))


class Lottery(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    participants = models.ManyToManyField(Person)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join(['(title)', self.title])


class Bid(models.Model):
    lottery = models.ForeignKey(Lottery, models.CASCADE)
    person = models.ForeignKey(Person, models.CASCADE)
    value = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join(['(value)', str(self.value)])


class Game(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Card(models.Model):
    lottery = models.ForeignKey(Lottery, models.SET_NULL, null=True)
    game = models.ForeignKey(Game, models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    value = models.IntegerField(default=0)

    def __str__(self):
        return ' '.join(['(game)', self.game, '(title)', self.title])
