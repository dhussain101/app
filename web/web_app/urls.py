from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lotteries/(.*)', views.lotteryDetail, name='lotteryDetail'),
    url(r'^lotteries$', views.index, name='index'),
    url(r'^cards$', views.cards, name='index'),
    url(r'^cards/(.*)', views.cardDetail, name='cardDetail'),
]
