import Vue from 'vue'
import Router from 'vue-router'
import main from '@/components/mainPage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: main
    }
  ]
})
