# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import status
from stockApp.models import Stock, StockValue
from stockApp.serializers import StockSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from stockApp.datasource import Datasource
from stockApp.utility import Utility
from stockApp.response import Response
from userApp.models import Portfolio, UserDetail
from userApp.serializers import PortfolioSerializer, UserDetailSerializer

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
		stock = Stock.objects.get(name = stockValue[0].name)
		stockValueDict = Datasource.createStockDetail(stockValue[0], stock)
		
		return JsonResponse(stockValueDict, status = status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def buyStock(request):
    if request.method == 'POST':
		data = JSONParser().parse(request)
		username = str(request.user)
		user = UserDetail.objects.get(pk = username)

		try:
			portfolio = Portfolio.objects.get(username = username, symbol = data['symbol'])
			newAveragePrice = Utility.calculateAveragePrice(portfolio.averagePrice, 
							portfolio.volume, data['averagePrice'], data['volume'])
			newVolume = portfolio.volume + data["volume"]

			actionDetail = Datasource.createActionDetail(portfolio.symbol, newVolume, newAveragePrice)
			newPortfolio = Datasource.createPortfolio(actionDetail, user)
			portfolioSerializer = PortfolioSerializer(portfolio, data = newPortfolio)

			if portfolioSerializer.is_valid():
				portfolioSerializer.save()
				response = Response.createSuccessBuyStock(portfolio.symbol, newAveragePrice, newVolume)

				return JsonResponse(response, status = status.HTTP_200_OK)

			response = Response.createFailedBuyStock()

			return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

		except Portfolio.DoesNotExist:
			portfolio = Datasource.createPortfolio(data, user)
			portfolioSerializer = PortfolioSerializer(data = portfolio)

			if portfolioSerializer.is_valid():
				portfolioSerializer.save()
				response = Response.createSuccessBuyStock(data['symbol'], data['averagePrice'], data['volume'])

				return JsonResponse(response, status = status.HTTP_200_OK)

			response = Response.createFailedBuyStock()

			return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
# def sellStock(request):