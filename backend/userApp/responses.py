from django.http import JsonResponse
from rest_framework import status

class ResponseObject(object):

    @staticmethod
    def createSuccessLoginResponse(userSerializer, key):
        response = {
            'message': 'Authentication success',
            'username': userSerializer['username'],
            'cash': userSerializer['cash'],
            'stepCount': userSerializer['stepCount'],
            'Token': key,
            'success': True
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createFailedLoginResponse():
        response = {
            'message': 'Authentication failed',
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
    def createFailedCreateUserResponse():
        response = {
            'message': 'User\'s already exist',
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def createSuccessLogoutResponse():
        response = {
            'message': 'Log out success',
            'success': True
        }

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createFailedLogoutResponse():
        response = {
            'message': 'You have to log in before log out',
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def createSuccessNextStepResponse(stockValueJSON):
        response = {
            'message': 'Next step success',
            'success': True
        }
        response.update(stockValueJSON)

        return JsonResponse(response, status = status.HTTP_200_OK)

    @staticmethod
    def createFailedNextStepResponse():
        response = {
            'message': 'Next step failed, check your authentication',
            'success': False
        }

        return JsonResponse(response, status = status.HTTP_400_BAD_REQUEST)