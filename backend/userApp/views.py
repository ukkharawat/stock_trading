# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from rest_framework import status
from userApp.responses import ResponseObject
from userApp.datasource import Datasource

from userApp.models import UserDetail, Portfolio
from userApp.serializers import UserDetailSerializer
from userApp.utility import Utility
# Create your views here.
@api_view(['POST'])
@permission_classes((AllowAny, ))
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        if data['username'] is not None and data['password'] is not None:
            try:
                username = data['username']
                password = data['password']

                userSerializer = UserDetailSerializer(data = Datasource.createUserDetailSerializer(username))

                if userSerializer.is_valid():
                    user = User.objects.create_user(username = username)
                    user.set_password(password)
                    userSerializer.save()
                    user.save()

                    return ResponseObject.createSuccessCreateUserResponse()
                
                return ResponseObject.createFailedResponse()
            except:
                return ResponseObject.createFailedResponse()
                
@api_view(['POST'])
@permission_classes((AllowAny, ))
def logIn(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        if data['username'] is not None and data['password'] is not None:
            try:
                username = data['username']
                password = data['password']

                user = authenticate(username = username, password = password)

                if user is not None:
                    token, _ = Token.objects.get_or_create(user=user)
                    userData = UserDetail.objects.get(pk = username)
                    userSerializer = UserDetailSerializer(userData)
                    portfolio = Portfolio.objects.filter(username = userSerializer.data)
                    stockValue = Utility.getStockValueFromName('PTT', 1, userSerializer.data['stepCount'])

                    return ResponseObject.createSuccessLoginResponse(userSerializer.data, token.key, stockValue, portfolio)

                return ResponseObject.createFailedResponse()
              
            except:
                return ResponseObject.createFailedResponse()

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def logOut(request):
    if request.method == 'GET':
        request.user.auth_token.delete()

        return ResponseObject.createSuccessLogoutResponse()

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUserDetail(request):
    if request.method == 'GET':
        user = UserDetail.objects.get(pk = request.user)
        portfolio = Portfolio.objects.filter(username = user)
        stockValue = Utility.getStockValueFromName('PTT', 1, user.stepCount)

        return ResponseObject.createUserDetailResponse(portfolio, user, stockValue)
        
@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def nextStep(request):
    if request.method == 'PUT':
        user = UserDetail.objects.get(pk = request.user)
        newStepCount = request.data['stepCount']
        updateUser = Datasource.createUpdateUser(user, newStepCount)
        userSerializer = UserDetailSerializer(user, data = updateUser)

        if userSerializer.is_valid():
            userSerializer.save()
            stockValue = Utility.getStockValueFromName('PTT', newStepCount - 1, newStepCount)
            stockValueDict = Datasource.createStockValueDict(stockValue[0])
            
            return ResponseObject.createSuccessNextStepResponse(stockValueDict)
        
        return ResponseObject.createFailedResponse()