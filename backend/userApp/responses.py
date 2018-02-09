from django.http import JsonResponse
from rest_framework import status
from userApp.datasource import Datasource

class ResponseObject(object):

    @staticmethod
    def createSuccessLoginResponse(userSerializer, key,  portfolio):
        portfolioList = Datasource.createUserPortfolio(portfolio)

        response = {
            'username': userSerializer['username'],
            'cash': userSerializer['cash'],
            'stepCount': userSerializer['stepCount'],
            'Token': key,
            'success': True,
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
    def createSuccessCreateUserResponse(user, key):
        response = {
            'username': user['username'],
            'cash': user['cash'],
            'stepCount': user['stepCount'],
            'Token': key,
            'success': True
        }

        return JsonResponse(response, status = status.HTTP_201_CREATED)

    @staticmethod
    def createSuccessLogoutResponse():
        response = {
            'success': True
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createSuccessNextStepResponse():
        response = {
            'success': True
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createUserDetailResponse(portfolio, user):
        portfolioList = Datasource.createUserPortfolio(portfolio)

        response = {
            'username': str(user.username),
            'cash': user.cash,
            'stepCount': user.stepCount,
            'portfolio': portfolioList,
            'success': True
        }

        return JsonResponse(response, status = status.HTTP_200_OK)
