<template>
  <div id="stock" v-show="symbol != null">
      <stockHeader :symbol="symbol"
                   :fullname="fullname">
      </stockHeader>

      <b-row>
        <b-col cols="12">
          <amChart :symbol="symbol"></amChart>
        </b-col>
      </b-row>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  import stockDatasource from '@/datasources/Stock.datasource'
  import stockHeader from '@/components/StockHeader'
  import amChart from '@/components/AmChart'

  export default {
    props: {
      symbol: {
        type: String
      },
      fullname: {
        type: String
      }
    },
    components: {
      stockHeader,
      amChart
    }
  }
</script>