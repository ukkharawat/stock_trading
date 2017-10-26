<template>
  <div id="stock">
      <stockHeader :corpShortName="'AH'"
        :corpFullThaiName="'บริษัท อาปิโก ไฮเทค จำกัด (มหาชน)'">
      </stockHeader>
      <div class="row">
        <div class="col-sm-10">
          <amChart></amChart>
        </div>
        <div class="col-sm-2 vertical-center">
          <textInput :placeholder="'Amount'"></textInput>
          <actionButton :message="'buy'"
                      :buttonClass="'buy-button'">
          </actionButton>
          <actionButton :message="'sell'"
                      :buttonClass="'sell-button'">
          </actionButton>
        </div>
      </div>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  import stockHeader from '@/components/StockHeader'
  import amChart from '@/components/AmChart'
  import textInput from '@/components/TextInput'
  import actionButton from '@/components/ActionButton'

  export default {
    components: {
      stockHeader,
      amChart,
      textInput,
      actionButton
    },
    computed: {
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
    height: auto;
    margin-top: 24px;
    border-radius: 8px;
    border: #ffc900 solid 1px;
    box-shadow: 0 2px 1px 0 rgba(0, 0, 0, 0.1);
  }

  .vertical-center {
    display : flex;
    flex-direction: column;
    justify-content: center;
  }
</style>
