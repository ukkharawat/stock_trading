<template>
  <div id="navbar-header">
    <router-link to="/">
      <b-navbar-brand>{{ brandTitle }}</b-navbar-brand>
    </router-link>
  </div>
</template>

<script>

  export default {
    props: {
      brandTitle: {
        type: String
      }
    }
  }
</script>
