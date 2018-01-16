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
          <textInput :placeholder="'Amount'"
                    @handleValueChange="amountChange">
          </textInput>
          <actionButton :message="'buy'" 
                        @onClick="onClick"
                        :buttonClass="'buy-button'">
          </actionButton>
          <actionButton :message="'sell'"
                        @onClick="onClick"
                        :buttonClass="'sell-button'">
          </actionButton>
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
  import textInput from '@/components/TextInput'
  import actionButton from '@/components/ActionButton'

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
      textInput,
      actionButton,
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
      onClick(event) {
        let nextActionInfo = stockDatasource.createStockObject(event, this.stock.symbol, this.stock.fullName, this.amount, this.currentPrice)

        if(event === "buy" && this.amount) {
          if(this.amount * this.currentPrice < this.getCash) {

            this.openConfirmModal(nextActionInfo)
          }
        } else if((event === "sell" && this.amount)) {
          let currentAmount = this.stock.amount

          if(this.amount <= currentAmount) {
            this.openConfirmModal(nextActionInfo)
          }
        }
      },
      amountChange(event) {
        this.amount = event
      },
      dataChange(event) {
        this.currentPrice = (Number(event["Close"]) + Number(event["Open"]))/2
        
        let stock = {
          'symbol': this.stock.symbol,
          'price': this.currentPrice
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
