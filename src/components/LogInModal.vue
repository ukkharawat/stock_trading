<template>
  <div id="log-in-modal">
    <modalHeader :message="message"></modalHeader>
    <logInModalContent></logInModalContent>
  </div>
</template>

<script>
  import modalHeader from '@/components/ModalHeader'
  import logInModalContent from '@/components/LogInModalContent'

  export default {
    data() {
      return {
        message: "Log In"
      }
    },
    components: {
      modalHeader,
      logInModalContent
    }
  }
</script>

<style>
  #log-in-modal {
    background-color: #fafafa;
    width: 50%;
    height: auto;
    border-radius: 8px;
  }
</style>
