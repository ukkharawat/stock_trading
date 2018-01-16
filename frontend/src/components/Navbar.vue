<template>
	<b-navbar class="stock-navbar">
		<div class="container-fluid">
			<navbarHeader :brandTitle="brandTitle"></navbarHeader>
			<navbarRight></navbarRight>
		</div>
	</b-navbar>
</template>

<script>
  import navbarHeader from '@/components/NavbarHeader'
  import navbarRight from '@/components/NavbarRight'

  export default {
    data() {
      return {
        brandTitle: "Brand"
      }
    },
    components: {
      navbarHeader: navbarHeader,
      navbarRight: navbarRight
    }
  }
</script>

<style>
	.stock-navbar {
		background-color : #ffc400;
		box-shadow: 0 4px 2px 0 rgba(0, 0, 0, 0.1);
    border-radius: 0 !important;
	}
</style>
