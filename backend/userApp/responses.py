from django.http import JsonResponse
from rest_framework import status
from userApp.datasource import Datasource

class ResponseObject(object):

    @staticmethod
    def createSuccessLoginResponse(userSerializer, key, stockValues, portfolio):
        stocks = Datasource.createStockArray(stockValues)
        portfolioList = Datasource.createUserPortfolio(portfolio)

        response = {
            'username': userSerializer['username'],
            'cash': userSerializer['cash'],
            'stepCount': userSerializer['stepCount'],
            'Token': key,
            'success': True,
            'stocks': stocks,
            'portfolio': portfolioList
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createFailedResponse():
        response = {
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def createSuccessCreateUserResponse():
        response = {
            'message': 'Creating user succesful',
            'success': True
        }

        return JsonResponse(response, status = status.HTTP_201_CREATED)

    @staticmethod
    def createSuccessLogoutResponse():
        response = {
            'message': 'Log out success',
            'success': True
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createSuccessNextStepResponse(stockValueJSON):
        response = {
            'message': 'Next step success',
            'success': True
        }
        response.update(stockValueJSON)

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createUserDetailResponse(portfolio, user, stockValue):
        portfolioList = Datasource.createUserPortfolio(portfolio)
        stockValueList = Datasource.createStockValueList(stockValue)

        response = {
            'username': str(user.username),
            'cash': user.cash,
            'stepCount': user.stepCount,
            'portfolio': portfolioList,
            'stockValue': stockValueList
        }

        return JsonResponse(response, status = status.HTTP_200_OK)
