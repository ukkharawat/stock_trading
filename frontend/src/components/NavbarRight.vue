<template>
  <div id="navbar-right">
    <ul class="nav navbar-nav navbar-right">
      <li class="list-menu">
        <a class="disable-hover menu-padding">Capital: {{getCapital | currency}} ({{getCash | currency}})</a>
        <router-link to="/portfolio">
          <a class="disable-hover portfolio-link menu-padding">Portfolio</a>
        </router-link>
        <a class="disable-hover" @click="openLogInModal" v-show="!getUser" >Log in</a>
        <a class="disable-hover" @click="openLogInModal" v-show="getUser" >{{ getUser }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
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
        'getUser'
      ])
    },
    methods: {
      ...mapActions([
        'openLogInModal'
      ])
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
