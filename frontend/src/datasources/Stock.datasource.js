export default class StockDatasource {

  static createStockObject(action, name, fullname, amount, price) {
    return {
      "action": action,
      "shortName": name,
      "fullName": fullname,
      "amount": Number(amount),
      "price": Number(price)
    }
  }

  static createChangedStockObject(shortName, amount, averageBuyPrice) {
    return {
      "shortName": shortName,
      "amount": amount,
      "averageBuyPrice": averageBuyPrice
    }
  }

  static createDefaultStockList(stock) {
    return {
      "shortName": stock.name,
      "fullName": stock.fullname,
      "industry": stock.industry,
      "sector": stock.sector,
      "amount": 0,
      "price": 0,
      "averageBuyPrice": 0
    }
  }
}
