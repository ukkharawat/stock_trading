<template>
  <div id="holding-info">
    <h5 class="holding">Holding</h5>
    <h6 class="holding-amount">{{ amount }}</h6>
  </div>
</template>

<script>

  export default {
    props: {
      amount: {
        type: Number
      }
    }
  }
</script>

<style>

  #holding-info {
    margin-bottom: 16px;
  }

  .holding {
    text-align: left;
    font-size: 18px;
  }

  .holding-amount {
    font-size: 14px;
  }
</style>
