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
      "volume": stock.amount,
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
      "symbol": stock.name,
      "fullName": stock.fullname,
      "industry": stock.industry,
      "sector": stock.sector,
      "amount": 0,
      "price": 0,
      "averagePrice": 0
    }
  }
}
