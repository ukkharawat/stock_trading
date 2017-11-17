import userService from '@/services/User.service'
import userDataSource from '@/datasources/User.datasource'

export default class UserController {

    static login(username, password) {
        let loginURL = "http://localhost:8000/user/authentication"
        let loggedInUser = userDataSource.createLoggedInUserObject(username, password)

        return userService.login(loggedInUser, loginURL)
    }
}