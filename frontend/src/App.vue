<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
    <nextDayButton></nextDayButton>
  </div>
</template>

<script>
  import navbar from '@/components/Navbar'
  import { mapGetters, mapActions } from 'vuex'
  import nextDayButton from '@/components/NextDayButton'
  import cacheController from '@/controllers/Cache.controller'
  import stockController from '@/controllers/Stock.controller'
  import userController from '@/controllers/User.controller'
  import stockDatasource from '@/datasources/Stock.datasource'

  export default {
    name: 'app',
    components: {
      navbar,
      nextDayButton
    },
    async created() {
      this.setStockList()
        .then(() => {
          if(cacheController.isLoggedIn()) {
            this.setUsername(cacheController.getUsername())
            this.updateUserDetail()
          }
        })

      
    },
    computed: {
      ...mapGetters([
        'isLoggedIn'
      ])
    },
    methods: {
      ...mapActions([
        'setUsername',
        'setStep',
        'updateStock',
        'setStock',
        'setCash'
      ]),
      updateUserDetail() {
        userController.getUserDetail()
          .then(response => {
            this.setCash(response.cash)
            this.setStep(response.stepCount)

            let stocks = response.portfolio.map(stock => stockDatasource.createChangedStockObject(stock))
            this.updateStock(stocks)
          })
      },
      setStockList() {
        return stockController.getStockList()
                .then(response => response.stockList)
                .then(stockLists => {
                  let stockList = stockLists.map(stock => stockDatasource.createDefaultStockList(stock))

                  this.setStock(stockList)
                })
      }
    }
  }
</script>
