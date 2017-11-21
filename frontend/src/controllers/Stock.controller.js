import stockService from '@/services/Stock.service'
import stockDataSource from '@/datasources/Stock.datasource'

export default class StockService {

  static getStockData(stockName) {
    let dataURL = "https://raw.githubusercontent.com/wasit7/data_analytics/master/demo/data_set/"+ stockName +".BK.csv"

    return stockService.getStockDataFromURL(dataURL)
      .then(csvData => {
        return stockDataSource.getStockJsonFromCSV(csvData)
      })
  }

  static findStockTradingCost(tradingAction) {
    return tradingAction.amount * tradingAction.price
  }

  static buyStock(stock, tradingAction) {
    let amount = stock.amount + tradingAction.amount
    let averagePrice = ((stock.averageBuyPrice * stock.amount) + (this.findStockTradingCost(tradingAction))) / (amount)

    return stockDataSource.createChangedStockObject(stock.shortName, amount, averagePrice)
  }

  static sellStock(stock, tradingAction) {
    let amount = stock.amount - tradingAction.amount

    return stockDataSource.createChangedStockObject(stock.shortName, amount, stock.averageBuyPrice)
  }
}
