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