<template>
  <div id="navbar-right">
    <ul class="nav navbar-nav navbar-right">
      <li>
        <a class="disable-hover" @click="openModal">Log in</a>
      </li>
    </ul>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'
  export default {
    props: {
      menuObjects : {
        type: Array
      }
    },
    methods: {
      ...mapActions([
        'openModal'
      ])
    }
  }
</script>

<style>
  .disable-hover {
    cursor: pointer;
  }

  a.disable-hover:hover {
    background-color: transparent !important;
  }
</style>
