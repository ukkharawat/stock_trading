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
  isModalOpen: false,
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
  OPEN_MODAL(state) {
    state.isModalOpen = true
  },
  CLOSE_MODAL(state) {
    state.isModalOpen = false
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
  openModal: ({ commit }) => commit('OPEN_MODAL'),
  closeModal: ({ commit }) => commit('CLOSE_MODAL'),
  buyStock: ({ commit }, stock) => commit('BUY_STOCK', stock),
  sellStock: ({ commit }, stock) => commit('SELL_STOCK', stock),
  updateCapital: ({ commit }, stock) => commit('UPDATE_CAPITAL'),
  updatePrice: ({ commit }, stock) => commit('UPDATE_PRICE', stock)
}

const getters = {
  getCategory: state => state.category,
  getIsModalOpen: state => state.isModalOpen,
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
