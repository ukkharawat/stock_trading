class Utility(object):

    @staticmethod
    def calculateAveragePrice(portfolio, current):
        oldAmount = portfolio.averagePrice * portfolio.volume
        newAmount = current['averagePrice'] * current['volume']
        amountSum = oldAmount + newAmount
        volumeSum = portfolio.volume + current['volume']

        newAveragePrice = amountSum / volumeSum

        return "{0:.2f}".format(round(newAveragePrice,2))

    @staticmethod
    def isPortfolioStockEnough(portfolioVolume, actionVolume):
        return portfolioVolume >= actionVolume

    @staticmethod
    def isEmptyVolume(volume):
        return volume == 0