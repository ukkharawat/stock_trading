<template>
  <div id="stock" v-show="isDisplay">
      <stockHeader :corpSymbol="stock.symbol"
                   :corpFullThaiName="stock.fullName">
      </stockHeader>
      <b-row>
        <div :class="{'col-sm-10': isLoggedIn, 'col-sm-12': !isLoggedIn}">
          <amChart :stockName="stock.symbol"
                  @displayChange="displayHandle"
                  @dataChange="dataChange">
          </amChart>
        </div>
        <b-col cols="2" class="vertical-center" v-show="isLoggedIn">
          <holdingInfo :amount="formatAmount(stock.amount)"></holdingInfo>
        <averagePriceInfo :price="formatAveragePrice(stock.averagePrice)"></averagePriceInfo>
          <b-form-input type="number"
                        name="amount"
                        v-model="amount"
                        v-validate="'required|min_value:100'"
                        placeholder="Amount">
          </b-form-input>
          <span v-show="errors.has('amount')" 
                    class="help text-danger">{{ errors.first('amount') }}</span>
          <b-button variant="primary" class="margin-top" 
                    @click="buy" :disabled="amount === null || errors.any() || isBuyButtonDisable">BUY</b-button>
          <b-button variant="danger" @click="sell"
                    :disabled="amount === null || errors.any() || isSellButtonDisable">SELL</b-button>
        </b-col>
      </b-row>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import stockDatasource from '@/datasources/Stock.datasource'
  import stockHeader from '@/components/StockHeader'
  import amChart from '@/components/AmChart'
  import holdingInfo from '@/components/HoldingInfo'
  import averagePriceInfo from '@/components/AveragePriceInfo'

  export default {
    props: {
      stock: {
        type: Object
      }
    },
    data() {
      return {
        amount: null,
        isDisplay: true,
        averagePrice: null,
        commissionRate: 0.001578,
        vatRate: 1.07
      }
    },
    components: {
      stockHeader,
      amChart,
      holdingInfo,
      averagePriceInfo
    },
    computed: {
      ...mapGetters([
        'getCategory',
        'getCash',
        'isLoggedIn'
      ]),
      isSellButtonDisable() {
        return this.amount > this.stock.amount
      },
      isBuyButtonDisable() {
        return this.amount * this.averagePrice * this.commissionRate * this.vatRate
      }
    },
    methods: {
      ...mapActions([
        'openConfirmModal'
      ]),
      buy() {
        let nextActionInfo = stockDatasource.createStockObject('buy', this.stock.symbol, this.amount, this.averagePrice)
        
        if(this.amount * this.averagePrice < this.getCash) {
          this.openConfirmModal(nextActionInfo)
        }
      },
      sell() {
        let nextActionInfo = stockDatasource.createStockObject('sell', this.stock.symbol, this.amount, this.averagePrice)
        let currentAmount = this.stock.amount

        if(this.amount <= currentAmount) {
          this.openConfirmModal(nextActionInfo)
        }
      },
      dataChange(event) {
        this.averagePrice = event['BuyPrice']
      },
      displayHandle(event) {
        this.isDisplay = false
      },
      formatAveragePrice(price) {
        if(!price)
          return '0'
        price = price.toFixed(2).toString()

        return price.replace(/(\d)(?=(\d{3})+\.)/g, '$1,') + " ฿"
      },
      formatAmount(amount) {
        if(!amount)
          return '0'

        return String(amount).replace(/(\d)(?=(\d{3})+\.)/g, '$1,') + " shares"
      }
    }
  }
</script>