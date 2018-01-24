<template>
  <div class="modal-content" v-if="actionInfo != null">
    <b-row class="justify-content-sm-center">
      <b-col cols="8" class="remove-padding">
        <h2 class="cautions">
          Do you want to {{actionInfo.action}} {{actionInfo.amount}} shares of {{actionInfo.symbol}} ?
          ({{formatAveragePrice(totalPrice)}})
        </h2>

        <b-row>
          <b-col cols="6">
            <b-button variant="primary" @click="submit">YES</b-button>
          </b-col>
          <b-col cols="6">
            <b-button variant="danger" @click="cancel">No</b-button>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </div>
</template>

<script>
  import stockController from '@/controllers/Stock.controller'
  import stockDatasource from '@/datasources/Stock.datasource'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    props: {
      actionInfo: {
        type: Object
      }
    },
    data() {
      return {
        commissionRate: 0.001578,
        vatRate: 1.07
      }
    },
    computed: {
      ...mapGetters([
        'getCash'
      ]),
      totalPrice() {
        if(this.actionInfo.action === "buy") {
          return  (this.actionInfo.amount * this.actionInfo.averagePrice * this.commissionRate * this.vatRate) +
                  (this.actionInfo.amount * this.actionInfo.averagePrice)
        } else {
          return  (this.actionInfo.amount * this.actionInfo.averagePrice) - 
                  (this.actionInfo.amount * this.actionInfo.averagePrice * this.commissionRate * this.vatRate)
        }
      }
    },
    methods: {
      ...mapActions([
        'closeModal',
        'setCash',
        'updateStock'
      ]),
      submit() {
        let action = this.actionInfo.action

        if(action === "buy") {
          this.buyStock(this.actionInfo)
        } else {
          this.sellStock(this.actionInfo)
        }
      },
      cancel() {
        this.closeModal()
      },
      buyStock(tradingAction) {
        let tradingObject = stockDatasource.createTradingStock(tradingAction)
        
        stockController.buyStock(tradingObject)
          .then(response => {
            let updateData = stockDatasource.createChangedStockObject(response)

            this.setCash(response.cash)
            this.updateVuex(updateData)
          })
      },
      sellStock(tradingAction) {
        let tradingObject = stockDatasource.createTradingStock(tradingAction)

        stockController.sellStock(tradingObject)
          .then(response => {
            let updateData = stockDatasource.createChangedStockObject(response)

            this.setCash(response.cash)
            this.updateVuex(updateData)
          })
      },
      updateVuex(updateData) {
        this.updateStock(updateData)
        this.closeModal()
      },
      formatAveragePrice(price) {
        if(!price)
          return '0'
        price = price.toFixed(2).toString()

        return price.replace(/(\d)(?=(\d{3})+\.)/g, '$1,') + " ฿"
      }
    }
  }
</script>