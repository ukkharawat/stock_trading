export default class StockDatasource {

  static createStockObject(action, symbol, fullname, amount, price) {
    return {
      "action": action,
      "symbol": symbol,
      "fullName": fullname,
      "amount": Number(amount),
      "price": Number(price)
    }
  }

  static createChangedStockObject(stock) {
    return {
      "symbol": stock.symbol,
      "amount": stock.volume,
      "averageBuyPrice": stock.averageBuyPrice
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
      "averageBuyPrice": 0
    }
  }
}
