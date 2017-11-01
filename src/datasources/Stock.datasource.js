export default class StockService {

  static getStockJsonFromCSV(csvData) {
    let csvDataEachLines = csvData.split("\n")
    let stockJson = []

    for(let i = 1 ; i < csvDataEachLines.length ; i++) {
      let dataEachColumns = csvDataEachLines[i].split(",")
      stockJson.push(
        {
          "Date": dataEachColumns[0],
          "Open": dataEachColumns[1],
          "High": dataEachColumns[2],
          "Low": dataEachColumns[3],
          "Close": dataEachColumns[4],
          "Adj": dataEachColumns[5],
          "Volume": dataEachColumns[6],
        }
      )
    }

    return stockJson
  }

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
