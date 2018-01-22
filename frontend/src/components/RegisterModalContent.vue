<template>
  <div class="modal-content">
      <b-row class="justify-content-sm-center">
        <b-col cols="8">
          <b-form @submit="register">
            <b-form-group id="registerUsernameInputGroup"
                          label="Your Username:"
                          label-for="registerUsernameInput">
              <b-form-input id="registerUsernameInput"
                            type="text"
                            name="username"
                            v-model="username"
                            v-validate="'required|min:8|alpha'"
                            placeholder="Username">
              </b-form-input>
              <span v-show="errors.has('username')" 
                    class="help text-danger">{{ errors.first('username') }}</span>
            </b-form-group>

            <b-form-group id="registerPasswordInputGroup"
                          label="Your Password:"
                          label-for="registerPasswordInput">
              <b-form-input id="registerPasswordInput"
                            type="password"
                            name="password"
                            v-model="password"
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
                            v-validate="'required|min:8|verify_password'"
                            placeholder="Re-password">
              </b-form-input>
              <span v-show="(repassword != null && password != repassword)" 
                    class="help text-danger">Your password doesn't match</span>
            </b-form-group>

            <b-button type="submit" class="margin-top" variant="warning"
                :disabled="!isFieldComplete || errors.any()">Register</b-button>
          </b-form>
        </b-col>
      </b-row>
  </div>
</template>

<script>
  import userController from "@/controllers/User.controller"
  import { mapActions } from "vuex"

  export default {
    data() {
      return {
        username: null,
        password: null,
        repassword: null
      };
    },
    computed: {
      isFieldComplete() {
        return  this.username != null && 
                this.password != null && 
                this.repassword != null && 
                this.repassword == this.password
      }
    },
    methods: {
      ...mapActions(["closeModal"]),
      isPasswordMatch() {
        return this.password === this.repassword
      },
      register(event) {
        event.preventDefault()

        if (this.isPasswordMatch()) {
          userController.register(this.username, this.password)
            .then(response => {
              this.closeModal()
            })
        }
      }
    }
  };
</script>