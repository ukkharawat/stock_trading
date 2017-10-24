<template>
  <div id="stock-header">
    <h2 class="shortname">{{corpShortName}}</h2>
    <h3 class="fullname">{{corpFullThaiName}}</h3>
  </div>
</template>

<script>

  export default {
    props: {
      corpShortName: {
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

  .shortname {
    font-size: 24px;
    display: inline;
  }

  .fullname {
    font-size: 16px;
    display: inline;
  }
</style>
