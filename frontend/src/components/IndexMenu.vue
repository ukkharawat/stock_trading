<template>
  <div id="index-menu" @click="selectSymbol" v-if="isDisplay">
    <b-row class="stock-list-margin">
      <b-col cols="3" class="cursor-pointer">
        <h4>{{ stock.symbol }}</h4>
      </b-col>
      <b-col :cols="columnGrid" class="text-right disable-padding cursor-pointer">
        <h4 :class="{'green-price': isPriceUp, 'red-price': !isPriceUp}">
          {{ value.currentPrice }}
        </h4>
        <p class="disable-margin" :class="{'green-percent': isPriceUp, 'red-percent': !isPriceUp}">
          {{isPlusSign}}{{ value.diff }}( {{ value.diffPer }}% )
        </p>
      </b-col>
      <b-col cols="5" class="fix-padding" v-show="isLoggedIn">
          <div class="input-group" @click.stop>
            <span class="input-group-btn">
              <button class="btn decrease-btn" @click="decrease" type="button" :disabled="!isAmountEnough || !isLoggedIn">
                <i class="fas fa-minus" />
              </button>
            </span>
            <input type="number" class="form-control text-right amount-input" v-model="stock.amount" disabled @click.stop>
            <span class="input-group-btn" @click.stop>
              <button class="btn increase-btn" @click="increase" type="button" :disabled="!isLoggedIn">
                <i class="fas fa-plus" />
              </button>
            </span>
          </div>
      </b-col>
    </b-row>
    <hr class="disable-margin">
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import stockDatasource from '@/datasources/Stock.datasource'

  export default {
    props: {
      stock: {
        type: Object
      },
      value: {
        type: Object
      }
    },
    computed: {
      ...mapGetters([
        'isLoggedIn',
        'getTrackingDay'
      ]),
      isPriceUp() {
        return this.value.diff >= 0
      },
      isPlusSign() {
        return this.isPriceUp? '+': ''
      },
      isAmountEnough() {
        return this.stock.amount >= 100
      },
      isDisplay() {
        return this.value != null && this.value.diff != null
      },
      columnGrid() {
        return this.isLoggedIn? "4": "9"
      }
    },
    methods: {
      ...mapActions([
        'updateUnchangedStock'
      ]),
      increase() {
        this.stock.changedAmount += 100
        this.stock.amount += 100

        this.updateStock()
      },
      decrease() {
        this.stock.changedAmount -= 100
        this.stock.amount -= 100

        this.updateStock()
      },
      updateStock() {
        let stock = stockDatasource.createUpdatedStock(this.stock, this.value.currentPrice)

        this.updateUnchangedStock(stock)
      },
      selectSymbol() {
        this.$emit('selectSymbol', this.stock.symbol)
      }
    }
  }
</script>