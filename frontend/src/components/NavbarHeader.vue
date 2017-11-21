<template>
  <div id="navbar-header" class="navbar-header">
    <navbarBrand :brandTitle="brandTitle"></navbarBrand>
  </div>
</template>

<script>
  import navbarBrand from '@/components/NavbarBrand'

  export default {
    components: {
      navbarBrand
    },
    props: {
      brandTitle: {
        type: String
      }
    }
  }
</script>
