class Datasource(object):

    @staticmethod
    def createUserDetailSerializer(username):
        return {
            "username": username,
            "cash": 10000,
            "stepCount": 0
        }

    @staticmethod
    def createStockValueDict(stockValue):
        result = {
            "update": {
                "shortname": str(stockValue.name),
                "date": stockValue.date.strftime('%Y-%m-%d'),
                "openPrice": stockValue.openPrice,
                "closePrice": stockValue.closePrice,
                "high": stockValue.high,
                "low": stockValue.low,
                "adjClose": stockValue.adjClose,
                "volume": stockValue.volume
            }
        }
        return result