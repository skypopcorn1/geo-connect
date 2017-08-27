from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.MapDetailAPIView.as_view(), name='list'),
]
