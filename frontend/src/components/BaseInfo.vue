<template>
  <div id="info-base">
    <h5 class="info">{{ title }}</h5>
    <h6 class="info-amount">{{ amount }}</h6>
  </div>
</template>

<script>

  export default {
    props: {
      amount: {
        type: String
      },
      title: {
        type: String
      }
    }
  }
</script>

<style>

  #info-base {
    margin-bottom: 16px;
  }

  .info {
    text-align: left;
    font-size: 18px;
  }

  .info-amount {
    font-size: 14px;
  }
</style>
