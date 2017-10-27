<template>
  <div id="password-input">
    <baseInput :inputType="'password'"
               @handleValueChange="handleValueChange"
               :placeholder="placeholder">
    </baseInput>
  </div>
</template>

<script>
  import baseInput from '@/components/BaseInput'

  export default {
    props: {
      placeholder: {
        type: String
      }
    },
    components: {
      baseInput
    },
    methods: {
      handleValueChange(event) {
        this.$emit('handleValueChange', event)
      }
    }
  }
</script>
