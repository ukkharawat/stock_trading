<template>
  <div id="stock-header">
    <content-placeholders v-show="!symbol">
      <content-placeholders-img style="height:30px"/>
    </content-placeholders>
    <h2 class="symbol" v-show="symbol">{{symbol}}</h2>
    <h3 class="fullname" v-show="fullname">{{fullname}}</h3>
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
