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
    def calculateTotalBuyPrice(averagePrice, volume):
        vatRate = 1.07
        commissionRate = 0.001578
        
        commission = averagePrice * volume * commissionRate * vatRate
        total = averagePrice * volume + commission

        return total

    @staticmethod
    def calculateTotalSellPrice(averagePrice, volume):
        vatRate = 1.07
        commissionRate = 0.001578
        
        commission = averagePrice * volume * commissionRate * vatRate
        total = averagePrice * volume - commission

        return total