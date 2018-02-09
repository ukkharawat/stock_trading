import axios from 'axios'
import headerUtility from '@/utilities/Header.utility'

export default class UserService {

  static async signUp(apiURL, user) {

    return axios.post(apiURL, user, {
        headers: headerUtility.createContentTypeJSON()
      })
      .then(response => response.data)
  }

  static async login(apiURL, user) {

    return axios.post(apiURL, user, {
        headers: headerUtility.createContentTypeJSON()
      })
      .then(response => response.data)
  }

  static async logout(apiURL, token) {

    return axios.get(apiURL, {
        headers: headerUtility.createAuthorzation(token)
      })
      .then(response => response.data)
  }

  static async nextDay(apiURL, nextDayObject, token) {

    return axios.put(apiURL, nextDayObject, {
        headers: headerUtility.createAuthorzation(token)
      })
      .then(response => response.data)
  }

  static async getUserDetail(apiURL, token) {
    return axios.get(apiURL, {
        headers: headerUtility.createAuthorzation(token)
      }).then(response => response.data)
  }
}
