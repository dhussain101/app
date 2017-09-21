from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

router = DefaultRouter()
router.register(r'users', views.PersonViewSet)

urlpatterns += router.urls
