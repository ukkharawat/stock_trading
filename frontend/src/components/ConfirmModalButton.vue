<template>
  <div id="action-button">
    <div class="form-group">
      <button class="btn"
              @click.stop.prevent="handleClick"
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