<template>
  <div id="action-button">
    <div class="form-group">
      <button class="btn" @click.stop.prevent="handleClick"
              :class="buttonClass">{{message}}</button>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      message: {
        type: String,
        required: true
      },
      buttonClass: {
        type: String,
        required: true
      }
    },
    methods: {
      handleClick() {
        this.$emit("onClickEvent", this.message)
      }
    }
  }
</script>


<style>
  .form-group {
    margin-bottom: 0;
  }

  .btn {
    border-radius: 8px;
    width: 100%;
    font-size: 18px;
    background-color: #fdfdfd;
    margin-bottom: 16px;
  }

  .no-button, .no-button:hover {
    border: #ff0000 solid 1px;
    color: #ff0000;
  }

  .yes-button, .yes-button:hover {
    border: #0288d1 solid 1px;
    color: #0288d1;
  }
</style>
