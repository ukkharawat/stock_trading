let baseURL = "http://localhost:8000"

export default class ApiURL {

  static signUpURL = `${baseURL}/user/signup`
  static loginURL = `${baseURL}/user/login`
  static logoutURL = `${baseURL}/user/logout`
  static nextDayURL = `${baseURL}/user/nextStep`
  static getUserDetailURL = `${baseURL}/user/detail`
  static buyStockURL = `${baseURL}/stock/buy`
  static sellStockURL = `${baseURL}/stock/sell`
  static getStockListURL = `${baseURL}/stock/list`
  static getStockValueURL = `${baseURL}/stock/stockValue`
  static getComparedValueURL = `${baseURL}/stock/comparedValue`
}
