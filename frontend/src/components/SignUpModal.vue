<template>
  <div class="modal" @click="closeModal" :style="{'display': isModalOpen}">
    <div class="base-modal" @click.stop>
      <div class="modal-header">
        <h4 class="modal-title">Become a part of us</h4>
        <button class="close" @click="closeModal">x</button>
      </div>

      <div class="modal-content">
        <b-row class="justify-content-sm-center">
          <b-col cols="8">
            <b-form @submit="signUp">
              <b-form-group id="registerUsernameInputGroup"
                            label="Your Username:"
                            label-for="registerUsernameInput">
                <b-form-input id="registerUsernameInput"
                              type="text"
                              name="username"
                              v-model="username"
                              v-validate="'required|min:8|alpha'"
                              :class="{'is-invalid': errors.has('username') || isSignUpFailed }"
                              placeholder="Username">
                </b-form-input>
                <span v-show="errors.has('username')" 
                      class="help text-danger">{{ errors.first('username') }}</span>
                <span v-show="isSignUpFailed" 
                      class="help text-danger">This username has been taken</span>

              </b-form-group>

              <b-form-group id="registerPasswordInputGroup"
                            label="Your Password:"
                            label-for="registerPasswordInput">
                <b-form-input id="registerPasswordInput"
                              type="password"
                              name="password"
                              v-model="password"
                              :class="{'is-invalid': errors.has('password')}"
                              v-validate="'required|min:8|verify_password'"
                              placeholder="Password">
                </b-form-input>
                <span v-show="errors.has('password')" 
                      class="help text-danger">{{ errors.first('password') }}</span>
              </b-form-group>

              <b-form-group id="registerRepasswordInputGroup"
                            label="Type Your Password Again:"
                            label-for="registerRepasswordInput">
                <b-form-input id="registerRepasswordInput"
                              type="password"
                              v-model="repassword"
                              :class="{'is-invalid': !isPasswordMatch}"
                              v-validate="'required|min:8|verify_password'"
                              placeholder="Re-password">
                </b-form-input>
                <span v-show="(repassword != null && !isPasswordMatch)" 
                      class="help text-danger">Your password doesn't match</span>
              </b-form-group>

              <b-button type="submit" class="margin-top" variant="primary"
                  :disabled="!isFieldComplete || errors.any() || !isPasswordMatch">Sign up</b-button>
            </b-form>
          </b-col>
        </b-row>
      </div>
    </div>
  </div>
</template>

<script>
  import userController from "@/controllers/User.controller"
  import cacheController from "@/controllers/Cache.controller"
  import { mapActions } from "vuex"

  export default {
    data() {
      return {
        username: null,
        password: null,
        repassword: null,
        isSignUpFailed: false,
        isModalOpen: 'none'
      }
    },
    computed: {
      isFieldComplete() {
        return  this.username != null && 
                this.password != null && 
                this.repassword != null
      },
      isPasswordMatch() {
        return this.repassword == this.password
      }
    },
    methods:{
      ...mapActions([
        'setUsername',
        'setCash'
      ]),
      openModal() {
        this.isModalOpen = 'flex'
      },
      closeModal() {
        this.isModalOpen = 'none'
      },
      signUp(event) {
        event.preventDefault()

        userController.signUp(this.username, this.password)
          .then(response => {
            this.fetchUserDetail(response)
            this.closeModal()
          })
          .catch(error => {
            this.isSignUpFailed = true
          })
      },
      fetchUserDetail(user) {
        cacheController.setUserCache(user.username, user.Token)
        this.setUsername(user.username)
        this.setCash(user.cash)
      }
    },
    watch: {
      username(val) {
        this.isSignUpFailed = false
      }
    }
  }
</script>
