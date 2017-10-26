<template>
  <div id="log-in-modal">
    <logInModalHeader></logInModalHeader>
    <logInModalContent></logInModalContent>
  </div>
</template>

<script>
  import logInModalHeader from '@/components/LogInModalHeader'
  import logInModalContent from '@/components/LogInModalContent'

  export default {
    components: {
      logInModalHeader,
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
