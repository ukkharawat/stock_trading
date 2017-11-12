<template>
  <div id="index-menu">
    <a class="main-menu" @click="setCategory(mainMenuTitle)">{{mainMenuTitle}}</a>
    <a class="sub-menu" v-for="subMenuTitle in subMenuTitles"
       @click="setCategory(subMenuTitle)">{{subMenuTitle}}</a>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    props: {
      mainMenuTitle: {
        type: String
      },
      subMenuTitles: {
        type: Array
      }
    },
    methods: {
      ...mapActions([
        'setCategory'
      ])
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
