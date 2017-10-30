<template>
  <div id="portfolio-page" class="row">
    <div class="col-sm-2" v-show="getHoldingStock != 0">
      <index>
          <indexMenu
            :mainMenuTitle="title"
            :subMenuTitles="getStocksName">
          </indexMenu>
      </index>
    </div>
    <div class="col-sm-10">
      <stock v-for="stock in getHoldingStock" :key="stock.shortName" :stock="stock"></stock>
    </div>
  </div>
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
        "getHoldingStock"
      ]),
      getStocksName() {
        return this.getHoldingStock.map(holdingStock => {
          return holdingStock.shortName
        })
      }
    }
  }
</script>
