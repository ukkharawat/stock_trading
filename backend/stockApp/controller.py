from stockApp.datasource import Datasource

class Controller(object):

    @staticmethod
    def createNewPortfolio(symbol, averagePrice, volume, user):
        tradingDetail = Datasource.createTradingDetail(symbol, averagePrice, volume)
        portfolio = Datasource.createPortfolio(portfolioDetail, user)

        return portfolio