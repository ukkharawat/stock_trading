from stockApp.models import StockValue, Stock

class Utility(object):

    @staticmethod
    def getStockValueFromName(name, start, end):
        stock = Stock.objects.get(name = name)
        stockValue = StockValue.objects.filter(name = stock)[start:end]

        return stockValue
