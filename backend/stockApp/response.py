from django.http import JsonResponse
from rest_framework.views import status

class Response(object):

    @staticmethod
    def createSuccessBuyStock(symbol, averagePrice, volume):
        action = 'buy'
        response = Response.createSuccessActionWithStockResponse(action, symbol, averagePrice, volume)

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createFailedBuyStock():
        respones = {
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def createSuccessSellStock(symbol, averagePrice, volume):
        action = 'sell'
        response = Response.createSuccessActionWithStockResponse(action, symbol, averagePrice, volume)

        return JsonResponse(response, status = status.HTTP_200_OK)
    
    @staticmethod
    def craeteFailedSellStock():
        respones = {
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def createSuccessActionWithStockResponse(action, symbol, averagePrice, volume):
        return {
            'action': action,
            'success': True,
            'symbol': symbol,
            'averagePrice': averagePrice,
            'volume': volume
        }