<template>
  <div id="text-input">
    <baseInput :inputType="'text'"
               @valueChange="valueChange"
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
      valueChange(event) {
        this.$emit('valueChange', event)
      }
    }
  }
</script>
