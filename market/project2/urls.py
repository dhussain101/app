from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

router = DefaultRouter()
router.register(r'users', views.PersonViewSet)
router.register(r'lottery', views.LotteryViewSet)
router.register(r'bids', views.BidViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'cards', views.CardViewSet)

urlpatterns += router.urls
