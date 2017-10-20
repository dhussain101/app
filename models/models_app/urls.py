from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = []

router = DefaultRouter()
router.register(r'users', views.PersonViewSet)
router.register(r'lotteries', views.LotteryViewSet)
router.register(r'bids', views.BidViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'cards', views.CardViewSet)
router.register(r'authenticators', views.AuthenticatorViewSet)

urlpatterns += router.urls
