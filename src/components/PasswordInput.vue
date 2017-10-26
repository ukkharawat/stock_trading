<template>
  <div id="password-input">
    <baseInput :inputType="'password'"
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
    }
  }
</script>
