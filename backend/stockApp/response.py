from django.http import JsonResponse
from rest_framework.views import status
from stockApp.datasource import Datasource

class Response(object):

    @staticmethod
    def createSuccessBuyStock(user, portfolio):
        action = 'buy'
        symbol = portfolio['symbol']
        averagePrice = portfolio['averagePrice']
        volume = portfolio['volume']
        response = Response.createSuccessActionWithStockResponse(user, action, symbol, averagePrice, volume)

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createFailedBuyStock():
        response = {
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def createSuccessSellStock(user, portfolio):
        action = 'sell'
        response = Response.createSuccessActionWithStockResponse(user, action, portfolio['symbol']
                                                    , portfolio['averagePrice'], portfolio['volume'])

        return JsonResponse(response, status = status.HTTP_200_OK)
    
    @staticmethod
    def craeteFailedSellStock():
        response = {
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def createSuccessActionWithStockResponse(userDetail, action, symbol, averagePrice, volume):
        return {
            'username': userDetail['username'],
            'cash': userDetail['cash'],
            'action': action,
            'success': True,
            'symbol': symbol,
            'averagePrice': averagePrice,
            'volume': volume
        }

    @staticmethod
    def createStockList(data):
        response = {
            'stockList': data
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createStockValueList(stockValue):
        stockValueList = Datasource.createStockValueList(stockValue)
        response = {
            'stockValue': stockValueList
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createNotFoundStock():
        response = {
            'status': False
        }

        return JsonResponse(response, status = status.HTTP_404_NOT_FOUND)