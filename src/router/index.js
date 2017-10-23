import Vue from 'vue'
import Router from 'vue-router'
import AmChartComponent from '@/components/AmChartComponent'

Vue.use(Router)

export default new Router({
  routes: [
    {
    	path: '/amchart',
    	name: 'AmChart',
    	component: AmChartComponent
    }
  ]
})
