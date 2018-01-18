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
