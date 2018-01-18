<template>
  <div id="modal" @click="closeModal" v-show="getIsModalOpen">
    <slot></slot>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    computed: {
      ...mapGetters([
        'getIsModalOpen'
      ])
    },
    methods: {
    ...mapActions([
        'closeModal'
      ])
    }
  }
</script>