<template>
  <div id="stock-header">
    <h2 class="symbol">{{symbol}}</h2>
    <h3 class="fullname">{{fullname}}</h3>
  </div>
</template>

<script>

  export default {
    props: {
      symbol: {
        type: String
      },
      fullname: {
        type: String
      }
    }
  }
</script>
