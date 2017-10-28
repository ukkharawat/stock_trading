<template>
  <div id="main-page" class="row">
    <div class="col-sm-2">
      <index>
        <div v-for="menuItem in menuItems">
          <indexMenu
            :mainMenuTitle="menuItem.mainMenuTitle"
            :subMenuTitles="menuItem.subMenuTitles">
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
        menuItems: [
          {
            mainMenuTitle: "ARGO",
            subMenuTitles: ["ARGI", "FOOD"]
          },
          {
            mainMenuTitle: "CONSUMP",
            subMenuTitles: ["FASHION", "HOME", "PERSON"]
          },
          {
            mainMenuTitle: "FINCIAL",
            subMenuTitles: ["BANK", "FIN", "INSUR"]
          },
          {
            mainMenuTitle: "INDUS",
            subMenuTitles: ["AUTO", "IMM", "PAPER", "PETRO", "PKG", "STEEL"]
          },
          {
            mainMenuTitle: "PROPCON",
            subMenuTitles: ["CONMAT", "PROP", "PF&REIT", "CONS"]
          },
          {
            mainMenuTitle: "RESOURC",
            subMenuTitles: ["ENERG", "MINE"]
          },
          {
            mainMenuTitle: "SERVICE",
            subMenuTitles: ["COMM", "HELTH", "MEDIA", "PROF", "TOURISM", "TRANS"]
          },
          {
            mainMenuTitle: "TECH",
            subMenuTitles: ["ETRON", "ICT"]
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
