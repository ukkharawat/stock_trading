<template>
  <div class="base-modal" @click.stop>
    <modalHeader :message="message"></modalHeader>
    <registerModalContent></registerModalContent>
  </div>
</template>

<script>
  import modalHeader from '@/components/ModalHeader'
  import registerModalContent from '@/components/RegisterModalContent'

  export default {
    data() {
      return {
        message: "Register"
      }
    },
    components: {
      modalHeader,
      registerModalContent
    }
  }
</script>