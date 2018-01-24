<template>
  <b-row id="portfolio-page" v-if="getStock !== null">
    <b-col cols="2" v-if="getHoldingStock !== null">
      <index>
          <portfolioIndex
            :title="title"
            :stocksName="getStocksName">
          </portfolioIndex>
      </index>
    </b-col>
    <b-col cols="10" :class="{'extend-buttom': isExtendButtom}">
      <stock v-for="stock in getHoldingStock" :key="stock.symbol" :stock="stock"></stock>
    </b-col>
  </b-row>
</template>

<script>
  import index from '@/components/Index'
  import stock from '@/components/Stock'
  import portfolioIndex from '@/components/PortfolioIndex'
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        title: "Holding Stock"
      }
    },
    components: {
      index,
      stock,
      portfolioIndex
    },
    computed: {
      ...mapGetters([
        "getStock"
      ]),
      getHoldingStock() {
        return this.getStock.filter(stock => stock.amount != 0)
      },
      getStocksName() {
        return this.getHoldingStock.map(stock => stock.symbol)
      },
      isExtendButtom() {
        return this.getHoldingStock.length == 1
      }
    }
  }
</script>
