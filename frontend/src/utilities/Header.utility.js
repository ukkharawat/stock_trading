export default class HeaderUtility {
  static createContentTypeJSON() {
    let header = {
      'Content-Type': 'application/json'
    }

    return header
  }

  static createAuthorzation(token) {
    let header = {
      'Authorization': 'Token ' + token
    }

    return header
  }
}
