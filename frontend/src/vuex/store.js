import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  stocks: null,
  cash: null,
  username: null,
  unchangedStocks: [],
  trackingDay: 0
}

const mutations = {
  UPDATE_STOCK(state, stocks) {
    stocks.forEach((stock) => {
      let stockIndex = state.stocks.findIndex(stateStock => stateStock.symbol === stock.symbol)

      state.stocks[stockIndex].amount = stock.amount
      state.stocks[stockIndex].averagePrice = stock.averagePrice
      state.stocks[stockIndex].changedAmount = 0
    })
  },
  SET_STOCK(state, stocks) {
    state.stocks = stocks
  },
  SET_USERNAME(state, username) {
    state.username = username
  },
  SET_CASH(state, cash) {
    state.cash = cash
  },
  UPDATE_UNCHANGED_STOCK(state, updatedStock) {
    let stockIndex = state.unchangedStocks.findIndex(stock => stock.symbol === updatedStock.symbol)

    if( stockIndex != -1)
      state.unchangedStocks.splice(stockIndex, 1)

    if( updatedStock.changedAmount != 0)
      state.unchangedStocks.push(updatedStock)
  },
  INCREASE_TRACKING_DAY(state) {
    state.trackingDay += 1
  },
  CLEAR_UNCHANGED_STOCK(state) {
    state.unchangedStocks = []
  }
}

const actions = {
  updateStock: ({ commit }, stocks) => commit('UPDATE_STOCK', stocks),
  updateUnchangedStock: ({ commit }, updatedStock) => commit('UPDATE_UNCHANGED_STOCK', updatedStock),
  clearUnchangedStock: ({ commit }) => commit('CLEAR_UNCHANGED_STOCK'),
  setStock: ({ commit }, stocks) => commit('SET_STOCK', stocks),
  setUsername: ({ commit }, username) => commit('SET_USERNAME', username),
  setCash: ({ commit }, cash) => commit('SET_CASH', cash),
  increaseTrackingDay: ({ commit }) => commit('INCREASE_TRACKING_DAY')
}

const getters = {
  getStock: state => state.stocks,
  getUsername: state => state.username,
  getCash: state => state.cash,
  isLoggedIn: state => state.username !== null,
  getUnchangedStocks: state => state.unchangedStocks,
  getTrackingDay: state => state.trackingDay
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
