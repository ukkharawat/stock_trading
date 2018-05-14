<template>
  <div class="modal" :style="{'display': isLoadingModalOpen}">
    <div class="loader"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoadingModalOpen: 'none'
    }
  },
  methods: {
    async  activateLoader() {
      this.isLoadingModalOpen = 'block'
      await this.sleep()
      this.isLoadingModalOpen = 'none'
    },
    sleep() {
      return new Promise(resolve => setTimeout(resolve, 750))
    }
  }
}
</script>
