import Vue from 'vue'
import Router from 'vue-router'
import mainPage from '@/components/MainPage'
import portfolioPage from '@/components/PortfolioPage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: mainPage
    },
    {
      path: '/portfolio',
      component: portfolioPage
    }
  ]
})
