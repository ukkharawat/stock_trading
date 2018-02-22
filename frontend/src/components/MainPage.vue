<template>
  <b-row id="main-page" v-if="getStock != null">
    <b-col cols="4">
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
          <h4 v-if="!filteredStockBySearch.length" class="warning">No symbol found.</h4>
          <div v-for="stock in filteredStockBySearch" v-bind:key="stock.symbol">
            <indexMenu
              :stock="stock"
              @selectSymbol="selectSymbol">
            </indexMenu>
          </div>
        </div>
      </index>
    </b-col>
    <b-col cols="8"> 
      <stock v-show="selectedSymbol !== null"
             :symbol="selectedSymbol">
      </stock>
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
        symbol: "",
        selectedSymbol: null
      }
    },
    components: {
      index,
      stock,
      indexMenu
    },
    computed: {
      ...mapGetters([
        'getStock'
      ]),
      filteredStockBySearch() {
        return this.getStock.slice(0,1)
        //.filter(stock => stock.symbol.includes(this.symbol.toUpperCase()))
      }
    },
    watch: {
      getStock: {
        handler(stock) {
          this.selectedSymbol = stock[0].symbol
        }
      }
    },
    methods: {
      selectSymbol(symbol) {
        this.selectedSymbol = symbol
      }
    }
  }
</script>
