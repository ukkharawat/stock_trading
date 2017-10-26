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
    <modal>
      <logInModal @click.stop></logInModal>
    </modal>
  </div>
</template>

<script>
  import modal from '@/components/Modal'
  import navbar from '@/components/Navbar'
  import index from '@/components/Index'
  import stock from '@/components/Stock'
  import logInModal from '@/components/LogInModal'

  export default {
    name: 'app',
    components: {
      modal,
      navbar,
      index,
      stock,
      logInModal
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
