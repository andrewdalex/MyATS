from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/(\d{5})/', views.home, name='home'),
    url(r'^$', views.SearchIdView, name ='search'),
]
