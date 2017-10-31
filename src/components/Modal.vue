<template>
  <div id="modal" @click="closeModal" v-show="getIsLogInModal || getIsConfirmModal">
    <slot></slot>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    computed: {
      ...mapGetters([
        'getIsLogInModal',
        'getIsConfirmModal'
      ])
    },
    methods: {
    ...mapActions([
        'closeModal'
      ])
    }
  }
</script>

<style>
  #modal {
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.7);
    position: fixed;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1;
    left: 0;
    top: 0;
  }
</style>
