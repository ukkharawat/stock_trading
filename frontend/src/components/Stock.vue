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
        <averagePriceInfo :price="formatAverageBuyPrice(stock.averageBuyPrice)"></averagePriceInfo>
          <b-form-input type="text"
                        v-model="amount"
                        required
                        placeholder="Amount">
          </b-form-input>
          <b-button variant="primary" class="margin-top" @click="buy">BUY</b-button>
          <b-button variant="danger" @click="sell">SELL</b-button>
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
        currentPrice: null,
        isDisplay: true,
        buyPrice: null
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
      ])
    },
    methods: {
      ...mapActions([
        'openConfirmModal'
      ]),
      buy() {
        let nextActionInfo = stockDatasource.createStockObject('buy', this.stock.symbol, this.stock.fullName, this.amount, this.buyPrice)
        
        if(this.amount * this.buyPrice < this.getCash) {
          this.openConfirmModal(nextActionInfo)
        }
      },
      sell() {
        let nextActionInfo = stockDatasource.createStockObject('sell', this.stock.symbol, this.stock.fullName, this.amount, this.buyPrice)
        let currentAmount = this.stock.amount

        if(this.amount <= currentAmount) {
          this.openConfirmModal(nextActionInfo)
        }
      },
      dataChange(event) {
        this.buyPrice = event['BuyPrice']
      },
      displayHandle(event) {
        this.isDisplay = false
      },
      formatAverageBuyPrice(price) {
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