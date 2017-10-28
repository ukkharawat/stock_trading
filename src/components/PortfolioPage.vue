<template>
  <div id="portfolio-page" class="row">
    <div class="col-sm-2">
      <index>
        <div v-for="holdingStock in holdingStocks">
          <indexMenu
            :mainMenuTitle="holdingStock.title"
            :subMenuTitles="holdingStock.stocksName">
          </indexMenu>
        </div>
      </index>
    </div>
    <div class="col-sm-10">
      <stock></stock>
    </div>
  </div>
</template>

<script>
  import index from '@/components/Index'
  import stock from '@/components/Stock'
  import indexMenu from '@/components/IndexMenu'

  export default {
    data() {
      return {
        holdingStocks: [
          {
            title: "Holding Stock",
            stocksName: ["AH"]
          }
        ]
      }
    },
    components: {
      index,
      stock,
      indexMenu
    }
  }
</script>
