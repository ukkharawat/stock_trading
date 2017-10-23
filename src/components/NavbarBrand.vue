<template>
  <div id="navbar-brand">
    <a class="navbar-brand" href="#">{{brandTitle}}</a>
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
