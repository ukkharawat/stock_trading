from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from userApp import views

urlpatterns = [
    url(r'^register', views.register),
    url(r'^login', views.logIn),
    url(r'^logout', views.logOut),
    url(r'^nextStep', views.nextStep),
    url(r'^detail', views.getUserDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)