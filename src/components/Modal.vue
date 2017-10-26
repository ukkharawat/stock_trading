<template>
  <div id="modal">
    <modalBox></modalBox>
  </div>
</template>

<script>
  import modalBox from '@/components/ModalBox'

  export default {
    components: {
      modalBox
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
