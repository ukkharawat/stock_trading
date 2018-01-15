import axios from 'axios'

export default class StockService {

  static async getStockValue(URL, params) {
    return axios.get(URL, {
        params: params
      })
      .then(response => response.data)
  }

  static async buyStock(URL, tradingDetail, token) {
    let header = {
      'Authorization': 'Token ' + token
    }

    return axios.post(URL, tradingDetail, {
        headers: header
      })
      .then(response => response.data)
  }

  static async sellStock(URL, tradingDetail, token) {
    let header = {
      'Authorization': 'Token ' + token
    }

    return axios.post(URL, tradingDetail, {
        headers: header
      })
      .then(response => response.data)
  }

  static async getStockList(URL) {
    return axios.get(URL).then(response => response.data)
  }
}
