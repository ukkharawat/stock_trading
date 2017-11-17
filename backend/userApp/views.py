# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.timezone import datetime
from django.utils.formats import localize

from django.contrib.auth.models import User
# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        if data['username'] is not None and data['password'] is not None:
            try:
                user = User.objects.create_user(username = data['username'], 
                                            password = data['username'])
            
                user.save()

                response = {
                    "message": "Creating user succesful"
                }

                return JsonResponse(response, status = 400)
            except:
                response = {
                    "message": "User's already exist"
                }

                return JsonResponse(response, status = 400)
                
            
