<template>
  <div class="modal-header">
    <h4 class="modal-title">{{message}}</h4>
    <button class="close" @click="closeModal">x</button>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    props: {
      message: {
        type: String
      }
    },
    methods: {
      ...mapActions([
        'closeModal'
      ])
    }
  }
</script>

<style>
  .modal-header {
    background-color : #ffc400;
  }

  .close {
    cursor: pointer;
  }
</style>
