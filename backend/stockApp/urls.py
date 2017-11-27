from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from stockApp import views

urlpatterns = [
    url(r'^list', views.list),
    url(r'^stockFirstValue', views.getStockFirstValue),
    url(r'^buy', views.buyStock)    
]

urlpatterns = format_suffix_patterns(urlpatterns)