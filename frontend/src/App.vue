<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
    <modal>
      <logInModal v-show="getIsLogInModal"></logInModal>
      <confirmModal v-show="getIsConfirmModal"></confirmModal>
    </modal>
    <nextDayButton></nextDayButton>
  </div>
</template>

<script>
  import modal from '@/components/Modal'
  import navbar from '@/components/Navbar'
  import logInModal from '@/components/LogInModal'
  import confirmModal from '@/components/ConfirmModal'
  import { mapGetters, mapActions } from 'vuex'
  import nextDayButton from '@/components/NextDayButton'
  import cacheController from '@/controllers/Cache.controller'
  import stockController from '@/controllers/Stock.controller'
  import userController from '@/controllers/User.controller'
  import stockDatasource from '@/datasources/Stock.datasource'

  export default {
    name: 'app',
    components: {
      modal,
      navbar,
      logInModal,
      confirmModal,
      nextDayButton
    },
    created() {
      this.setStockList()

      if(cacheController.isLoggedIn()) {
        this.setUsername(cacheController.getUsername())
        this.updateUserDetail()
      }
    },
    computed: {
      ...mapGetters([
        'getIsLogInModal',
        'getIsConfirmModal',
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

            let stock = stockDatasource.createChangedStockObject(
              response.portfolio[0].symbol,
              response.portfolio[0].volume,
              response.portfolio[0].averagePrice
            )

            this.updateStock(stock)
            this.setCash(response.cash)
          })
      },
      setStockList() {
        stockController.getStockList()
          .then(response => {
            let defaultStockList = response.stockList.map(stock => {
              return stockDatasource.createDefaultStockList(stock.name, stock.fullname)
            })

            this.setStock(defaultStockList)
          })
      }
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  .row {
    margin-right: 0 !important;
  }
</style>
