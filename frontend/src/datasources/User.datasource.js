export default class UserDatasource {

  static createUser(username, password) {
    return {
      username: username,
      password: password
    }
  }

  static createNextDayForm(username, cash, step) {
    return {
      username: username,
      cash: cash,
      stepCount: step + 1
    }
  }
}
