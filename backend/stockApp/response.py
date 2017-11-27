class Response(object):

    @staticmethod
    def createSuccessBuyStock(symbol, averagePrice, volume):
        return {
            "success": True,
            "symbol": symbol,
            "averagePrice": averagePrice,
            "volume": volume
        }

    def createFailedBuyStock():
        return {
            "success": False
        }