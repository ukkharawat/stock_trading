<template>
  <div id="log-in-modal-content">
    <b-row class="justify-content-sm-center">
      <b-col cols="8">
        <b-form @submit="login">
          <b-form-group id="usernameInputGroup"
                        label="Your Username:"
                        label-for="usernameInput">
            <b-form-input id="usernameInput"
                          type="text"
                          v-model="username"
                          required
                          placeholder="Username">
            </b-form-input>
          </b-form-group>
          <b-form-group id="passwordInputGroup"
                        label="Your Password:"
                        label-for="exampleInput2">
            <b-form-input id="passwordInput"
                          type="password"
                          v-model="password"
                          required
                          placeholder="Password">
            </b-form-input>
          </b-form-group>
          <b-button type="submit" class="margin-top" variant="warning">Log In</b-button>
        </b-form>
      </b-col>
    </b-row>
  </div>
</template>

<script>
  import userController from '@/controllers/User.controller'
  import cacheController from '@/controllers/Cache.controller'
  import stockDatasource from '@/datasources/Stock.datasource'
  import { mapActions } from 'vuex'

  export default {
    data() {
      return {
        username: null,
        password: null
      }
    },
    methods: {
      ...mapActions([
        'closeModal',
        'setUsername',
        'setCash',
        'setStep'
      ]),
      login(event) {
        event.preventDefault()
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
        stockDatasource.createChangedStockObject(data.portfolio[0])
        this.setCash(data.cash)
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
    margin-top: 8px;
    padding-bottom: 16px;
  }

  .form-group {
    padding-top: 8px;
    text-align: left;
  }

  .margin-top {
    margin-top: 16px;
  }

  .btn {
    width: 100%;
    color: #424242;
  }
</style>
