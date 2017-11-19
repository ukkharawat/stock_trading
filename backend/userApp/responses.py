class ResponseObject(object):

    @staticmethod
    def createSuccessLoginResponse(username):
        return {
            "message": "Authentication success",
            "username": username,
            "success": True
        }

    @staticmethod
    def createFailedLoginResponse():
        return {
            "message": "Authentication failed",
            "success": False
        }

    @staticmethod
    def createSuccessCreateUserResponse():
        return {
            "message": "Creating user succesful",
            "success": True
        }

    @staticmethod
    def createFailedCreateUserResponse():
        return {
            "message": "User's already exist",
            "success": False
        }

    @staticmethod
    def createSuccessLogoutResponse():
        return {
            "message": "Log out success",
            "success": True
        }

    @staticmethod
    def createFailedLogoutResponse():
        return {
            "message": "You have to log in before log out",
            "success": False
        }

    @staticmethod
    def createSuccessGetUserDetailResponse(userSerializer):
        return {
            "username": userSerializer['username'],
            "cash": userSerializer['cash'],
            "stepCount": userSerializer['stepCount'],
            "success": True
        }

    @staticmethod
    def createFailedGetUserDetailResponse():
        return {
            "message": "You have to log in",
            "success": False
        }