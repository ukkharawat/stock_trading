from stockApp.datasource import Datasource

class Controller(object):

    @staticmethod
    def createNewPortfolio(symbol, averagePrice, volume, user):
        dataDetail = Datasource.createDataDetail(symbol, averagePrice, volume)
        portfolioDetail = Datasource.createPortfolioDetail(dataDetail)
        newPortfolio = Datasource.createPortfolio(portfolioDetail, user)

        return newPortfolio

    @staticmethod
    def createUpdateUser(user, updateCash):
        updateUser = Datasource.createUserDetail(user.username, user.stepCount, updateCash)

        return updateUser