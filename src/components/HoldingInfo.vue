<template>
  <div id="holding-info">
    <baseInfo :title="'Holding'"
              :amount="amount"></baseInfo>
  </div>
</template>

<script>

  import baseInfo from '@/components/BaseInfo'

  export default {
    props: {
      amount: {
        type: Number
      }
    },
    components: {
      baseInfo
    }
  }
</script>
