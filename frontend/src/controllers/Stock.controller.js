import stockService from '@/services/Stock.service'
import stockDataSource from '@/datasources/Stock.datasource'
import cacheController from '@/controllers/Cache.controller'
import apiURL from '@/utilities/ApiURL.utility'
import ApiURL from '../utilities/ApiURL.utility';

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

  static buyStock(tradingAction) {
    let token = cacheController.getToken()
    
    return stockService.buyStock(ApiURL.buyStockURL, tradingAction, token)
  }

  static sellStock(tradingAction) {
    let token = cacheController.getToken()

    return stockService.sellStock(ApiURL.sellStockURL, tradingAction, token)
  }
}
