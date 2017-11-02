from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views, views_auth

urlpatterns = [
    url(r'^authenticate/?$', views_auth.authenticate, name='authenticate'),
    url(r'^login/?$', views_auth.login, name='login'),
    url(r'^logout/?$', views_auth.logout, name='logout'),
    url(r'^register/?$', views_auth.register, name='register-user'),
]

router = DefaultRouter()
router.register(r'users', views.PersonViewSet)
router.register(r'lotteries', views.LotteryViewSet)
router.register(r'bids', views.BidViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'cards', views.CardViewSet)
router.register(r'authenticators', views.AuthenticatorViewSet)

urlpatterns += router.urls
