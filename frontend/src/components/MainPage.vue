<template>
  <b-row id="main-page" >
    <b-col cols="4">
      <index>
        <div v-for="stock in stocks" v-bind:key="stock.symbol">
          <indexMenu
            :stock="stock"
            @sectorClick="sectorClick">
          </indexMenu>
        </div>
      </index>
    </b-col>
    <b-col cols="8"> 
      <stock v-for="stock in filteredStock" v-show="getStock !== null"
             :key="stock.symbol"
             :stock="stock"></stock>
    </b-col>
  </b-row>
</template>

<script>
  import index from '@/components/Index'
  import stock from '@/components/Stock'
  import indexMenu from '@/components/IndexMenu'
  import { mapGetters, mapActions } from 'vuex'

  export default {
    data() {
      return {
        stocks: [
          {
            'symbol': 'TEST',
            'price': 255,
            'diff': 0.74,
            'diffPer': 0.1,
            'amount': 50
          },
          {
            'symbol': 'TEST2',
            'price': 255,
            'diff': -0.74,
            'diffPer': 0.1,
            'amount': 50
          }
        ],
        sector: "AGRI"
      }
    },
    components: {
      index,
      stock,
      indexMenu
    },
    created() {
      this.setCurrentCategory("AGRI")
    },
    computed: {
      ...mapGetters([
        'getStock'
      ]),
      filteredStock() {
        if(this.getStock != null) {
          return this.getStock.filter(stock => stock.sector === this.sector || stock.industry == this.industry)
        }
      }
    },
    methods: {
      ...mapActions([
        'setCurrentCategory'
      ]),
      sectorClick(sector) {
        this.sector = sector
        this.industry = null
      },
      industryClick(industry) {
        this.industry = industry
        this.sector = null
      }
    }
  }
</script>
