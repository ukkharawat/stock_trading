<template>
  <div>
    <div class="footer" v-if="isLoggedIn">
      <div class="row">
          <b-col cols="7" class="text-left" >
              <p class="summary cursor-default" v-if="buyAmount == 0 && sellAmount == 0">No Trading Today?</p>
              <p class="summary cursor-default" v-if="buyAmount != 0">Buy {{ formatNumber(buyAmount) }} shares,</p>
              <p class="summary cursor-default" v-if="sellAmount != 0">Sell {{ formatNumber(sellAmount) }} shares,</p>
              <p class="summary cursor-default" v-if="totalPrice > 0">Total price {{ formatPrice(totalPrice) }} baht</p>
              <p class="summary cursor-default" v-if="totalPrice < 0">Gain {{ formatPrice(Math.abs(totalPrice)) }} baht</p>
          </b-col>
          <b-col cols="5" class="text-right">
              <p class="summary complete-trading footer-button" v-if="buyAmount == 0 && sellAmount == 0" @click="nextDay">next <i class="fas fa-angle-right"></i></p>
              <p class="summary complete-trading footer-button" v-else-if="totalPrice <= getCash" @click="openModal">complete trading <i class="fas fa-check"></i></p>
              <p class="summary" v-else>check your cash</p>
          </b-col>
      </div>
    </div>
    <summaryModal ref="summaryModal"></summaryModal>
    <loader ref="loader"></loader>
  </div>
</template>
<script>
  import { mapGetters, mapActions } from 'vuex'
  import summaryModal from '@/components/SummaryModal'
  import userController from '@/controllers/User.controller'
  import loader from '@/components/Loader.vue'

  export default {
    data() {
        return {
            buyAmount: 0,
            sellAmount: 0,
            totalPrice: 0,
            vatRate: 1.07,
            commissionRate: 0.00157
        }
    },
    components: {
        summaryModal,
        loader
    },
    computed: {
        ...mapGetters([
            'getUnchangedStocks',
            'getCash',
            'isLoggedIn'
        ]),
        isUnchangedStock() {
            return this.getUnchangedStocks.length != 0
        }
    },
    watch: {
        getUnchangedStocks: {
            handler(val) {
                this.updateBuyAmount(val.filter(stock => stock.changedAmount > 0))
                this.updateSellAmount(val.filter(stock => stock.changedAmount < 0))
                this.findTotalPrice(val)
            }
        },
        deep: true
    },
    methods: {
        ...mapActions([
            'increaseTrackingDay'
        ]),
        updateBuyAmount(stocks) {
            this.buyAmount = stocks.map(stock => stock.changedAmount)
                                   .reduce((sum, e) => sum + e, 0)
        },
        updateSellAmount(stocks) {
            this.sellAmount = stocks.map(stock => Math.abs(stock.changedAmount))
                                    .reduce((sum, e) => sum + e, 0)
        },
        findTotalPrice(stocks) {
            this.totalPrice = stocks.map(stock => stock.changedAmount * stock.averagePrice)
                                    .map(price => {
                                        if(price > 0) {
                                            return parseInt(price) * (1 + this.commissionRate * this.vatRate)
                                        } else {
                                            return parseInt(price) * (1 - this.commissionRate * this.vatRate)
                                        }
                                    })
                                    .reduce((sum, e) => sum + e, 0)
        },
        formatPrice(price) {
            if(!price)
                return '0'
            price = price.toFixed(2).toString()

            return price.replace(/(\d)(?=(\d{3})+\.)/g, '$1,')
        },
        formatNumber(number) {
            if(!number)
                return '0'

            return number.toString().replace(/(\d)(?=(\d{3})+)/g, '$1,')
        },
        openModal() {
            this.$refs.summaryModal.openModal()
        },
        nextDay() {
            userController.nextDay()
                .then(() => this.increaseTrackingDay())
                .then(() => this.$refs.loader.activateLoader(750))
        }
    }
  }

</script>
