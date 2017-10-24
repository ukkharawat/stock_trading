import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  category: ""
}

const mutations = {
  SET_CATEGORY(state, current) {
    state.category = current
  }
}

const actions = {
  setCategory: ({ commit }, current) => commit('SET_CATEGORY', current)
}

const getters = {
  getCategory: state => state.category
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
