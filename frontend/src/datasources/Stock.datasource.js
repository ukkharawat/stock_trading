export default class StockDatasource {

  static createStockObject(action, symbol, amount, averagePrice) {
    return {
      "action": action,
      "symbol": symbol,
      "amount": Number(amount),
      "averagePrice": Number(averagePrice)
    }
  }

  static createTradingStock(stock) {
    return {
      "symbol": stock.symbol,
      "volume": Math.abs(stock.changedAmount),
      "averagePrice": stock.averagePrice
    }
  }

  static createChangedStockObject(stock) {
    return {
      "symbol": stock.symbol,
      "amount": stock.volume
    }
  }

  static createUpdatedPriceStock(stock) {
    return {
      "symbol": stock.symbol,
      "averagePrice": stock.currentPrice,
      "diff": stock.diff,
      "diffPer": stock.diffPer
    }
  }

  static createDefaultStockList(stock) {
    return {
      "symbol": stock.symbol,
      "fullname": stock.fullname,
      "amount": 0,
      "changedAmount": 0,
      "price": 0,
      "averagePrice": 0,
      "diff": 0,
      "diffPer": 0
    }
  }

  static createUpdatedStock(stock, averagePrice) {
    return {
      "symbol": stock.symbol,
      "amount": stock.amount,
      "changedAmount": stock.changedAmount,
      "averagePrice": averagePrice
    }
  }
}
