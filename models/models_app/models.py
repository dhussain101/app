import uuid

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)
    birthday = models.DateField()
    currency = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join(['(username)', self.username, '(currency)', str(self.currency)])


class Authenticator(models.Model):
    authenticator = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Person, models.CASCADE, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        person = Person.objects.get(id=self.user_id_id)
        return {
            'authenticator': self.authenticator,
            'username': person.username,
            'first_name': person.first_name,
            'last_name': person.last_name,
            'currency': person.currency,
        }

    def __str__(self):
        return ' '.join(map(str, [self.authenticator, self.user_id]))


class Lottery(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    participants = models.ManyToManyField(Person, blank=True)
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
        return ' '.join(['(game)', str(self.game), '(title)', self.title])


class LotteryRecommendation(models.Model):
    lottery = models.OneToOneField(Lottery)
    recommended = models.ManyToManyField(Lottery, related_name='recommendations')
