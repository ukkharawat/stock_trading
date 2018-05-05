<template>
  <div id="navbar-right">
    <b-nav>
        <b-nav-item v-show="isLoggedIn">
          Capital: {{capital?capital:getCash | currency}} 
        </b-nav-item>
        <b-nav-item v-show="isLoggedIn">
          Cash: {{getCash | currency}}
        </b-nav-item>
        
        <logInComponent></logInComponent>
        <signUpComponent></signUpComponent>

        <b-nav-item-dropdown v-bind:text="getUsername" right v-show="isLoggedIn">
          <a href="/portfolio" class="dropdown-item"> Portfolio </a>
          <b-dropdown-item @click="logout">Log out</b-dropdown-item>
        </b-nav-item-dropdown>
    </b-nav>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import userController from '@/controllers/User.controller'
  import cacheController from '@/controllers/Cache.controller'
  import logInComponent from '@/components/LogInComponent'
  import signUpComponent from '@/components/SignUpComponent'

  export default {
    props: {
      menuObjects : {
        type: Array
      }
    },
    components: {
      logInComponent,
      signUpComponent
    },
    data() {
      return {
        capital: 1000000
      }
    },
    computed: {
      ...mapGetters([
        'getCash',
        'getUsername',
        'isLoggedIn',
        'getStock'
      ])
    },
    watch: {
      getStock: {
        handler(val) {
          this.capital = this.getCash
          let holdingStock = this.getStock.filter(stock => stock.amount > 0)
          
          if(holdingStock.length > 0) {
            this.capital += holdingStock.map(stock => (stock.amount - stock.changedAmount) * stock.averagePrice)
                              .reduce((sum, current) => sum + current)
          }
          
        },
        deep: true
      }
    },
    methods: {
      ...mapActions([
        'setUsername',
        'setCash'
      ]),
      logout() {
        userController.logout()
          .then(response => {
            if(response.success) {
              cacheController.clearUserCache()
              this.clearVuex()
            }
          })
      },
      clearVuex() {
        this.setUsername(null)
        this.setCash(null)
      }
    },
    filters: {
      currency(value) {
        if (!value) return ''
        value = parseFloat(value).toFixed(2).toString()
        return value.replace(/(\d)(?=(\d{3})+\.)/g, '$1,') + " ฿"
      }
    }
  }
</script>