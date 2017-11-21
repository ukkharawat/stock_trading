import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

function findIndexOfStocks(stockName) {
  return state.stocks.findIndex(stock => {
    return stock.shortName === stockName
  })
}

const state = {
  category: "",
  isLogInModal: false,
  isConfirmModal: false,
  nextActionInfo: null,
  stocks: [ {
    "shortName": "CHOTI",
    "fullName": "Kiang Huat Sea Gull Trading Frozen Food",
    "amount": 0,
    "price": 0,
    "averageBuyPrice": 0
  } ],
  capital: 10000,
  step: null,
  cash: null,
  username: null
}

const mutations = {
  SET_CATEGORY(state, current) {
    state.category = current
  },
  CLOSE_MODAL(state) {
    state.isLogInModal = false
    state.isConfirmModal = false
  },
  OPEN_LOG_IN_MODAL(state) {
    state.isLogInModal = true
  },
  OPEN_CONFIRM_MODAL(state, nextActionInfo) {
    state.isConfirmModal = true
    state.nextActionInfo = nextActionInfo
  },
  UPDATE_CAPITAL(state) {
    state.capital = state.cash
    state.capital += state.stocks.map(stock => stock.amount * stock.price).reduce((sum, value) => {
      return sum + value
    })
  },
  UPDATE_PRICE(state, stock) {
    let stockIndex = findIndexOfStocks(stock.shortName)

    state.stocks[stockIndex].price = stock.price
  },
  UPDATE_STOCK(state, stock) {
    let stockIndex = findIndexOfStocks(stock.shortName)

    state.stocks[stockIndex].amount = stock.amount
    state.stocks[stockIndex].averageBuyPrice = stock.averageBuyPrice
  },
  SET_USERNAME(state, username) {
    state.username = username
  },
  SET_STEP(state, step) {
    state.step = step
  },
  SET_CASH(state, cash) {
    state.cash = cash
    state.capital = cash
  }
}

const actions = {
  setCategory: ({ commit }, current) => commit('SET_CATEGORY', current),
  closeModal: ({ commit }) => commit('CLOSE_MODAL'),
  openLogInModal: ({ commit }) => commit('OPEN_LOG_IN_MODAL'),
  openConfirmModal: ({ commit }, nextActionInfo) => commit('OPEN_CONFIRM_MODAL', nextActionInfo),
  updateCapital: ({ commit }, stock) => commit('UPDATE_CAPITAL'),
  updatePrice: ({ commit }, stock) => commit('UPDATE_PRICE', stock),
  updateStock: ({ commit }, stock) => commit('UPDATE_STOCK', stock),
  setUsername: ({ commit }, username) => commit('SET_USERNAME', username),
  setStep: ({ commit }, step) => commit('SET_STEP', step),
  setCash: ({ commit }, cash) => commit('SET_CASH', cash),
}

const getters = {
  getCategory: state => state.category,
  getIsModalOpen: state => { return state.isConfirmModal || state.isLogInModal},
  getIsLogInModal: state => state.isLogInModal,
  getIsConfirmModal: state => state.isConfirmModal,
  getStock: state => state.stocks,
  getHoldingStock: state => state.stocks.filter(stock => stock.amount !== 0),
  getCapital: state => state.capital,
  getNextActionInfo: state => state.nextActionInfo,
  getUsername: state => state.username,
  getCash: state => state.cash,
  getStep: state => state.step,
  isLoggedIn: state => state.username !== null
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
