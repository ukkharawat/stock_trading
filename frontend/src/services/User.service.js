import axios from 'axios'

export default class UserService {

  static async register(apiURL, user) {
    let header = {
      'Content-Type': 'application/json'
    }

    return axios.post(apiURL, user, {
        headers: header
      })
      .then(response => response.data)
  }

  static async login(apiURL, user) {
    let header = {
      'Content-Type': 'application/json'
    }

    return axios.post(apiURL, user, {
        headers: header
      })
      .then(response => response.data)
  }

  static async logout(apiURL, token) {
    let header = {
      'Authorization': 'Token ' + token
    }

    return axios.get(apiURL, {
        headers: header
      })
      .then(response => response.data)
  }

  static async nextDay(apiURL, nextDayObject, token) {
    let header = {
      'Authorization': 'Token ' + token
    }

    return axios.put(apiURL, nextDayObject, {
        headers: header
      })
      .then(response => response.data)
  }

  static async getUserDetail(apiURL, token) {
    let header = {
      'Authorization': 'Token ' + token
    }

    return axios.get(apiURL, {
      headers: header
    }).then(response => response.data)
  }
}
