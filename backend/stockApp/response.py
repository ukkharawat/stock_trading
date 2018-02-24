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
            'stockList': [Datasource.createStockDetail(x) for x in data]
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
        
        comparedValues = [ Datasource.createComparedStockValue(x, y) for (x, y) in zip(stockValues[::2], stockValues[1::2])]
        
        response = {
            'success': True,
            'comparedValues': comparedValues
        }

        return JsonResponse(response, status = status.HTTP_200_OK)