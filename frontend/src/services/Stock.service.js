import axios from 'axios'

export default class StockService {

  static async getStockDataFromURL(dataURL) {
    return axios.get(dataURL)
        .then(response => {
          return response.data
        })
  }

  static async buyStock(URL, tradingDetail, token) {
    let header = {
        'Authorization': 'Token ' + token
    }
    
    return axios.post(URL, tradingDetail, {headers: header})
      .then(response => {
        return response.data
      })
  }

  static async sellStock(URL, tradingDetail, token) {
    let header = {
        'Authorization': 'Token ' + token
    }
    
    return axios.post(URL, tradingDetail, {headers: header})
      .then(response => {
        return response.data
      })
  }
}
