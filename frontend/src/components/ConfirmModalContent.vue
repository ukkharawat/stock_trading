<template>
  <div id="confirm-modal-content" v-if="actionInfo != null">
    <b-row class="justify-content-sm-center">
      <b-col cols="6" class="remove-padding">
        <h2 class="cautions">
          Do you want to {{actionInfo.action}} {{actionInfo.amount}} shares of {{actionInfo.symbol}} ?
        </h2>

        <b-row>
          <b-col cols="6">
            <confirmModalButton :buttonClass="'yes-button'"
                                @onClickEvent="handleClickYes"
                                :message="'YES'">
            </confirmModalButton>
          </b-col>
          <b-col cols="6">
            <confirmModalButton :buttonClass="'no-button'"
                                @onClickEvent="handleClickNo"
                                :message="'NO'">
            </confirmModalButton>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </div>
</template>

<script>
  import confirmModalButton from '@/components/ConfirmModalButton'
  import stockController from '@/controllers/Stock.controller'
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
      buyStock(tradingAction) {
        let tradingObject = this.createTradingObject(tradingAction)

        stockController.buyStock(tradingObject)
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
