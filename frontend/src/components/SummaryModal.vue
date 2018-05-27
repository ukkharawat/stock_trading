<template>
  <div>
    <div class="modal" @click="closeModal" :style="{'display': isModalOpen}">
      <div class="base-modal" @click.stop>
        <div class="modal-header">
          <h4 class="modal-title">Trading Summary</h4>
          <button class="close" @click="closeModal">x</button>
        </div>

        <div class="modal-content">
          <b-row class="justify-content-sm-center">
            <b-col cols="12" class="margin-col">
              <table class="table">
                <thead>
                  <tr>
                    <th><h4 class="text-left table-header">Items</h4></th>
                    <th><h4 class="text-right table-header">Price</h4></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="stock in getUnchangedStocks" :key="stock.symbol">
                    <td>
                      <p class="trading-stock text-left">{{isBuyOrSell(stock)}} {{Math.abs(stock.changedAmount)}} shares of {{stock.symbol}}</p>
                    </td>
                    <td>
                      <p class="trading-stock text-right">{{ formatPrice(findPrice(stock)) }} ฿</p>
                    </td>
                  </tr>
                  <tr class="double-underline">
                    <td>
                      <p class="trading-stock text-left"> Total </p>
                    </td>
                    <td>
                      <p class="trading-stock text-right"> {{ formatPrice(findTotalPrice()) }} ฿</p>
                    </td>
                  </tr>
                </tbody>
              </table>
            </b-col>
          </b-row>

          <h6 class="cautions">* including commission (0.157%)</h6>
          <h6 class="cautions padding-bottom">* including VAT (7% of commision)</h6>

          <b-row class="justify-content-sm-center">
            <b-col cols="8">
              <b-row>
                <b-col cols="6">
                  <b-button variant="primary" @click="proceed">Proceed</b-button>
                </b-col>
                <b-col cols="6">
                  <b-button variant="danger" @click="closeModal">Cancel</b-button>
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </div>
      </div>
    </div>
    <loader ref="loader"></loader>
  </div>
</template>

<script>
  import stockController from '@/controllers/Stock.controller'
  import userController from '@/controllers/User.controller'
  import stockDatasource from '@/datasources/Stock.datasource'
  import loader from '@/components/Loader.vue'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    data() {
      return {
        isModalOpen: 'none',
        commissionRate: 0.00157,
        vatRate: 1.07
      }
    },
    components: {
      loader
    },
    computed: {
      ...mapGetters([
        'getUnchangedStocks'
      ])
    },
    methods: {
      ...mapActions([
        'clearUnchangedStock',
        'increaseTrackingDay',
        'setCash',
        'updateStock'
      ]),
      openModal() {
        this.isModalOpen = 'flex'
      },
      closeModal() {
        this.isModalOpen = 'none'
      },
      isBuyOrSell(stock) {
        return stock.changedAmount > 0? 'Buy': 'Sell'
      },
      findPrice(stock) {
        let price = stock.changedAmount * stock.averagePrice * (1 + this.commissionRate * this.vatRate)

        return price
      },
      findTotalPrice() {
        let totalPrice = this.getUnchangedStocks.map(stock => this.findPrice(stock))
                                .reduce((sum, e) => sum + e, 0)

        return totalPrice
      },
      formatPrice(price) {
        if(!price)
          return '0'

        let result = price > 0 ? '-':'+'
        price = Math.abs(price).toFixed(2).toString()

        return result + price.replace(/(\d)(?=(\d{3})+\.)/g, '$1,')
      },
      async proceed() {
        await this.sellStock()
        await this.buyStock()
        await this.nextDay()
        this.clearUnchangedStock()
        this.closeModal()
        this.$refs.loader.activateLoader(1500)
      },
      sellStock() {
        let sellStock = this.getUnchangedStocks.filter(stock => stock.changedAmount < 0)
                          .map(stock => stockDatasource.createTradingStock(stock))

        if(sellStock.length != 0) 
          return stockController.sellStock(sellStock)
      },
      buyStock() {
        let buyStock = this.getUnchangedStocks.filter(stock => stock.changedAmount > 0)
                          .map(stock => stockDatasource.createTradingStock(stock))

        if(buyStock.length != 0)
          return stockController.buyStock(buyStock)
      },
      nextDay() {
        userController.nextDay()
          .then(() => this.updateCash())
          .then(() => this.updateComparedValue())
          .then(() => this.increaseTrackingDay())
      },
      updateCash() {
        userController.getUserDetail().then(response => this.setCash(response.cash))
      },
      updateComparedValue() {
        stockController.getComparedValue()
          .then(response => response.comparedValues)
          .then(comparedValues => {
            let stocks = comparedValues.map(comparedValue => stockDatasource.createUpdatedPriceStock(comparedValue))

            this.updateStock(stocks)
          })
      }
    }
  }
</script>