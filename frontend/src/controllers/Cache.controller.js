export default class CacheController {

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