<template>
  <div id="confirm-modal" @click.stop>
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

<style>
  #confirm-modal {
    background-color: #fafafa;
    width: 50%;
    height: auto;
    border-radius: 8px;
  }
</style>
