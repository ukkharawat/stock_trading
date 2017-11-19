from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from userApp import views

urlpatterns = [
    url(r'^register', views.register),
    url(r'^authentication', views.authentication),
    url(r'^logout', views.logOut),
    url(r'^userDetail', views.getUserDetail)
]

urlpatterns = format_suffix_patterns(urlpatterns)