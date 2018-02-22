import axios from 'axios'
import headerUtility from '@/utilities/Header.utility'

export default class StockService {

  static async getStockValue(URL, params) {
    return axios.get(URL, {
        params: params
      })
      .then(response => response.data)
  }

  static async buyStock(URL, tradingDetail, token) {

    return axios.post(URL, tradingDetail, {
        headers: headerUtility.createAuthorzation(token)
      })
      .then(response => response.data)
  }

  static async sellStock(URL, tradingDetail, token) {

    return axios.post(URL, tradingDetail, {
        headers: headerUtility.createAuthorzation(token)
      })
      .then(response => response.data)
  }

  static async getStockList(URL) {
    return axios.get(URL).then(response => response.data)
  }

  static async getComparedValue(URL, params) {
    return axios.get(URL, {
              params: params
            })
            .then(response => response.data)
  }
}
