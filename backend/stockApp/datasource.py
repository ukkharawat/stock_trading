from stockApp.utility import Utility

class Datasource(object):

    @staticmethod
    def createStockDetail(stock):
        return {
            'fullname': str(stock['fullname']),
            'symbol': str(stock['name'])
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
    def createTradingDetail(symbol, averagePrice, volume):
        return {
            'symbol': symbol,
            'averagePrice': averagePrice if volume > 0 else 0,
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
    def createStockValue(stockValue):

        return {
            'Date': str(stockValue.date),
            'Open': stockValue.openPrice,
            'Close': stockValue.closePrice,
            'BuyPrice': Utility.findStockPrice(stockValue),
            'High': stockValue.high,
            'Low': stockValue.low,
            'Adj': stockValue.adjClose,
            'Volume': stockValue.volume,
        }