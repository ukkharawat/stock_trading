<template>
  <div id="average-price-info">
    <baseInfo :title="'Average Buy Price'"
              :amount="price"></baseInfo>
  </div>
</template>

<script>

  import baseInfo from '@/components/BaseInfo'

  export default {
    props: {
      price: {
        type: Number
      }
    },
    components: {
      baseInfo
    }
  }
</script>
