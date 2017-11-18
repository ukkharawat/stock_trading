# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.timezone import datetime
from django.utils.formats import localize

from django.contrib.auth.models import User
from userApp.definitions import HttpStatus
from userApp.responses import ResponseObject
# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        if data['username'] is not None and data['password'] is not None:
            try:
                user = User.objects.create_user(username = data['username'])
                user.set_password(data['password'])
            
                user.save()

                response = ResponseObject.createSuccessCreateUserResponse()

                return JsonResponse(response, status = HttpStatus.CREATED)
            except:
                response = ResponseObject.createFailedCreateUserResponse()

                return JsonResponse(response, status = HttpStatus.BAD_REQUEST)
                
@api_view(['POST'])
def authentication(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        if data['username'] is not None and data['password'] is not None:
            user = authenticate(username = data['username'], 
                                password = data['password'])

            if user is not None:
                login(request, user)
                response = ResponseObject.createSuccessLoginResponse(user.username)

                return JsonResponse(response, status = HttpStatus.OK)
            else:
                response = ResponseObject.createFailedLoginResponse()

                return JsonResponse(response, status = HttpStatus.BAD_REQUEST)

@api_view(['GET'])
def logOut(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            logout(request)
            response = ResponseObject.createSuccessLogoutResponse()

            return JsonResponse(response, status = HttpStatus.OK)
        else:
            response = ResponseObject.createFailedLogoutResponse()

            return JsonResponse(response, status = HttpStatus.OK)