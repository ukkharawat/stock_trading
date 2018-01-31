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
      await this.setStockList()

      if(cacheController.isLoggedIn()) {
        this.setUsername(cacheController.getUsername())
        this.updateUserDetail()
      }
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
            this.setStep(response.stepCount)
            let stocks = response.portfolio.map(stock => {
              return stockDatasource.createChangedStockObject(stock)
            })

            this.updateStock(stocks)
            this.setCash(response.cash)
          })
      },
      setStockList() {
        stockController.getStockList()
                .then(response => {
                  let defaultStockList = response.stockList.map(stock => {
                    return stockDatasource.createDefaultStockList(stock)
                  })

                  this.setStock(defaultStockList)
                })
      }
    }
  }
</script>
