from django.http import JsonResponse
from rest_framework.views import status

class Response(object):

    @staticmethod
    def createSuccessBuyStock(user, symbol, averagePrice, volume):
        action = 'buy'
        response = Response.createSuccessActionWithStockResponse(user, action, symbol, averagePrice, volume)

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createFailedBuyStock():
        response = {
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def createSuccessSellStock(user, symbol, averagePrice, volume):
        action = 'sell'
        response = Response.createSuccessActionWithStockResponse(user, action, symbol, averagePrice, volume)

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