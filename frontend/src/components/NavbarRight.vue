<template>
  <div id="navbar-right">
    <b-nav>
        <b-nav-item v-show="isLoggedIn">
          Capital: {{capital | currency}} 
        </b-nav-item>
        <b-nav-item v-show="isLoggedIn">
          Cash: {{getCash | currency}}
        </b-nav-item>
        
        <b-nav-item @click="openLogInModal" v-show="!isLoggedIn" >Log in</b-nav-item>
        <b-nav-item @click="openRegisterModal" v-show="!isLoggedIn" >Register</b-nav-item>

        <b-nav-item-dropdown v-bind:text="getUsername" right v-show="isLoggedIn">
          <router-link to="/portfolio" class="dropdown-item"> Portfolio </router-link>
            <b-dropdown-item @click="logout">Log out</b-dropdown-item>
          </b-nav-item-dropdown>
    </b-nav>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import userController from '@/controllers/User.controller'
  import cacheController from '@/controllers/Cache.controller'

  export default {
    props: {
      menuObjects : {
        type: Array
      }
    },
    data() {
      return {
        'capital': null
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
            this.capital += holdingStock.map(stock => stock.amount * stock.averagePrice)
                              .reduce((sum, current) => sum + current)
          }
          
        },
        deep: true
      }
    },
    methods: {
      ...mapActions([
        'openLogInModal',
        'setUsername',
        'setCash',
        'setStep',
        'openRegisterModal'
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
        this.setStep(1)
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