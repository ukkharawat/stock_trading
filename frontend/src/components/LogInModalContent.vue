<template>
  <div class="modal-content">
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
          <b-button type="submit" class="margin-top" variant="warning"
                :disabled="username == null || password == null">Log In</b-button>
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
          .catch(error => console.log(error))
      },
      setUserCache(response) {
        this.setLocalStorage(response)
        this.setVuex(response)
      },
      setVuex(data) {
        this.setUsername(data.username)
        this.setStep(data.stepCount)
        this.setCash(data.cash)
        
        if(this.isPortfolioExist(data)) {
          stockDatasource.createChangedStockObject(data.portfolio[0])
        }
      },
      setLocalStorage(data) {
        cacheController.setUserCache(data.username, data.Token)
      },
      isPortfolioExist(data) {
        return data.portfolio != null && data.portfolio != undefined && data.portfolio.length > 0
      }
    }
  }
</script>