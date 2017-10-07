from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lottery-pane$', views.lottery_pane, name='lottery-pane'),
    url(r'^card-pane$', views.card_pane, name='card-pane'),
    url(r'^lottery-detail/(.*)', views.lottery_detail, name='lottery-detail'),
    url(r'^card-detail/(.*)', views.card_detail, name='card-detail'),
]
