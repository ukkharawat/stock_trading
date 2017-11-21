<template>
  <div id="app">
    <navbar></navbar>
    <router-view/>
    <modal>
      <logInModal v-show="getIsLogInModal"></logInModal>
      <confirmModal v-show="getIsConfirmModal"></confirmModal>
    </modal>
    <nextDayButton></nextDayButton>
  </div>
</template>

<script>
  import modal from '@/components/Modal'
  import navbar from '@/components/Navbar'
  import logInModal from '@/components/LogInModal'
  import confirmModal from '@/components/ConfirmModal'
  import { mapGetters, mapActions } from 'vuex'
  import userController from '@/controllers/User.controller'
  import nextDayButton from '@/components/NextDayButton'

  export default {
    name: 'app',
    components: {
      modal,
      navbar,
      logInModal,
      confirmModal,
      nextDayButton
    },
    created() {
      this.setUsername(userController.getUsername())
    },
    computed: {
      ...mapGetters([
        'getIsLogInModal',
        'getIsConfirmModal'
      ])
    },
    methods: {
      ...mapActions([
        'setUsername'
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
