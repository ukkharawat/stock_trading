<template>
  <div class="modal" @click="closeModal" :style="{'display': isModalOpen}">
    <div class="base-modal" @click.stop>
      <div class="modal-header">
        <h4 class="modal-title">Confirmation</h4>
        <button class="close" @click="closeModal">x</button>
      </div>

      <div class="modal-content" v-if="actionInfo != null">
        <b-row class="justify-content-sm-center">
          <b-col cols="8" class="remove-padding">
            <h2 class="cautions">
              Are you sure to {{actionInfo.action}} {{actionInfo.amount}} shares of {{actionInfo.symbol}} ?
              ({{formatAveragePrice(totalPrice)}})
            </h2>

            <b-row>
              <b-col cols="6">
                <b-button variant="primary" @click="submit">YES</b-button>
              </b-col>
              <b-col cols="6">
                <b-button variant="danger" @click="closeModal">No</b-button>
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
        commissionRate: 0.001578,
        vatRate: 1.07,
        actionInfo: null
      }
    },
    computed: {
      ...mapGetters([
        'getCash'
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
      openModal(actionInfo) {
        this.actionInfo = actionInfo
        this.isModalOpen = 'flex'
      },
      closeModal() {
        this.isModalOpen = 'none'
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
      formatAveragePrice(price) {
        if(!price)
          return '0'
        price = price.toFixed(2).toString()

        return price.replace(/(\d)(?=(\d{3})+\.)/g, '$1,') + " ฿"
      }
    }
  }
</script>