<template>
  <div class="modal-content" v-if="actionInfo != null">
    <b-row class="justify-content-sm-center">
      <b-col cols="6" class="remove-padding">
        <h2 class="cautions">
          Do you want to {{actionInfo.action}} {{actionInfo.amount}} shares of {{actionInfo.symbol}} ?
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
    computed: {
      ...mapGetters([
        'getNextActionInfo',
        'getStock',
        'getCash'
      ])
    },
    methods: {
      ...mapActions([
        'closeModal',
        'setCash',
        'updateStock',
        'updateCapital'
      ]),
      submit() {
        let action = this.getNextActionInfo.action

        if(action === "buy") {
          this.buyStock(this.getNextActionInfo)
        } else {
          this.sellStock(this.getNextActionInfo)
        }
      },
      cancle() {
        this.closeModal()
      },
      buyStock(tradingAction) {
        let tradingObject = this.createTradingObject(tradingAction)

        stockController.buyStock(tradingObject)
          .then(response => {
            let updateData = stockDatasource.createChangedStockObject(response)

            this.setCash(response.cash)
            this.updateVuex(updateData)
          })
      },
      sellStock(tradingAction) {
        let tradingObject = this.createTradingObject(tradingAction)

        stockController.sellStock(tradingObject)
          .then(response => {
            let updateData = {
              'symbol': response.symbol,
              'amount': response.volume,
              'averageBuyPrice': response.averagePrice
            }

            this.setCash(response.cash)
            this.updateVuex(updateData)
          })
      },
      updateVuex(updateData) {
        this.updateStock(updateData)
        this.closeModal()
      },
      createTradingObject(tradingAction) {
        return {
          'symbol': tradingAction.symbol,
          'volume': tradingAction.amount,
          'averagePrice': tradingAction.price
        }
      }
    }
  }
</script>