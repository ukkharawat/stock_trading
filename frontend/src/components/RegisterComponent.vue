<template>
  <div>
      <b-nav-item @click="openRegisterModal" v-show="!isLoggedIn">Register</b-nav-item>

      <registerModal ref="registerModal"></registerModal>
  </div>
</template>

<script>
  import registerModal from '@/components/RegisterModal'
  import { mapGetters } from 'vuex'

  export default {
      components: {
          registerModal
      },
      computed: {
          ...mapGetters([
              'isLoggedIn'
          ])
      },
      methods: {
          openRegisterModal() {
            this.$refs.registerModal.openModal()
          }
      }
  }

</script>
