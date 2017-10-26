<template>
  <div id="text-input">
    <div class="form-group">
      <input class="form-control" name="textInput"
             type="text" :placeholder="placeholder">
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      placeholder: {
        type: String
      }
    }
  }
</script>

<style>

  #text-input {
    margin-bottom: 8px;
  }

  .form-control {
    border-radius: 8px;
    font-size: 18px;
    text-align:center;
  }
</style>
