<template>
  <div id="app">
    <navbar></navbar>
    <div class="row">
      <div class="col-sm-2">
        <index></index>
      </div>
      <div class="col-sm-10">
        <stock></stock>
      </div>
    </div>
  </div>
</template>

<script>
  import navbar from '@/components/Navbar'
  import index from '@/components/Index'
  import stock from '@/components/Stock'

  export default {
    name: 'app',
    components: {
      navbar,
      index,
      stock
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  .row {
    margin-right: 0 !important;
  }
</style>
