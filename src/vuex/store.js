import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  category: "",
  isModalOpen: false
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
  }
}

const actions = {
  setCategory: ({ commit }, current) => commit('SET_CATEGORY', current),
  openModal: ({ commit }) => commit('OPEN_MODAL'),
  closeModal: ({ commit }) => commit('CLOSE_MODAL')
}

const getters = {
  getCategory: state => state.category,
  getIsModalOpen: state => state.isModalOpen
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
