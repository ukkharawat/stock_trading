# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from userApp.definitions import HttpStatus
from userApp.responses import ResponseObject

from userApp.models import UserDetail
from userApp.serializers import UserDetailSerializer
# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        if data['username'] is not None and data['password'] is not None:
            try:
                userSerializer = UserDetailSerializer(data = {
                    "username": data['username'],
                    "cash": 10000,
                    "stepCount": 0
                })

                if userSerializer.is_valid():
                    user = User.objects.create_user(username = data['username'])
                    user.set_password(data['password'])

                    userSerializer.save()
                    user.save()

                    response = ResponseObject.createSuccessCreateUserResponse()

                    return JsonResponse(response, status = HttpStatus.CREATED)

                response = ResponseObject.createFailedCreateUserResponse()

                return JsonResponse(response, status = HttpStatus.BAD_REQUEST)
            except Exception, e:
                print str(e)
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

            return JsonResponse(response, status = HttpStatus.BAD_REQUEST)

@api_view(['GET'])
def getUserDetail(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            user = UserDetail.objects.get(pk = request.user)
            userSerializer = UserDetailSerializer(user)
            
            response = ResponseObject.createSuccessGetUserDetailResponse(userSerializer.data)

            return JsonResponse(response, status = HttpStatus.OK)
        else:
            response = ResponseObject.createFailedGetUserDetailResponse()

            return JsonResponse(response, status = HttpStatus.BAD_REQUEST)