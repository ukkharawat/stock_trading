import userService from '@/services/User.service'
import cacheController from '@/controller/Cache.controller'
import userDataSource from '@/datasources/User.datasource'
import apiURL from '@/utilities/ApiURL.utility'

export default class UserController {

    static login(username, password) {
        let userForm = userDataSource.createLoggedInUserObject(username, password)

        return userService.login(apiURL.loginURL, userForm)
    }

    static logout() {
        let token = cacheController.getToken()

        return userService.logout(apiURL.logoutURL, token)
    }

    static nextDay(cash, step) {
        let token = cacheController.getToken()
        let nextDayForm = userDataSource.createNextDayForm(cacheController.getUsername(), cash, step)

        return userService.nextDay(apiURL.nextDayURL, nextDayForm, token)
    }
}