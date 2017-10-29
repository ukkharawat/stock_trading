import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  category: "",
  isModalOpen: false,
  holdingStocks: []
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
    let stockIndex = state.holdingStocks.findIndex( holdingStock => {
      return holdingStock.name === stock.name
    })

    if(stockIndex >= 0) {
      state.holdingStocks[stockIndex].amount += stock.amount
    } else {
      state.holdingStocks.push(stock)
    }
  },
  SELL_STOCK(state, stock) {
    let stockIndex = state.holdingStocks.findIndex( holdingStock => {
      return holdingStock.name === stock.name
    })

    state.holdingStocks[stockIndex].amount -= stock.amount

    if(state.holdingStocks[stockIndex].amount === 0) {
      state.holdingStocks.splice(stockIndex, 1)
    }
  }
}

const actions = {
  setCategory: ({ commit }, current) => commit('SET_CATEGORY', current),
  openModal: ({ commit }) => commit('OPEN_MODAL'),
  closeModal: ({ commit }) => commit('CLOSE_MODAL'),
  buyStock: ({ commit }, stock) => commit('BUY_STOCK', stock),
  sellStock: ({ commit }, stock) => commit('SELL_STOCK', stock)

}

const getters = {
  getCategory: state => state.category,
  getIsModalOpen: state => state.isModalOpen,
  getHoldingStock: state => state.holdingStocks
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
