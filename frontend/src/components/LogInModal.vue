<template>
  <div>
    <div class="modal" @click="closeModal" :style="{'display': isModalOpen}">
      <div class="base-modal" @click.stop>
        <div class="modal-header">
          <h4 class="modal-title">Log in to begin trading</h4>
          <button class="close" @click="closeModal">x</button>
        </div>

        <div class="modal-content">
          <b-row class="justify-content-sm-center">
            <b-col cols="8">
              <b-form @submit="login">
                <h5 class="text-danger margin-top"
                    v-show="isLoginFailed">Your username or password is invalid.</h5>
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
                <b-button type="submit" class="margin-top" variant="primary"
                      :disabled="username == null || password == null">Log in</b-button>
              </b-form>
            </b-col>
          </b-row>
        </div>
      </div>
    </div>
    <loader ref="loader"></loader>
  </div>
</template>

<script>
  import userController from '@/controllers/User.controller'
  import cacheController from '@/controllers/Cache.controller'
  import stockDatasource from '@/datasources/Stock.datasource'
  import loader from '@/components/Loader.vue'
  import { mapActions } from 'vuex'

  export default {
    data() {
      return {
        username: null,
        password: null,
        isLoginFailed: false,
        isModalOpen: 'none'
      }
    },
    components: {
      loader
    },
    watch: {
      username(val) {
        this.isLoginFailed = false
      },
      password(val) {
        this.isLoginFailed = false
      }
    },
    methods: {
       ...mapActions([
        'setUsername',
        'setCash',
        'updateStock'
      ]),
      openModal() {
        this.isModalOpen = 'flex'
      },
      closeModal() {
        this.isModalOpen = 'none'
      },
      login(event) {
        event.preventDefault()
        userController.login(this.username, this.password)
          .then(response => {
            this.fetchCache(response)
            this.closeModal()
            this.$refs.loader.activateLoader()
          })
          .catch(error => {
            this.isLoginFailed = true
          })
      },
      fetchCache(response) {
        this.setLocalStorage(response)
        this.setUserDetail(response)
        this.setPortfolio(response.portfolio)
      },
      setPortfolio(portfolio) {
        if(this.isPortfolioExist(portfolio)) {
          let stocks = portfolio.map(stock => stockDatasource.createChangedStockObject(stock))
          this.updateStock(stocks)
        }
      },
      setLocalStorage(data) {
        cacheController.setUserCache(data.username, data.Token)
      },
      setUserDetail(data) {
        this.setUsername(data.username)
        this.setCash(data.cash)
      },
      isPortfolioExist(portfolio) {
        return portfolio != null && portfolio != undefined && portfolio.length > 0
      }
    }
  }
</script>
