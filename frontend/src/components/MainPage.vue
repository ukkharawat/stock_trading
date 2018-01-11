<template>
  <div id="main-page" class="row" v-show="getStock !== null">
    <div class="col-sm-2">
      <index>
        <div v-for="menuItem in menuItems" v-bind:key="menuItem.industry">
          <indexMenu
            :industry="menuItem.industry"
            :sectors="menuItem.sectors"
            @industryClick="industryClick"
            @sectorClick="sectorClick">
          </indexMenu>
        </div>
      </index>
    </div>
    <div class="col-sm-10">
      <stock v-for="stock in filteredStock"
             :key="stock.shortName"
             :stock="stock"></stock>
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
        menuItems: [
          {
            industry: "AGRO",
            sectors: ["AGRI", "FOOD"]
          },
          {
            industry: "CONSUMP",
            sectors: ["FASHION", "HOME", "PERSON"]
          },
          {
            industry: "FINCIAL",
            sectors: ["BANK", "FIN", "INSUR"]
          },
          {
            industry: "INDUS",
            sectors: ["AUTO", "IMM", "PAPER", "PETRO", "PKG", "STEEL"]
          },
          {
            industry: "PROPCON",
            sectors: ["CONMAT", "PROP", "PF&REITs", "CONS"]
          },
          {
            industry: "RESOURC",
            sectors: ["ENERG", "MINE"]
          },
          {
            industry: "SERVICE",
            sectors: ["COMM", "HELTH", "MEDIA", "PROF", "TOURISM", "TRANS"]
          },
          {
            industry: "TECH",
            sectors: ["ETRON", "ICT"]
          }
        ],
        sector: "AGRI",
        industry: null
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
      filteredStock() {
        if(this.getStock != null) {
          return this.getStock.filter(stock => stock.sector === this.sector || stock.industry == this.industry)
        }
      }
    },
    methods: {
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
