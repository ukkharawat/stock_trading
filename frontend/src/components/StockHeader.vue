<template>
  <div id="stock-header">
    <h2 class="symbol">{{corpSymbol}}</h2>
    <h3 class="fullname">{{corpFullThaiName}}</h3>
  </div>
</template>

<script>

  export default {
    props: {
      corpSymbol: {
        type: String
      },
      corpFullThaiName: {
        type: String
      }
    }
  }
</script>

<style>
  #stock-header {
    margin-left: 16px;
    padding-top: 16px;
    text-align: left;
  }

  .symbol {
    font-size: 24px;
    display: inline;
    margin-right: 4px;
  }

  .fullname {
    font-size: 16px;
    display: inline;
  }
</style>
