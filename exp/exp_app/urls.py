from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lottery-pane$', views.lotteryPane, name='lottery-pane'),
]
