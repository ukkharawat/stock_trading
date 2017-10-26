<template>
  <div id="base-input">
    <div class="form-group">
        <input class="form-control" name="textInput"
               :type="inputType" :placeholder="placeholder">
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      placeholder: {
        type: String
      },
      inputType: {
        type: String
      }
    }
  }
</script>

<style>

  #base-input {
    margin-bottom: 8px;
  }

  .form-control {
    border-radius: 8px;
    font-size: 18px;
    text-align:center;
  }
</style>
