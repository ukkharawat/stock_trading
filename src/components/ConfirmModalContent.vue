<template>
  <div id="confirm-modal-content" v-if="actionInfo != null">
    <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-sm-6 remove-padding">
        <h2 class="cautions">
          Do you want to {{actionInfo.action}} {{actionInfo.amount}} shares of {{actionInfo.shortName}} ?
        </h2>

        <div class="row">
          <div class="col-sm-6">
            <confirmModalButton :buttonClass="'yes-button'"
                                @onClickEvent="handleClickYes"
                                :message="'YES'">
            </confirmModalButton>
          </div>
          <div class="col-sm-6">
            <confirmModalButton :buttonClass="'no-button'"
                                @onClickEvent="handleClickNo"
                                :message="'NO'">
            </confirmModalButton>
          </div>
        </div>
      </div>
      <div class="col-sm-3"></div>
    </div>
  </div>
</template>

<script>
  import confirmModalButton from '@/components/ConfirmModalButton'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    props: {
      actionInfo: {
        type: Object
      }
    },
    components: {
      confirmModalButton
    },
    computed: {
      ...mapGetters([
        'getNextActionInfo',
        'getStock'
      ])
    },
    methods: {
      ...mapActions([
        'closeModal',
        'updateCash',
        'updateStock',
        'updateCapital'
      ]),
      handleClickYes() {
        let action = this.getNextActionInfo.action

        if(action === "buy") {
          this.buyStock(this.getNextActionInfo)
        } else {
          this.sellStock(this.getNextActionInfo)
        }
      },
      handleClickNo() {
        this.closeModal()
      },
      createNewStock(shortName, amount, averagePrice) {
        return {
          "shortName": shortName,
          "amount": amount,
          "averageBuyPrice": averagePrice
        }
      },
      buyStock(stock) {
        let cost = stock.amount * stock.price
        let stocks = this.getCurrentStock(stock.shortName)
        let averagePrice = ((stocks.averageBuyPrice * stocks.amount) + (cost)) / (stocks.amount + stock.amount)
        let amount = stocks.amount + stock.amount
        let stockObject = this.createNewStock(stock.shortName, amount, averagePrice)

        this.updateVuex(-Math.abs(cost), stockObject)
      },
      sellStock(stock) {
        let cost = stock.amount * stock.price
        let stocks = this.getCurrentStock(stock.shortName)
        let amount = stocks.amount - stock.amount
        let stockObject = this.createNewStock(stock.shortName, amount, stocks.averageBuyPrice)

        this.updateVuex(Math.abs(cost), stockObject)
      },
      getCurrentStock(shortName) {
        let stocks = this.getStock
        let stockIndex = stocks.findIndex(stock => {
          return stock.shortName === shortName
        })

        return stocks[stockIndex]
      },
      updateVuex(cost, stock) {
        this.updateCash(cost)
        this.updateStock(stock)
        this.updateCapital()
        this.closeModal()
      }
    }
  }
</script>

<style>
  #confirm-modal-content {
    width: 100%;
    margin-top: 24px;
    padding-bottom: 24px;
  }

  .cautions {
    text-align: left;
    font-size: 24px;
    margin-bottom: 24px;
  }

  .remove-padding {
    padding: 0 8px;
  }
</style>
