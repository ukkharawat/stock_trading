from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from stockApp import views

urlpatterns = [
    url(r'^list', views.list),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)