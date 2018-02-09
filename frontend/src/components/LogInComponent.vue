<template>
  <div>
      <b-nav-item @click="openLogInModal" v-show="!isLoggedIn">Log in</b-nav-item>

      <logInModal ref="logInModal"></logInModal>
  </div>
</template>

<script>
  import logInModal from '@/components/LogInModal'
  import { mapGetters } from 'vuex'

  export default {
      components: {
          logInModal
      },
      computed: {
          ...mapGetters([
              'isLoggedIn'
          ])
      },
      methods: {
          openLogInModal() {
            this.$refs.logInModal.openModal()
          }
      }
  }

</script>
