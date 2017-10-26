<template>
  <div id="text-input">
    <baseInput :inputType="'text'"
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
