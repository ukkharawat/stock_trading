import userService from '@/services/User.service'
import cacheController from '@/controllers/Cache.controller'
import userDataSource from '@/datasources/User.datasource'
import apiURL from '@/utilities/ApiURL.utility'

export default class UserController {

  static signUp(username, password) {
    let user = userDataSource.createUser(username, password)

    return userService.signUp(apiURL.signUpURL, user)
  }

  static login(username, password) {
    let userForm = userDataSource.createUser(username, password)

    return userService.login(apiURL.loginURL, userForm)
  }

  static logout() {
    let token = cacheController.getToken()

    return userService.logout(apiURL.logoutURL, token)
  }

  static nextDay() {
    let token = cacheController.getToken()

    return userService.nextDay(apiURL.nextDayURL, token)
  }

  static getUserDetail() {
    let token = cacheController.getToken()

    return userService.getUserDetail(apiURL.getUserDetailURL, token)
  }
}
