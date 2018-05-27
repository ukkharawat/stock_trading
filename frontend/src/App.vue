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
      await this.setStockList()
      await this.getComparedValue()
      if(cacheController.isLoggedIn()) {
        this.setUsername(cacheController.getUsername())
        await this.updateUserDetail()
        this.increaseTrackingDay()
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
        'updateStock',
        'setStock',
        'setCash'
      ]),
      updateUserDetail() {
        return userController.getUserDetail()
                .then(response => {
                  this.setCash(response.cash)

                  let stocks = response.portfolio.map(stock => stockDatasource.createChangedStockObject(stock))
                  this.updateStock(stocks)
                })
      },
      getComparedValue() {
        return stockController.getComparedValue()
                .then(response => response.comparedValues)
                .then(comparedValues => {
                  let stocks = comparedValues.map(comparedValue => stockDatasource.createUpdatedPriceStock(comparedValue))

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
