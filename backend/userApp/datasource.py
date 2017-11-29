class Datasource(object):

    @staticmethod
    def createUserDetailSerializer(username):
        return {
            'username': username,
            'cash': 10000,
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

    @staticmethod
    def createStockValueList(stockValue):
        result = []
        for i in range(stockValue.count()):
            temp = {
                'shortname': str(stockValue[i].name),
                "Date": stockValue[i].date.strftime('%Y-%m-%d'),
                "Open": stockValue[i].openPrice,
                "High": stockValue[i].high,
                "Low": stockValue[i].low,
                "Close": stockValue[i].closePrice,
                "Adj": stockValue[i].adjClose,
                "Volume": stockValue[i].volume
            }

            result.append(temp)
        
        return result