<template>
  <div>
      <b-nav-item @click="openSignUpModal" v-show="!isLoggedIn">Sign up</b-nav-item>

      <signUpModal ref="signUpModal"></signUpModal>
  </div>
</template>

<script>
  import signUpModal from '@/components/SignUpModal'
  import { mapGetters } from 'vuex'

  export default {
      components: {
          signUpModal
      },
      computed: {
          ...mapGetters([
              'isLoggedIn'
          ])
      },
      methods: {
          openSignUpModal() {
            this.$refs.signUpModal.openModal()
          }
      }
  }

</script>
