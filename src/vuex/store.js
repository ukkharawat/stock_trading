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
  stocks: [ {
    "shortName": "CHOTI",
    "fullName": "Kiang Huat Sea Gull Trading Frozen Food",
    "amount": 0,
    "price": 0,
    "averageBuyPrice": 0
  } ],
  capital: 10000,
  cash: 10000
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
  OPEN_CONFIRM_MODAL(state) {
    state.isConfirmModal = true
  },
  BUY_STOCK(state, stock) {
    let stockIndex = findIndexOfStocks(stock.shortName)

    state.cash -= stock.amount * stock.price
    state.stocks[stockIndex].averageBuyPrice = ((state.stocks[stockIndex].averageBuyPrice * state.stocks[stockIndex].amount)
      + (stock.amount * stock.price))
      /(state.stocks[stockIndex].amount + stock.amount)

    state.stocks[stockIndex].amount += stock.amount
  },
  SELL_STOCK(state, stock) {
    let stockIndex = findIndexOfStocks(stock.shortName)

    state.cash += stock.amount * stock.price
    state.stocks[stockIndex].amount -= stock.amount
    if(state.stocks[stockIndex].amount === 0)
      state.stocks[stockIndex].averageBuyPrice = 0
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
  }
}

const actions = {
  setCategory: ({ commit }, current) => commit('SET_CATEGORY', current),
  closeModal: ({ commit }) => commit('CLOSE_MODAL'),
  openLogInModal: ({ commit }) => commit('OPEN_LOG_IN_MODAL'),
  openConfirmModal: ({ commit }) => commit('OPEN_CONFIRM_MODAL'),
  buyStock: ({ commit }, stock) => commit('BUY_STOCK', stock),
  sellStock: ({ commit }, stock) => commit('SELL_STOCK', stock),
  updateCapital: ({ commit }, stock) => commit('UPDATE_CAPITAL'),
  updatePrice: ({ commit }, stock) => commit('UPDATE_PRICE', stock)
}

const getters = {
  getCategory: state => state.category,
  getIsLogInModal: state => state.isLogInModal,
  getIsConfirmModal: state => state.isConfirmModal,
  getStock: state => state.stocks,
  getHoldingStock: state => state.stocks.filter(stock => stock.amount !== 0),
  getCapital: state => state.capital,
  getCash: state=> state.cash
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
