import stockService from '@/services/Stock.service'
import stockDataSource from '@/datasources/Stock.datasource'
import cacheController from '@/controllers/Cache.controller'
import apiURL from '@/utilities/ApiURL.utility'

export default class StockController {

  static getStockValue(symbol) {
    let params = {
      'symbol': symbol
    }

    let token = cacheController.getToken()

    return stockService.getStockValue(apiURL.getStockValueURL, params, token)
  }

  static findStockTradingCost(tradingAction) {
    return tradingAction.amount * tradingAction.price
  }

  static buyStock(tradingActions) {
    let token = cacheController.getToken()
    let axiosObjects = tradingActions.map(action => {
      return stockService.buyStock(apiURL.buyStockURL, action, token)
    })

    return stockService.axiosMultiObject(axiosObjects)
  }

  static sellStock(tradingActions) {
    let token = cacheController.getToken()
    let axiosObjects = tradingActions.map(action => {
      return stockService.sellStock(apiURL.sellStockURL, action, token)
    })

    return stockService.axiosMultiObject(axiosObjects)
  }

  static getStockList() {
    return stockService.getStockList(apiURL.getStockListURL)
  }

  static getComparedValue(symbol) {
    let params = {
      'symbol': symbol
    }

    let token = cacheController.getToken()

    return stockService.getComparedValue(apiURL.getComparedValueURL, params, token)
  }
}
