<template>
  <div id="stock">
    {{getHoldingStock}}
      <stockHeader :corpShortName="stock.shortName"
        :corpFullThaiName="stock.fullName">
      </stockHeader>
      <div class="row">
        <div class="col-sm-10">
          <amChart :stockName="stock.shortName"
            @dateChange="dateChange">
          </amChart>
        </div>
        <div class="col-sm-2 vertical-center">
          <holdingInfo :amount="stock.amount"></holdingInfo>
          <textInput :placeholder="'Amount'"
                      @handleValueChange="amountChange">
          </textInput>
          <actionButton :message="'buy'" @onClick="onClick"
                      :buttonClass="'buy-button'">
          </actionButton>
          <actionButton :message="'sell'" @onClick="onClick"
                      :buttonClass="'sell-button'">
          </actionButton>
        </div>
      </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import stockHeader from '@/components/StockHeader'
  import amChart from '@/components/AmChart'
  import holdingInfo from '@/components/HoldingInfo'
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
        date: null
      }
    },
    components: {
      stockHeader,
      amChart,
      textInput,
      actionButton,
      holdingInfo
    },
    computed: {
      ...mapGetters([
        'getCategory',
        'getHoldingStock'
      ])
    },
    methods: {
      ...mapActions([
        "buyStock",
        "sellStock"
      ]),
      onClick(event) {
        if(event === "buy") {
          this.buy(this.stock.shortName, this.stock.fullName, this.amount)
        } else {
          if(this.amount < this.getHoldingStock.find(holdingStock => {
            return holdingStock.name === this.stock.shortName
            }).amount) {
            this.sell(this.stock.shortName, this.stock.fullName, this.amount)
          }
        }
      },
      buy(name, fullname, amount) {
        let stock = {
          "shortName": name,
          "fullName": fullname,
          "amount": Number(amount)
        }

        this.buyStock(stock)
      },
      sell(name, fullname, amount) {
        let stock = {
          "shortName": name,
          "fullName": fullname,
          "amount": Number(amount)
        }

        this.sellStock(stock)
      },
      amountChange(event) {
        this.amount = event
      },
      dateChange(event) {
        this.date = event
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
