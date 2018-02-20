<template>
  <div class="footer" v-show="isUnchangedStock">
      <div class="row">
          <b-col cols="7" class="text-left">
              <p class="summary" v-show="buyAmount != 0">Buy {{buyAmount}} shares,</p>
              <p class="summary" v-show="sellAmount != 0">Sell {{sellAmount}} shares,</p>
              <p class="summary" v-show="totalAmount != 0">Total price {{totalPrice}} baht</p>
          </b-col>
          <b-col cols="5" class="text-right">
              <p class="summary complete-trading">complete trading</p>
          </b-col>
      </div>
  </div>
</template>
<script>
  import { mapGetters } from 'vuex'

  export default {
    data() {
        return {
            buyAmount: null,
            sellAmount: null,
            totalPrice: null,
            vatRate: 1.07,
            commissionRate: 0.00157
        }
    },
    computed: {
        ...mapGetters([
            'getUnchangedStocks'
        ]),
        isUnchangedStock() {
            return this.getUnchangedStocks.length != 0
        }
    },
    watch: {
        getUnchangedStocks: {
            handler(val) {
                this.updateBuyAmount(val.filter(stock => stock.newAmount > stock.oldAmount))
                this.updateSellAmount(val.filter(stock => stock.newAmount < stock.oldAmount))
                this.findTotalPrice(val)
            }
        },
        deep: true
    },
    methods: {
        updateBuyAmount(stocks) {
            this.buyAmount = stocks.map(stock => stock.newAmount - stock.oldAmount)
                                   .reduce((sum, e) => sum + e, 0)
        },
        updateSellAmount(stocks) {
            this.sellAmount = stocks.map(stock => stock.oldAmount - stock.newAmount)
                                    .reduce((sum, e) => sum + e, 0)
        },
        findTotalPrice(stocks) {
            this.totalPrice = stocks.map(stock => (stock.newAmount - stock.oldAmount) * stock.price)
                                    .map(price => parseInt(price) * (1 + this.commissionRate * this.vatRate))
                                    .reduce((sum, e) => sum + e, 0)

            this.totalPrice = this.formatPrice(this.totalPrice)
        },
        formatPrice(price) {
            if(!price)
                return '0'
            price = price.toFixed(2).toString()

            return price.replace(/(\d)(?=(\d{3})+\.)/g, '$1,') + " ฿"
        }
    }
  }

</script>
