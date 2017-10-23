<template>
  <div id="navbar-right">
    <ul class="nav navbar-nav navbar-right">
      <li>
        <a class="disable-hover">Log in</a>
      </li>
    </ul>
  </div>
</template>

<script>

  export default {
    props: {
      menuObjects : {
        type: Array
      }
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
