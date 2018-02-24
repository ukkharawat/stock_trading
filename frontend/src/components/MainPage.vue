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
          <virtualList class="scroll" :size="40" :remain="8" :bench="32" :startIndex="startIndex">
            <div v-for="stock in filteredStockBySearch" v-bind:key="stock.symbol">
              <indexMenu
                :stock="stock"
                :value="values.find(e => e.symbol === stock.symbol)"
                @selectSymbol="selectSymbol">
              </indexMenu>
            </div>
          </virtualList>
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
  import virtualList from 'vue-virtual-scroll-list'
  import stockController from '@/controllers/Stock.controller'
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        symbol: "",
        selectedSymbol: null,
        values: [],
        startIndex: 0
      }
    },
    async created() {
      await stockController.getComparedValue()
                .then(response => {
                  this.values = response.comparedValues
                })
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
        'getTrackingDay'
      ]),
      filteredStockBySearch() {
        return this.getStock.filter(stock => stock.symbol.includes(this.symbol.toUpperCase()))
      }
    },
    watch: {
      getStock: {
        handler(stock) {
          this.selectedSymbol = stock[0].symbol
        }
      },
      getTrackingDay: {
        async handler() {
          await stockController.getComparedValue()
                .then(response => {
                  this.values = response.comparedValues
                })
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
