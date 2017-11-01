import stockService from '@/services/Stock.service'
import stockDataSource from '@/datasources/Stock.datasource'

export default class StockService {

  static getStockData(stockName) {
    let dataURL = "https://raw.githubusercontent.com/wasit7/data_analytics/master/demo/data_set/"+ stockName +".BK.csv"

    return stockService.getStockDataFromURL(dataURL)
      .then(csvData => {
        return stockDataSource.getStockJsonFromCSV(csvData)
      })
  }
}
