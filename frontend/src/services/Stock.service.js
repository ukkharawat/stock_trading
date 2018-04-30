import axios from 'axios'
import headerUtility from '@/utilities/Header.utility'

export default class StockService {

  static async getStockValue(URL, params, token) {
    let headers = token !== null? headerUtility.createAuthorzation(token): {}

    return axios.get(URL, { 
        params: params,
        headers: headers
      })
      .then(response => response.data)
  }

  static async buyStock(URL, tradingDetail, token) {
    
    return axios.post(URL, tradingDetail, {
        headers: headerUtility.createAuthorzation(token)
      })
  }

  static async sellStock(URL, tradingDetail, token) {

    return axios.post(URL, tradingDetail, {
        headers: headerUtility.createAuthorzation(token)
      })
  }

  static async getStockList(URL) {
    return axios.get(URL).then(response => response.data)
  }

  static async getComparedValue(URL, token) {
    let headers = token !== null? headerUtility.createAuthorzation(token): {}

    return axios.get(URL, {
        headers: headers
      }).then(response => {
        return response.data
      })
  }

  static async axiosMultiObject(objects) {
    return axios.all(objects).then(axios.spread((acct, perms) => {
      return acct
    }))
  }
}
