class Utility(object):

    @staticmethod
    def calculateAveragePrice(oldAveragePrice, oldVolume, newAveragePrice, newVolume):
        oldAmount = oldAveragePrice * oldVolume
        newAmount = newAveragePrice * newVolume
        amountSum = oldAmount + newAmount
        volumeSum = oldVolume + newVolume

        newAveragePrice = amountSum / volumeSum

        return "{0:.2f}".format(round(newAveragePrice,2))

    @staticmethod
    def isPortfolioStockEnough(portfolioVolume, actionVolume):
        return portfolioVolume >= actionVolume

    @staticmethod
    def isEmptyVolume(volume):
        return volume == 0