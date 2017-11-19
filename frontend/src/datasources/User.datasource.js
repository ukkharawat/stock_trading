export default class UserDatasource {

    static createLoggedInUserObject(username, password) {
        return {
            username: username,
            password: password
        }
    }

}