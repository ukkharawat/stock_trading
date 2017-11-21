import axios from 'axios'

export default class StockService {

  static async getStockDataFromURL(dataURL) {
    return axios.get(dataURL)
        .then(response => {
          return response.data
        })
  }
}
