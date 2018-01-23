<template>
  <b-row id="portfolio-page">
    <b-col cols="2" v-show="getHoldingStock != 0">
      <index>
          <indexMenu
            :mainMenuTitle="title"
            :subMenuTitles="getStocksName">
          </indexMenu>
      </index>
    </b-col>
    <b-col cols="10">
      <stock v-for="stock in getHoldingStock" :key="stock.symbol" :stock="stock"></stock>
    </b-col>
  </b-row>
</template>

<script>
  import index from '@/components/Index'
  import stock from '@/components/Stock'
  import indexMenu from '@/components/IndexMenu'
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
      indexMenu
    },
    computed: {
      ...mapGetters([
        "getStock"
      ]),
      getHoldingStock() {
        return this.getStock.filter(stock => stock.amount != 0)
      },
      getStocksName() {
        return this.getHoldingStock.map(holdingStock => {
          return holdingStock.symbol
        })
      }
    }
  }
</script>
