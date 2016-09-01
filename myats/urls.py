from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/(\d{5})/', views.home, name='home'),
    url(r'^search/', views.SearchIdView, name ='search'),
    url(r'^info/(\d{5})/(.{,15})/$', views.infoView),
]
