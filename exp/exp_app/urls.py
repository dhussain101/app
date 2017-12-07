from django.conf.urls import url

from . import views, views_auth

urlpatterns = [
    url(r'^game-pane/?$', views.game_pane, name='game-pane'),

    url(r'^card-pane/?$', views.card_pane, name='card-pane'),
    url(r'^card-create/?$', views.card_create, name='card-create'),
    url(r'^card-detail/([0-9]+)/?$', views.card_detail, name='card-detail'),

    url(r'^lottery-pane/?$', views.lottery_pane, name='lottery-pane'),
    url(r'^lottery-detail/(?P<pk>[0-9]+)/?$', views.lottery_detail, name='lottery-detail'),
    url(r'^lottery-create/?$', views.lottery_create, name='lottery-create'),

    url(r'^search/?$', views.search, name='search'),
    url(r'^recommendations/([0-9]+)/?$', views.lottery_recommendations, name='lottery-recommendations'),

    url(r'^authenticate/?$', views_auth.authenticate, name='authenticate'),
    url(r'^login/?$', views_auth.login, name='login'),
    url(r'^logout/?$', views_auth.logout, name='logout'),
    url(r'^register/?$', views_auth.register, name='register-user'),
]
