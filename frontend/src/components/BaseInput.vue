<template>
  <div id="base-input">
    <div class="form-group">
        <input class="form-control" name="textInput"
               v-model="value" @change="handleValueChange"
               :type="inputType" :placeholder="placeholder">
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        value: null
      }
    },
    props: {
      placeholder: {
        type: String
      },
      inputType: {
        type: String
      }
    },
    methods: {
      handleValueChange() {
        this.$emit('handleValueChange', this.value)
      }
    }
  }
</script>

<style>

  #base-input {
    margin-bottom: 16px;
  }

  .form-control {
    border-radius: 8px;
    font-size: 18px;
    text-align:center;
  }
</style>
