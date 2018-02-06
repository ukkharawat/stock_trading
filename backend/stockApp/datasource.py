class Datasource(object):

    @staticmethod
    def createStockDetail(stockValue, stockName):
        return {
            'fullname': str(stockName.fullname),
            'shortname': str(stockValue.name),
            'date': stockValue.date.strftime('%Y-%m-%d'),
            'openPrice': stockValue.openPrice,
            'closePrice': stockValue.closePrice,
            'high': stockValue.high,
            'low': stockValue.low,
            'adjClose': stockValue.adjClose,
            'volume': stockValue.volume
        }

    @staticmethod
    def createPortfolio(actionData, user):
        return {
            'user': user.pk,
            'symbol': actionData['symbol'],
            'averagePrice': actionData['averagePrice'],
            'volume': actionData['volume']
        }

    @staticmethod
    def createPortfolioDetail(data):
        return {
            'symbol': data['symbol'],
            'averagePrice': data['averagePrice'],
            'volume': data['volume']
        }

    @staticmethod
    def createDataDetail(symbol, averagePrice, volume):
        return {
            'symbol': symbol,
            'averagePrice': averagePrice,
            'volume': volume
        }

    @staticmethod
    def createUserDetail(user, cash):
        return {
            'username': user.username,
            'cash': cash,
            'stepCount': user.stepCount
        }

    @staticmethod
    def createStockValueList(stockValues):
        result = []
        
        for i in range(stockValues.count()):
            temp = {
                'Date': stockValues[i].date.strftime('%Y-%m-%d'),
                'shortname': str(stockValues[i].name),
                'Open': stockValues[i].openPrice,
                'Close': stockValues[i].closePrice,
                'High': stockValues[i].high,
                'Low': stockValues[i].low,
                'Adj': stockValues[i].adjClose,
                'Volume': stockValues[i].volume,
            }

            result.append(temp)

        return result