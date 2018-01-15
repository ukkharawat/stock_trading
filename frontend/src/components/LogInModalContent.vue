<template>
  <div id="log-in-modal-content">
    <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-sm-6">
        <textInput :placeholder="'Username'"
                   @handleValueChange="handleUsernameChange">
        </textInput>
        <passwordInput :placeholder="'Password'"
                       @handleValueChange="handlePasswordChange">
        </passwordInput>
        <actionButton :buttonClass="'log-in-button'"
                      @onClick="login"
                      :message="'Log in'">
        </actionButton>
      </div>
      <div class="col-sm-3"></div>
    </div>
  </div>
</template>

<script>
  import textInput from '@/components/TextInput'
  import passwordInput from '@/components/PasswordInput'
  import actionButton from '@/components/ActionButton'
  import userController from '@/controllers/User.controller'
  import cacheController from '@/controllers/Cache.controller'
  import { mapActions } from 'vuex'

  export default {
    data() {
      return {
        username: null,
        password: null
      }
    },
    components: {
      textInput,
      actionButton,
      passwordInput
    },
    methods: {
      ...mapActions([
        'closeModal',
        'setUsername',
        'setCash',
        'setStep'
      ]),
      handleUsernameChange(event) {
        this.username = event
      },
      handlePasswordChange(event) {
        this.password = event
      },
      login() {
        userController.login(this.username, this.password)
          .then(response => {
            this.setUserCache(response)
            this.closeModal()
          })
      },
      setUserCache(response) {
        this.setLocalStorage(response)
        this.setVuex(response)
      },
      setVuex(data) {
        this.setUsername(data.username)
        this.setStep(data.stepCount)
        
        let stock = {
          'symbol': response.portfolio[0].symbol,
          'amount': response.portfolio[0].volume,
          'averageBuyPrice': response.portfolio[0].averagePrice
        }
            
        this.setCash(response.cash)
        this.updateStock(stock)
      },
      setLocalStorage(data) {
        cacheController.setUserCache(data.username, data.Token)
      }
    }
  }
</script>

<style>

  #log-in-modal-content {
    width: 100%;
    margin-top: 24px;
    padding-bottom: 24px;
  }
</style>
