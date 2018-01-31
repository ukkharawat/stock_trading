import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  stocks: null,
  step: 1,
  cash: null,
  username: null,
  category: null
}

const mutations = {
  UPDATE_STOCK(state, stocks) {
    stocks.forEach((stock) => {
      let stockIndex = state.stocks.findIndex(stateStock => stateStock.symbol === stock.symbol)

      state.stocks[stockIndex].amount = stock.amount
      state.stocks[stockIndex].averagePrice = stock.averagePrice
    })
  },
  SET_STOCK(state, stocks) {
    state.stocks = stocks
  },
  SET_USERNAME(state, username) {
    state.username = username
  },
  SET_STEP(state, step) {
    state.step = step
  },
  SET_CASH(state, cash) {
    state.cash = cash
  },
  SET_CURRENT_CATEGORY(state, category) {
    state.category = category
  }
}

const actions = {
  updateStock: ({ commit }, stocks) => commit('UPDATE_STOCK', stocks),
  setStock: ({ commit }, stocks) => commit('SET_STOCK', stocks),
  setUsername: ({ commit }, username) => commit('SET_USERNAME', username),
  setStep: ({ commit }, step) => commit('SET_STEP', step),
  setCash: ({ commit }, cash) => commit('SET_CASH', cash),
  setCurrentCategory: ({ commit }, category) => commit('SET_CURRENT_CATEGORY', category)
}

const getters = {
  getStock: state => state.stocks,
  getUsername: state => state.username,
  getCash: state => state.cash,
  getStep: state => state.step,
  getCurrentCategory: state => state.category,
  isLoggedIn: state => state.username !== null
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
