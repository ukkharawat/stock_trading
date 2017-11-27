# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status
from stockApp.models import Stock, StockValue
from stockApp.serializers import StockSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from userApp.datasource import Datasource

@api_view(['GET'])
@permission_classes((AllowAny, ))
def list(request):
	if request.method == 'GET':
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)
		return Response(serializer.data)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def getStockFirstValue(request):
    if request.method == 'GET':
        stockValue = StockValue.objects.all()[:1]
        stockValueDict = Datasource.createStockValueDict(stockValue[0])

        return JsonResponse(stockValueDict, status = status.HTTP_200_OK)
	
