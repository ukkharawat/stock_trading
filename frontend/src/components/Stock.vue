<template>
  <div id="stock">
    <stockHeader :symbol="symbol"
                  :fullname="fullname">
    </stockHeader>
    <b-row v-if="symbol != null">
      <b-col cols="12">
        <amChart :symbol="symbol"></amChart>
      </b-col>
    </b-row>
  </div>
</template>

<script>
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