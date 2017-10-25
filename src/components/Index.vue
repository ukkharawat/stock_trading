<template>
  <div id="index">
    <div v-for="menuItem in menuItems">
      <indexMenu
        :mainMenuTitle="menuItem.mainMenuTitle"
        :subMenuTitles="menuItem.subMenuTitles">
      </indexMenu>
    </div>
  </div>
</template>

<script>
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
      indexMenu: indexMenu
    },
    methods: {
    }
  }
</script>

<style>
  #index {
    margin-left: 24px;
    margin-top: 24px;
    padding-bottom: 8px;
    background-color: #fff59d;
    width: calc(100% - 16px);
    height: auto;
  }
</style>
