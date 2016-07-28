from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/', views.RegFormView, name='signup'),
    url(r'^home/', views.home, name='home'),
    url(r'^resources/', views.ResourceView, name='resources'),
]
