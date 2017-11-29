<template>
  <div id="navbar-right">
    <ul class="nav navbar-nav navbar-right">
      <li class="list-menu">
        <a class="disable-hover menu-padding" v-show="isLoggedIn">
          Capital: {{capital | currency}} ({{getCash | currency}})
          </a>
        <router-link to="/portfolio" v-show="isLoggedIn">
          <a class="disable-hover portfolio-link menu-padding">Portfolio</a>
        </router-link>
        <a class="disable-hover" @click="openLogInModal" v-show="!isLoggedIn" >Log in</a>
        <a class="disable-hover" @click="logout" v-show="isLoggedIn" >{{ getUsername }} (Log out)</a>
      </li>
    </ul>
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
          this.capital = this.getCash + this.getStock.map(stock => stock.amount * stock.price).reduce((sum, current) => sum + current)
        },
        deep: true
      }
    },
    methods: {
      ...mapActions([
        'openLogInModal',
        'setUsername',
        'setCash',
        'setStep'
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

<style>
  .disable-hover {
    cursor: pointer;
  }

  .list-menu a {
    text-decoration: none;
  }

  .menu-padding {
    padding-right: 16px;
  }

  .portfolio-link, .portfolio-link:hover {
    color: #424242 !important;
    text-decoration: none;
  }

  a.disable-hover:hover {
    background-color: transparent !important;
  }
</style>
