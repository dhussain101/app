from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lottery-pane$', views.lotteryPane, name='lottery-pane'),
    url(r'^card-pane$', views.cardPane, name='card-pane'),
    url(r'^lottery-detail/(.*)', views.lotteryDetail, name='lottery-detail'),
    url(r'^card-detail/(.*)', views.cardDetail, name='card-detail'),
]
