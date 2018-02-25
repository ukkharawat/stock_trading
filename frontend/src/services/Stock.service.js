import axios from 'axios'
import headerUtility from '@/utilities/Header.utility'

export default class StockService {

  static async getStockValue(URL, params, token) {
    return axios.get(URL, {
        params: params,
        headers: headerUtility.createAuthorzation(token)
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
    return axios.get(URL, {
              headers: headerUtility.createAuthorzation(token)
            })
            .then(response => response.data)
  }

  static async axiosMultiObject(objects) {
    return axios.all(objects).then(axios.spread((acct, perms) => {
      return acct
    }))
  }
}
