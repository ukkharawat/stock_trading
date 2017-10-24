<template>
  <div id="stock">
      <stockHeader :corpShortName="'AH'"
        :corpFullThaiName="'บริษัท อาปิโก ไฮเทค จำกัด (มหาชน)'">
      </stockHeader>
      <h1>{{getCategory()}}</h1>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  import stockHeader from '@/components/StockHeader'

  export default {
    components: {
      stockHeader
    },
    methods: {
      ...mapGetters([
        'getCategory'
      ])
    }
  }
</script>

<style>
  #stock {
    width: 100%;
    height: 200px;
    margin-top: 24px;
    border-radius: 8px;
    border: #ffc900 solid 1px;
    box-shadow: 0 2px 1px 0 rgba(0, 0, 0, 0.1);
  }
</style>
