export default class CacheController {

    static setUserCache(username, token) {
        localStorage.setItem("username", username)
        localStorage.setItem("token", token)
    }

    static setStep(step) {
        localStorage.setItem("step", step)
    }

    static getStep() {
        return localStorage.getItem("step")
    }

    static setCash(cash) {
        localStorage.setItem("cash", cash)
    }

    static getCash() {
        return localStorage.getItem("cash")
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