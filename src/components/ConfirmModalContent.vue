<template>
  <div id="confirm-modal-content" v-if="actionInfo != null">
    <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-sm-6 remove-padding">
        <h2 class="cautions">
          Do you want to {{actionInfo.action}} {{actionInfo.amount}} shares of {{actionInfo.shortName}} ?
        </h2>

        <div class="row">
          <div class="col-sm-6">
            <confirmModalButton :buttonClass="'yes-button'"
                                @onClickEvent="handleClickYes"
                                :message="'YES'">
            </confirmModalButton>
          </div>
          <div class="col-sm-6">
            <confirmModalButton :buttonClass="'no-button'"
                                @onClickEvent="handleClickNo"
                                :message="'NO'">
            </confirmModalButton>
          </div>
        </div>
      </div>
      <div class="col-sm-3"></div>
    </div>
  </div>
</template>

<script>
  import confirmModalButton from '@/components/ConfirmModalButton'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    props: {
      actionInfo: {
        type: Object
      }
    },
    components: {
      confirmModalButton
    },
    computed: {
      ...mapGetters([
        'getNextActionInfo'
      ])
    },
    methods: {
      ...mapActions([
        'closeModal',
        'buyStock',
        'sellStock',
        'updateCapital'
      ]),
      handleClickYes() {
        let action = this.getNextActionInfo.action
        let actionObject = this.createActionObject()

        if(action === "buy") {
          this.buyStock(actionObject)
        } else {
          this.sellStock(actionObject)
        }

        this.updateCapital()
        this.closeModal()
      },
      handleClickNo() {
        this.closeModal()
      },
      createActionObject() {
        return {
          "shortName": this.getNextActionInfo.shortName,
          "amount": this.getNextActionInfo.amount,
          "price": this.getNextActionInfo.price
        }
      }
    }
  }
</script>

<style>
  #confirm-modal-content {
    width: 100%;
    margin-top: 24px;
    padding-bottom: 24px;
  }

  .cautions {
    text-align: left;
    font-size: 24px;
    margin-bottom: 24px;
  }

  .remove-padding {
    padding: 0 8px;
  }
</style>
