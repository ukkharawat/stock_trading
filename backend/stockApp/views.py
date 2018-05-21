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
import datetime

@api_view(['GET'])
@permission_classes((AllowAny, ))
def list(request):
	if request.method == 'GET':
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)

		return Response.createStockList(serializer.data)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def getCurrentStockData(request):
	if request.method == 'GET':
		try:
			username = str(request.user)
			user = UserDetail.objects.get(username = username)
			step = int(user.stepCount)
		
		except:
			step = 1
			
		symbol = request.GET['symbol']
		stock = Stock.objects.get(symbol = symbol)
		date = datetime.date(2016, 1, 3) + datetime.timedelta(days = step)
		
		stockValue = StockValue.objects.filter(symbol = stock, date__gte = date)[:1]

		if stockValue is not None:
			return Response.createStockData(stockValue[0])
		
		else:
			return Response.createNotFoundStockValue()

@api_view(['GET'])
@permission_classes((AllowAny,))
def getComparedValue(request):
	if request.method == 'GET':
		try:
			username = str(request.user)
			user = UserDetail.objects.get(username = username)
			step = int(user.stepCount)
		
		except:
			step = 1

		startDate =  datetime.date(2016, 1, 3) + datetime.timedelta(days = step - 7)
		endDate = datetime.date(2016, 1, 3) + datetime.timedelta(days = 1 + step)
		try:
			stockValue = StockValue.objects.filter(date__gte=startDate, date__lte=endDate)

			return Response.createComparedStockValue(stockValue)

		except Exception as e:
			print(e)
			return Response.createNotFoundStockValue()

@api_view(['GET'])
@permission_classes((AllowAny, ))
def getStockValue(request):
	if request.method == 'GET':
		try:
			username = str(request.user)
			user = UserDetail.objects.get(username = username)
			step = int(user.stepCount)
		
		except:
			step = 1

		symbol = request.GET['symbol']
		stock = Stock.objects.get(symbol = symbol)
		date = datetime.date(2016, 1, 3) + datetime.timedelta(days = step)

		stockValue = StockValue.objects.filter(symbol = stock, date__lte=date)
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
		action = 'BUY'
		user = UserDetail.objects.get(username = username)
		
		totalBuyPrice = Utility.calculateTotalBuyPrice(data['averagePrice'], data['volume'])
		newCash = float("{0:.2f}".format(user.cash - totalBuyPrice))

		try:
			portfolio = Portfolio.objects.get(user = user, symbol = data['symbol'])
			newAveragePrice = Utility.calculateAveragePrice(portfolio, data)
			newVolume = portfolio.volume + data['volume']

			newPortfolio = Controller.createNewPortfolio(portfolio.symbol, newAveragePrice, newVolume, user)
			updateUser = Datasource.createUserDetail(user, newCash)
			portfolioSerializer = PortfolioSerializer(portfolio, data = newPortfolio)
			userSerializer = UserDetailSerializer(user, data = updateUser)

			if portfolioSerializer.is_valid() and userSerializer.is_valid() and newCash >= 0:
				portfolioSerializer.save()
				userSerializer.save()

				return Response.createSuccessAction(userSerializer.data, action, portfolioSerializer.data)

		except Portfolio.DoesNotExist:
			portfolio = Datasource.createPortfolio(data, user)
			portfolioSerializer = PortfolioSerializer(data = portfolio)
			updateUser = Datasource.createUserDetail(user, newCash)
			userSerializer = UserDetailSerializer(user, data = updateUser)

			if portfolioSerializer.is_valid() and userSerializer.is_valid() and newCash >= 0:
				portfolioSerializer.save()
				userSerializer.save()

				return Response.createSuccessAction(userSerializer.data, action, portfolioSerializer.data)

		return Response.craeteFailedAction()

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def sellStock(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		action = 'SELL'
		username = str(request.user)
		
		try:
			user = UserDetail.objects.get(username = username)
			portfolio = Portfolio.objects.get(user = user, symbol = data['symbol'])

			if Utility.isPortfolioStockEnough(portfolio.volume, data['volume']):
				newVolume = portfolio.volume - data['volume']
				totalSellPrice = Utility.calculateTotalSellPrice(data['averagePrice'], data['volume'])
				newCash = float("{0:.2f}".format(user.cash + totalSellPrice))

				updateUser =  Datasource.createUserDetail(user, newCash)
				userSerializer = UserDetailSerializer(user, data = updateUser)
				newPortfolio = Controller.createNewPortfolio(portfolio.symbol, portfolio.averagePrice, newVolume, user)
				portfolioSerializer = PortfolioSerializer(portfolio, data = newPortfolio)
						
				if portfolioSerializer.is_valid() and userSerializer.is_valid():
					userSerializer.save()
					portfolioSerializer.save()
					
					return Response.createSuccessAction(userSerializer.data, action, portfolioSerializer.data)

		except Portfolio.DoesNotExist:

			return Response.craeteFailedAction()

		return Response.craeteFailedAction()