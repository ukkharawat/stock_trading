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
          <b-button variant="primary" class="margin-top" @onClick="buy">BUY</b-button>
          <b-button variant="danger" @onClick="sell">SELL</b-button>
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
        isDisplay: true
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
        'getHoldingStock',
        'getCash',
        'isLoggedIn'
      ])
    },
    methods: {
      ...mapActions([
        'openConfirmModal',
        'updatePrice'
      ]),
      buy() {
        let nextActionInfo = stockDatasource.createStockObject('buy', this.stock.symbol, this.stock.fullName, this.amount, this.currentPrice)

        if(this.amount * this.currentPrice < this.getCash) {

          this.openConfirmModal(nextActionInfo)
        }
      },
      sell() {
        let nextActionInfo = stockDatasource.createStockObject('sell', this.stock.symbol, this.stock.fullName, this.amount, this.currentPrice)
        let currentAmount = this.stock.amount

        if(this.amount <= currentAmount) {
          this.openConfirmModal(nextActionInfo)
        }
      },
      dataChange(event) {
        let stock = {
          'symbol': this.stock.symbol,
          'price': event['BuyPrice']
        }
        
        this.updatePrice(stock)
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

<style>
  #stock {
    width: 100%;
    height: auto;
    margin-top: 24px;
    border-radius: 8px;
    background-color: rgba(255, 255, 255, 0.8);
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2);
  }

  .vertical-center {
    display : flex;
    flex-direction: column;
    justify-content: center;
  }
</style>
