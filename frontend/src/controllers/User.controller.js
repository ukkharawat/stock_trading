import userService from '@/services/User.service'
import userDataSource from '@/datasources/User.datasource'

export default class UserController {

    static login(username, password) {
        let loginURL = "http://localhost:8000/user/login"
        let loggedInUser = userDataSource.createLoggedInUserObject(username, password)

        return userService.login(loggedInUser, loginURL)
    }

    static logout() {
        let logoutURL = "http://localhost:8000/user/logout"
        let token = this.getToken()

        return userService.logout(logoutURL, token)
    }

    static setUserCache(username, token) {
        localStorage.setItem("username", username)
        localStorage.setItem("token", token)
    }

    static isLoggedIn() {
        return localStorage.getItem("username") != null && localStorage.getItem("username") != undefined 
    }

    static getUsername() {
        return localStorage.getItem("username")
    }

    static getToken() {
        return localStorage.getItem("token")
    }

    static clearUserCache() {
        localStorage.clear()
    }
}