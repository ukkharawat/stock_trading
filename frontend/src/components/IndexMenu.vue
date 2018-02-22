<template>
  <div id="index-menu" @click="selectSymbol">
    <b-row class="stock-list-margin">
      <b-col cols="3" class="cursor-pointer">
        <h4>{{ stock.symbol }}</h4>
      </b-col>
      <b-col cols="4" class="text-right disable-padding cursor-pointer">
        <h4 :class="{'green-price': isPriceUp, 'red-price': !isPriceUp}">
          {{ price }}
        </h4>
        <p class="disable-margin" :class="{'green-percent': isPriceUp, 'red-percent': !isPriceUp}">
          {{isPlusSign}}{{ diff }}( {{ diffPer }}% )
        </p>
      </b-col>
      <b-col cols="5" class="fix-padding">
          <div class="input-group" @click.stop>
            <span class="input-group-btn">
              <button class="btn decrease-btn" @click="decrease" type="button" :disabled="!isAmountEnough">
                <i class="fas fa-minus" />
              </button>
            </span>
            <input type="number" class="form-control text-right amount-input" v-model="stock.amount" disabled @click.stop>
            <span class="input-group-btn" @click.stop>
              <button class="btn increase-btn" @click="increase" type="button"><i class="fas fa-plus" /></button>
            </span>
          </div>
      </b-col>
    </b-row>
    <hr class="disable-margin">
  </div>
</template>

<script>
  import { mapActions } from 'vuex'
  import stockDatasource from '@/datasources/Stock.datasource'
  import stockController from '@/controllers/Stock.controller'

  export default {
    props: {
      stock: {
        type: Object
      }
    },
    created() {
      stockController.getComparedValue(this.stock.symbol)
        .then(response => {
          this.diff = response.diff
          this.diffPer = response.diffPer
          this.price = response.currentPrice
        })
    },
    data() {
      return {
        diff: null,
        diffPer: null,
        price: null,
        changed: 0
      }
    },
    computed: {
      isPriceUp() {
        return this.diff > 0
      },
      isPlusSign() {
        return this.isPriceUp? '+': ''
      },
      isAmountEnough() {
        return this.stock.amount >= 100
      }
    },
    methods: {
      ...mapActions([
        'updateUnchangedStock'
      ]),
      increase() {
        this.changed += 100
        this.stock.amount += 100

        this.updateStock()
      },
      decrease() {
        this.changed -= 100
        this.stock.amount -= 100

        this.updateStock()
      },
      updateStock() {
        let stock = stockDatasource.createUpdatedStock(this.stock, this.changed, this.price)

        this.updateUnchangedStock(stock)
      },
      selectSymbol() {
        this.$emit('selectSymbol', this.stock.symbol)
      }
    }
  }
</script>