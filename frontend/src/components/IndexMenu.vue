<template>
  <div id="index-menu">
    <a class="main-menu" @click="onClickIndustry">{{industry}}</a>
    <a class="sub-menu" v-for="(sector, index) in sectors"
        v-bind:key="sector"
        @click="onClickSector(index)">{{sector}}</a>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    props: {
      industry: {
        type: String
      },
      sectors: {
        type: Array
      }
    },
    methods: {
      onClickIndustry() {
        this.$emit("industryClick", this.industry)
      },
      onClickSector(index) {
        this.$emit("sectorClick", this.sectors[index])
      }
    }
  }
</script>

<style>
  #index-menu {
    padding-top: 8px;
    margin-left: 16px;
    text-align: left;
  }

  a.main-menu {
    color: #373737;
    font-size: 16px;
    cursor: pointer;
    display: block;
  }

  a.sub-menu {
    margin-left: 16px;
    color: #636363;
    font-size: 14px;
    cursor: pointer;
    display: block;
  }
</style>
