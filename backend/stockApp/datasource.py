from stockApp.utility import Utility

class Datasource(object):

    @staticmethod
    def createStockDetail(stock):
        return {
            'fullname': str(stock['fullname']),
            'symbol': str(stock['symbol'])
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
        if (stockValue.open == stockValue.open):
            return {
            'Date': str(stockValue.date),
            'Open': stockValue.open,
            'Close': stockValue.close,
            'BuyPrice': Utility.findStockPrice(stockValue),
            'High': stockValue.high,
            'Low': stockValue.low,
            'Adj': stockValue.adjClose,
            'Volume': stockValue.volume
            }
        else:
            return {}

    @staticmethod
    def createComparedStockValue(before, after):
        oldPrice = float(Utility.findStockPrice(before))
        oldPrice = oldPrice if oldPrice == oldPrice else 0
        currentPrice = float(Utility.findStockPrice(after))
        currentPrice = currentPrice if currentPrice == currentPrice else 0
        diff = currentPrice - oldPrice

        return {
            'diff': "{0:.2f}".format(diff),
            'diffPer': "{0:.2f}".format(round(diff/oldPrice,2)) if oldPrice > 0 else 0,
            'currentPrice': currentPrice,
            'symbol': str(after.symbol)
        }