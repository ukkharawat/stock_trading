<template>
  <div id="action-button">
    <div class="form-group">
      <button type="submit" class="btn"
              @click="eventClick"
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
      eventClick() {
        this.$emit('onClick', this.message)
      }
    }
  }
</script>


<style>

  .btn {
    border-radius: 8px;
    width: 100%;
    font-size: 18px;
    background-color: #fafafa;
    margin-bottom: 8px;
  }

  .sell-button, .sell-button:hover {
    border: #ff0000 solid 1px;
    color: #ff0000;
  }

  .buy-button, .buy-button:hover {
    border: #0288d1 solid 1px;
    color: #0288d1;
  }

  .log-in-button, .log-in-button:hover {
    border: #ffd740 solid 1px;
    color: #212121;
    background-color: #ffd740;
  }
</style>
