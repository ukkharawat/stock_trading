<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
    <modal>
      <logInModal @click.stop></logInModal>
    </modal>
  </div>
</template>

<script>
  import modal from '@/components/Modal'
  import navbar from '@/components/Navbar'
  import logInModal from '@/components/LogInModal'

  export default {
    name: 'app',
    components: {
      modal,
      navbar,
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
