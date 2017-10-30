<template>
  <div id="average-price-info">
    <infoBase :title="'Average Buy Price'"
              :amount="price"></infoBase>
  </div>
</template>

<script>

  import infoBase from '@/components/InfoBase'

  export default {
    props: {
      price: {
        type: Number
      }
    },
    components: {
      infoBase
    }
  }
</script>
