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