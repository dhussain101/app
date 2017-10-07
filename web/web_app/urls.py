from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lotteries/(.*)', views.lottery_detail, name='lotteryDetail'),
    url(r'^lotteries$', views.index, name='index'),
    url(r'^cards$', views.cards, name='cards'),
    url(r'^cards/(.*)', views.card_detail, name='cardDetail'),
]
