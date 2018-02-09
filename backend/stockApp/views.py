# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from stockApp.models import Stock, StockValue
from stockApp.serializers import StockSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from stockApp.datasource import Datasource
from stockApp.utility import Utility
from stockApp.controller import Controller
from stockApp.response import Response
from userApp.models import Portfolio, UserDetail
from userApp.serializers import PortfolioSerializer, UserDetailSerializer

@api_view(['GET'])
@permission_classes((AllowAny, ))
def list(request):
	if request.method == 'GET':
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)

		return Response.createStockList(serializer.data)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def getStockValue(request):
	if request.method == 'GET':
		symbol = request.GET['symbol']
		start = int(request.GET['start'])
		end = int(request.GET['end'])
		stock = Stock.objects.get(name = symbol)
		stockValue = StockValue.objects.filter(name = stock)[start:end]
		if stockValue.exists():
			return Response.createStockValueList(stockValue)
		else:
			return Response.createNotFoundStock()

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def buyStock(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		username = str(request.user)
		user = UserDetail.objects.get(username = username)

		try:
			portfolio = Portfolio.objects.get(user = user, symbol = data['symbol'])
			newAveragePrice = Utility.calculateAveragePrice(portfolio, data)
			newVolume = portfolio.volume + data['volume']
			newCash = user.cash - (data['averagePrice'] * data['volume'])

			newPortfolio = Controller.createNewPortfolio(portfolio.symbol, newAveragePrice, newVolume, user)
			updateUser = Datasource.createUserDetail(user, newCash)
			portfolioSerializer = PortfolioSerializer(portfolio, data = newPortfolio)
			userSerializer = UserDetailSerializer(user, data = updateUser)

			if portfolioSerializer.is_valid() and userSerializer.is_valid() and newCash >= 0:
				portfolioSerializer.save()
				userSerializer.save()

				return Response.createSuccessBuyStock(userSerializer.data, portfolioSerializer.data)

			return Response.createFailedBuyStock()

		except Portfolio.DoesNotExist:
			newCash = user.cash - (data['averagePrice'] * data['volume'])
			portfolio = Datasource.createPortfolio(data, user)
			portfolioSerializer = PortfolioSerializer(data = portfolio)
			updateUser = Datasource.createUserDetail(user, newCash)
			userSerializer = UserDetailSerializer(user, data = updateUser)

			if portfolioSerializer.is_valid() and userSerializer.is_valid() and newCash >= 0:
				portfolioSerializer.save()
				userSerializer.save()

				return Response.createSuccessBuyStock(userSerializer.data, portfolioSerializer.data)

			return Response.createFailedBuyStock()

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def sellStock(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		username = str(request.user)
		
		try:
			user = UserDetail.objects.get(username = username)
			portfolio = Portfolio.objects.get(user = user, symbol = data['symbol'])

			if Utility.isPortfolioStockEnough(portfolio.volume, data['volume']):
				newVolume = portfolio.volume - data['volume']
				newCash = user.cash + (data['volume'] * data['averagePrice'])

				updateUser =  Datasource.createUserDetail(user, newCash)
				userSerializer = UserDetailSerializer(user, data = updateUser)
				newPortfolio = Controller.createNewPortfolio(portfolio.symbol, portfolio.averagePrice, newVolume, user)
				portfolioSerializer = PortfolioSerializer(portfolio, data = newPortfolio)
						
				if portfolioSerializer.is_valid() and userSerializer.is_valid():
					userSerializer.save()
					portfolioSerializer.save()
					
					return Response.createSuccessSellStock(userSerializer.data, portfolioSerializer.data)
				else:
					return Response.createFailedSellStock()
				
			else:
				return Response.createFailedSellStock()

		except Portfolio.DoesNotExist:

			return Response.createFailedSellStock()