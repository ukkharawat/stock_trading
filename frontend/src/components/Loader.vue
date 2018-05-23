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
    async  activateLoader(ms) {
      this.isLoadingModalOpen = 'block'
      await this.sleep(ms)
      this.isLoadingModalOpen = 'none'
    },
    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms))
    }
  }
}
</script>
