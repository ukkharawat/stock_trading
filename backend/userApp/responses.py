class ResponseObject(object):

    @staticmethod
    def createSuccessLoginResponse(userSerializer, key):
        return {
            'message': 'Authentication success',
            'username': userSerializer['username'],
            'cash': userSerializer['cash'],
            'stepCount': userSerializer['stepCount'],
            'Token': key,
            'success': True
        }

    @staticmethod
    def createFailedLoginResponse():
        return {
            'message': 'Authentication failed',
            'success': False
        }

    @staticmethod
    def createSuccessCreateUserResponse():
        return {
            'message': 'Creating user succesful',
            'success': True
        }

    @staticmethod
    def createFailedCreateUserResponse():
        return {
            'message': 'User\'s already exist',
            'success': False
        }

    @staticmethod
    def createSuccessLogoutResponse():
        return {
            'message': 'Log out success',
            'success': True
        }

    @staticmethod
    def createFailedLogoutResponse():
        return {
            'message': 'You have to log in before log out',
            'success': False
        }

    @staticmethod
    def createSuccessNextStepResponse(stockValueJSON):
        response = {
            'message': 'Next step success',
            'success': True
        }
        response.update(stockValueJSON)

        return response

    @staticmethod
    def createFailedNextStepResponse():
        return {
            'message': 'Next step failed, check your authentication',
            'success': False
        }