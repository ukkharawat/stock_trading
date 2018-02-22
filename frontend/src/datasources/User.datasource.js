export default class UserDatasource {

  static createUser(username, password) {
    return {
      username: username,
      password: password
    }
  }
}
