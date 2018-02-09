class Datasource(object):

    @staticmethod
    def createUserDetailSerializer(username):
        return {
            'username': username,
            'cash': 1000000,
            'stepCount': 1
        }

    @staticmethod
    def createStockValueDict(stockValue):
        result = {
            'stocks': {
                'shortname': str(stockValue.name),
                'date': stockValue.date.strftime('%Y-%m-%d'),
                'openPrice': stockValue.openPrice,
                'closePrice': stockValue.closePrice,
                'high': stockValue.high,
                'low': stockValue.low,
                'adjClose': stockValue.adjClose,
                'volume': stockValue.volume
            }
        }
        return result

    @staticmethod
    def createStockArray(stockValues):
        result = []
        for i in range(stockValues.count()):
            temp = Datasource.createStockValueDict(stockValues[i])

            result.append(temp['stocks'])

        return result

    @staticmethod
    def createUpdateUser(user, newStepCount):
        return {
            "username": user.username,
            "cash": user.cash,
            "stepCount": newStepCount
        }

    @staticmethod
    def createUserPortfolio(portfolio):
        result = []
        for i in range(portfolio.count()):
            temp = {
                'symbol': portfolio[i].symbol,
                'volume': portfolio[i].volume,
                'averagePrice': portfolio[i].averagePrice
            }

            result.append(temp)

        return result