<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
    <summaryFooter></summaryFooter>
  </div>
</template>

<script>
  import navbar from '@/components/Navbar'
  import summaryFooter from '@/components/SummaryFooter'
  import { mapGetters, mapActions } from 'vuex'
  import cacheController from '@/controllers/Cache.controller'
  import stockController from '@/controllers/Stock.controller'
  import userController from '@/controllers/User.controller'
  import stockDatasource from '@/datasources/Stock.datasource'

  export default {
    name: 'app',
    components: {
      navbar,
      summaryFooter
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
        'updateStock',
        'setStock',
        'setCash'
      ]),
      updateUserDetail() {
        userController.getUserDetail()
          .then(response => {
            this.setCash(response.cash)

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
