from django.conf.urls import url
from . import views, views_auth

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lotteries/?$', views.lotteries, name='lotteries'),
    url(r'^lotteries/([0-9]+)/?$', views.lottery_detail, name='lottery-detail'),
    url(r'^cards/?$', views.cards, name='cards'),
    url(r'^cards/([0-9]+)/?$', views.card_detail, name='card-detail'),

    url(r'^login/?$', views_auth.login, name='login'),
    url(r'^register/?$', views_auth.register, name='register-user'),

    url(r'^.*$', views.bad_url, name='404'),
]
