<template>
  <div id="navbar-brand">
    <router-link to="/">
      <a class="navbar-brand">{{brandTitle}}</a>
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
