<template>
  <div id="index-menu">
    <a class="main-menu">{{title}}</a>
    <a class="sub-menu" v-for="stockName in stocksName" v-bind:key="stockName">{{stockName}}</a>
  </div>
</template>

<script>
  export default {
    props: {
      title: {
        type: String
      },
      stocksName: {
        type: Array
      }
    }
  }
</script>