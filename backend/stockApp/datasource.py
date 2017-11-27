class Datasource(object):

    @staticmethod
    def createStockDetail(stockValue, stockName):
        return {
            "fullname": str(stockName.fullname),
            "shortname": str(stockValue.name),
            "date": stockValue.date.strftime('%Y-%m-%d'),
            "openPrice": stockValue.openPrice,
            "closePrice": stockValue.closePrice,
            "high": stockValue.high,
            "low": stockValue.low,
            "adjClose": stockValue.adjClose,
            "volume": stockValue.volume
        }

    @staticmethod
    def createPortfolio(actionData, username):
        return {
            "username": username,
            "symbol": actionData["symbol"],
            "volume": actionData["volume"],
            "averagePrice": actionData["averagePrice"]
        }

    @staticmethod
    def createActionDetail(symbol, volume, averagePrice):
        return {
            "symbol": symbol,
            "volume": volume,
            "averagePrice": averagePrice
        }