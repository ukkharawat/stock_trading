<template>
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
                  <th>
                    <h4 class="text-left table-header">Items</h4>
                  </th>
                  <th>
                    <h4 class="text-right table-header">Price</h4>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="stock in getUnchangedStocks" :key="stock.symbol">
                  <td>
                    <p class="trading-stock text-left">
                      {{isBuyOrSell(stock)}} {{Math.abs(stock.changedAmount)}} shares of {{stock.symbol}}
                    </p>
                  </td>
                  <td>
                    <p class="trading-stock text-right">
                      {{ formatPrice(Math.abs(findPrice(stock))) }} ฿
                    </p>
                  </td>
                </tr>
                <tr class="double-underline">
                  <td>
                    <p class="trading-stock text-left"> Total </p>
                  </td>
                  <td>
                    <p class="trading-stock text-right"> {{findTotalPrice()}} ฿</p>
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
                <b-button variant="primary" @click="submit">Proceed</b-button>
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
</template>

<script>
  import stockController from '@/controllers/Stock.controller'
  import stockDatasource from '@/datasources/Stock.datasource'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    data() {
      return {
        isModalOpen: 'none',
        commissionRate: 0.00157,
        vatRate: 1.07
      }
    },
    computed: {
      ...mapGetters([
        'getUnchangedStocks'
      ]),
      totalPrice() {
        if(this.actionInfo.action === "buy") {
          return  (this.actionInfo.amount * this.actionInfo.averagePrice) * (1 + this.commissionRate * this.vatRate)
        } else {
          return  (this.actionInfo.amount * this.actionInfo.averagePrice) * (1 - this.commissionRate * this.vatRate)
        }
      }
    },
    methods: {
      ...mapActions([
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
        let price = stock.changedAmount * stock.price * (1 + this.commissionRate * this.vatRate)

        return price
      },
      findTotalPrice() {
        let totalPrice = this.getUnchangedStocks.map(stock => this.findPrice(stock))
                                .reduce((sum, e) => sum + e, 0)

        let result = totalPrice > 0 ? '': '-'

        return result + this.formatPrice(Math.abs(totalPrice))
      },
      submit() {
        let action = this.actionInfo.action

        if(action === "buy") {
          this.buyStock(this.actionInfo)
        } else {
          this.sellStock(this.actionInfo)
        }
      },
      buyStock(tradingAction) {
        let tradingObject = stockDatasource.createTradingStock(tradingAction)
        
        stockController.buyStock(tradingObject)
          .then(response => {
            this.updateAfterTakeAction(response)
            this.closeModal()
          })
      },
      sellStock(tradingAction) {
        let tradingObject = stockDatasource.createTradingStock(tradingAction)

        stockController.sellStock(tradingObject)
          .then(response => {
            this.updateAfterTakeAction(response)
            this.closeModal()
          })
      },
      updateAfterTakeAction(response) {
        this.setCash(response.cash)

        let updateDetail = []
        updateDetail.push(stockDatasource.createChangedStockObject(response))
        this.updateStock(updateDetail)
      },
      formatPrice(price) {
        if(!price)
          return '0'
        price = price.toFixed(2).toString()

        return price.replace(/(\d)(?=(\d{3})+\.)/g, '$1,')
      }
    }
  }
</script>