<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
    <modal>
      <logInModal v-show="getIsLogInModal" @click.stop></logInModal>
      <confirmModal v-show="getIsConfirmModal" @click.stop></confirmModal>
    </modal>
  </div>
</template>

<script>
  import modal from '@/components/Modal'
  import navbar from '@/components/Navbar'
  import logInModal from '@/components/LogInModal'
  import confirmModal from '@/components/ConfirmModal'
  import { mapGetters } from 'vuex'

  export default {
    name: 'app',
    components: {
      modal,
      navbar,
      logInModal,
      confirmModal
    },
    computed: {
      ...mapGetters([
        'getIsLogInModal',
        'getIsConfirmModal'
      ])
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
