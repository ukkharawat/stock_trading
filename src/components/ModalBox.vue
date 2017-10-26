<template>
  <div id="modal-box">
    <modalBoxHeader></modalBoxHeader>
    <modalBoxContent></modalBoxContent>
  </div>
</template>

<script>
  import modalBoxHeader from '@/components/ModalBoxHeader'
  import modalBoxContent from '@/components/ModalBoxContent'

  export default {
    components: {
      modalBoxHeader,
      modalBoxContent
    }
  }
</script>

<style>
  #modal-box {
    background-color: #fafafa;
    width: 50%;
    height: auto;
    border-radius: 8px;
  }
</style>
