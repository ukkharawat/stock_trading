let baseURL = "http://localhost:8000"

export default class ApiURL {

    static loginURL = `${baseURL}/user/login`
    static logoutURL = `${baseURL}/user/logout`
    static nextDayURL = `${baseURL}/user/nextStep`

}