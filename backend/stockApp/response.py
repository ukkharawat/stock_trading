class Response(object):

    @staticmethod
    def createSuccessBuyStock(symbol, averagePrice, volume):
        action = 'buy'

        return Response.createSuccessActionWithStockResponse(action, symbol, averagePrice, volume)

    @staticmethod
    def createFailedBuyStock():
        return {
            'success': False
        }

    @staticmethod
    def createSuccessSellStock(symbol, averagePrice, volume):
        action = 'sell'

        return Response.createSuccessActionWithStockResponse(action, symbol, averagePrice, volume)
    
    @staticmethod
    def craeteFailedSellStock():
        return {
            'success': False
        }

    @staticmethod
    def createSuccessActionWithStockResponse(action, symbol, averagePrice, volume):
        return {
            'action': action,
            'success': True,
            'symbol': symbol,
            'averagePrice': averagePrice,
            'volume': volume
        }