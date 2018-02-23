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
      "volume": stock.changedAmount,
      "averagePrice": stock.averagePrice
    }
  }

  static createChangedStockObject(stock) {
    return {
      "symbol": stock.symbol,
      "amount": stock.volume,
      "averagePrice": stock.averagePrice
    }
  }

  static createDefaultStockList(stock) {
    return {
      "symbol": stock.symbol,
      "fullname": stock.fullname,
      "amount": 0,
      "changedAmount": 0,
      "price": 0,
      "averagePrice": 0
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
