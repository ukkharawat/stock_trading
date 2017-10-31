<template>
  <div id="modal-header">
    <h1 class="modal-text-header">{{message}}</h1>
  </div>
</template>

<script>
  export default {
    props: {
      message: {
        type: String
      }
    }
  }
</script>

<style>
  #modal-header {
    width: 100%;
    height: 20%;
    background-color : #ffc400;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    display: flex;
    align-items: center;
  }

  .modal-text-header {
    text-align: left;
    font-size: 40px;
    margin: 8px 16px !important;
  }
</style>
