class Datasource(object):

    @staticmethod
    def createUserDetailSerializer(username):
        return {
            "username": username,
            "cash": 10000,
            "stepCount": 0
        }