<template>
  <div id="navbar-right">
    <ul class="nav navbar-nav navbar-right">
      <li class="list-menu">
        <a class="disable-hover menu-padding" v-if="isLoggedIn">
          Capital: {{getCapital | currency}} ({{getCash | currency}})
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

  export default {
    props: {
      menuObjects : {
        type: Array
      }
    },
    computed: {
      ...mapGetters([
        'getCapital',
        'getCash',
        'getUsername',
        'isLoggedIn'
      ])
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
              userController.clearUserCache()
              this.clearVuex()
            }
          })
      },
      clearVuex() {
        this.setUsername(null)
        this.setCash(null)
        this.setStep(null)
      }
    },
    filters: {
      currency(value) {
        if (!value) return ''
        value = value.toFixed(2).toString()
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
