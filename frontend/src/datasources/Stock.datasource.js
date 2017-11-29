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
}
