<template>
  <div id="stock">
      <stockHeader :corpShortName="stock.shortName"
                   :corpFullThaiName="stock.fullName">
      </stockHeader>
      <div class="row">
        <div class="col-sm-10">
          <amChart :stockName="stock.shortName"
                   @dataChange="dataChange">
          </amChart>
        </div>
        <div class="col-sm-2 vertical-center">
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
        </div>
      </div>
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
        currentPrice: null
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
        'getCash'
      ])
    },
    methods: {
      ...mapActions([
        "openConfirmModal"
      ]),
      onClick(event) {
        let nextActionInfo = stockDatasource.createStockObject(event, this.stock.shortName, this.stock.fullName, this.amount, this.currentPrice)

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
        this.currentPrice = event["Close"]
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
    border: #ffc900 solid 1px;
    box-shadow: 0 2px 1px 0 rgba(0, 0, 0, 0.1);
  }

  .vertical-center {
    display : flex;
    flex-direction: column;
    justify-content: center;
  }
</style>
