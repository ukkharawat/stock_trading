from django.http import JsonResponse
from rest_framework.views import status
from stockApp.datasource import Datasource
from stockApp.utility import Utility

class Response(object):
    
    @staticmethod
    def craeteFailedAction():
        response = {
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def createSuccessAction(user, action, portfolio):
        response = {
            'success': True,
            'username': user['username'],
            'cash': user['cash'],
            'action': action,
            'symbol': portfolio['symbol'],
            'averagePrice': portfolio['averagePrice'],
            'volume': portfolio['volume']
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createStockData(stockData):
        value = Datasource.createStockValue(stockData)

        response = {
            'success': True,
            'symbol': str(stockData),
            'stockValue': value
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createStockList(data):
        response = {
            'success': True,
            'stockList': data
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createStockValueList(stockValue):
        value = [Datasource.createStockValue(x) for x in stockValue]

        response = {
            'success': True,
            'symbol': str(stockValue[0]),
            'stockValue': value
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createNotFoundStock():
        response = {
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_404_NOT_FOUND)

    @staticmethod
    def createNotFoundStockValue():
        response = {
            'success': False,
            'diff': None,
            'currentPrice': None
        }

        return JsonResponse(response, status = status.HTTP_404_NOT_FOUND)

    @staticmethod
    def createUncomparedStockValue(stockValue):
        response = {
            'success': False,
            'diff': 0,
            'diffPer': 0,
            'currentPrice': Utility.findStockPrice(stockValue),
            'symbol': str(stockValue.name)
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createComparedStockValue(stockValues):
        oldPrice = float(Utility.findStockPrice(stockValues[0]))
        currentPrice = float(Utility.findStockPrice(stockValues[1]))
        diff = oldPrice - currentPrice

        response = {
            'success': False,
            'diff': diff,
            'diffPer': "{0:.2f}".format(round(diff/oldPrice,2)),
            'currentPrice': currentPrice,
            'symbol': str(stockValues[1].name)
        }

        return JsonResponse(response, status = status.HTTP_200_OK)