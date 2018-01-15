<template>
  <div class="base-modal" @click.stop>
    <modalHeader :message="message"></modalHeader>
    <confirmModalContent :actionInfo="getNextActionInfo">
    </confirmModalContent>
  </div>
</template>

<script>
  import modalHeader from '@/components/ModalHeader'
  import confirmModalContent from '@/components/ConfirmModalContent'
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        message: "Confirmation"
      }
    },
    components: {
      modalHeader,
      confirmModalContent
    },
    computed: {
      ...mapGetters([
        'getNextActionInfo'
      ])
    }
  }
</script>