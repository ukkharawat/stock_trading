<template>
  <div id="navbar-header">
    <a href="/">
      <b-navbar-brand>{{ brandTitle }}</b-navbar-brand>
    </a>
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
