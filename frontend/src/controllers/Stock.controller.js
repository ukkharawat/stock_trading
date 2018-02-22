import stockService from '@/services/Stock.service'
import stockDataSource from '@/datasources/Stock.datasource'
import cacheController from '@/controllers/Cache.controller'
import apiURL from '@/utilities/ApiURL.utility'
import ApiURL from '../utilities/ApiURL.utility';

export default class StockController {

  static getStockValue(symbol) {
    let params = {
      'symbol': symbol
    }

    let token = cacheController.getToken()

    return stockService.getStockValue(ApiURL.getStockValueURL, params, token)
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

  static getStockList() {
    return stockService.getStockList(ApiURL.getStockListURL)
  }

  static getComparedValue(symbol) {
    let params = {
      'symbol': symbol
    }

    let token = cacheController.getToken()

    return stockService.getComparedValue(ApiURL.getComparedValueURL, params, token)
  }
}
