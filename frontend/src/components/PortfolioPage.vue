<template>
  <b-row id="porfolio-page" v-if="getStock != null">
    <b-col cols="4" class="remove-right-padding">
      <index>
        <div class="margin-top">
          <b-form-input id="searchInput"
                        type="text"
                        name="symbol"
                        v-model="symbol"
                        placeholder="Type symbol">
          </b-form-input>
        </div>
        <div class="scrollable">
          <content-placeholders v-for="i in 10" :key="i" v-if="!filteredStockBySearch.length && !symbol" :rounded="true">
            <content-placeholders-img style="height:60px"/>
            <hr>
          </content-placeholders>
          <h4 v-if="!filteredStockBySearch.length && symbol" class="warning">No matching symbol for "{{symbol}}"</h4>
          <virtualList class="scroll" :size="40" :remain="8" :bench="32" :startIndex="startIndex">
            <div v-for="stock in filteredStockBySearch" v-bind:key="stock.symbol">
              <indexMenu
                :stock="stock"
                :value="values.find(e => e.symbol === stock.symbol)"
                @selectedStock="selectedStock">
              </indexMenu>
            </div>
          </virtualList>
        </div>
      </index>
    </b-col>
    <b-col cols="8" class="remove-left-padding">
      <stock :symbol="selectedSymbol"
             :fullname="selectedFullname">
      </stock>
    </b-col>
  </b-row>
</template>

<script>
  import index from '@/components/Index'
  import stock from '@/components/Stock'
  import indexMenu from '@/components/IndexMenu'
  import virtualList from 'vue-virtual-scroll-list'
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        symbol: "",
        selectedSymbol: null,
        selectedFullname: null,
        values: [],
        startIndex: 0,
        portfolio: []
      }
    },
    components: {
      index,
      stock,
      indexMenu,
      virtualList
    },
    computed: {
      ...mapGetters([
        'getStock',
        'getUnchangedStocks'
      ]),
      filteredStockBySearch() {
        return this.portfolio.filter(stock => stock.symbol.includes(this.symbol.toUpperCase()))
      }
    },
    watch: {
      getStock: {
        handler(stocks) {
          this.portfolio = stocks.filter(stock => stock.amount > 0)
          this.getUnchangedStocks.forEach(unchangedStock => {
            if(unchangedStock.amount === 0)
              this.portfolio.push(stocks.find(stock => stock.symbol === unchangedStock.symbol))
          })
          
          this.updateValues()
          if(this.portfolio.length != 0)
            this.selectedStock(this.portfolio[0])
        },
        deep: true
      }
    },
    methods: {
      selectedStock(stock) {
        this.selectedSymbol = stock.symbol
        this.selectedFullname = stock.fullname
      },
      updateValues() {
        this.values = this.portfolio.map(stock => {
            return {
              symbol: stock.symbol,
              diff: stock.diff,
              diffPer: stock.diffPer,
              currentPrice: stock.averagePrice
            }
          })
      }
    }
  }
</script>
