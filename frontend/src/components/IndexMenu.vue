<template>
  <div id="index-menu">
    <a class="main-menu" @click="onClickIndustry"
        :class="{'bold-text': getCurrentCategory === industry}">{{industry}}</a>
    <a class="sub-menu" v-for="(sector, index) in sectors"
        v-bind:key="sector"
        :class="{'bold-text': getCurrentCategory === sector}"
        @click="onClickSector(index)">{{sector}}</a>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    props: {
      industry: {
        type: String
      },
      sectors: {
        type: Array
      }
    },
    computed: {
      ...mapGetters([
        'getCurrentCategory'
      ])
    },
    methods: {
      ...mapActions([
        'setCurrentCategory'
      ]),
      onClickIndustry() {
        this.setCurrentCategory(this.industry)
        this.$emit("industryClick", this.industry)
      },
      onClickSector(index) {
        this.setCurrentCategory(this.sectors[index])
        this.$emit("sectorClick", this.sectors[index])
      }
    }
  }
</script>