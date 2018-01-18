<template>
  <div class="modal-content">
      <b-row class="justify-content-sm-center">
        <b-col cols="8">
          <b-form @submit="register">
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
                          label-for="passwordInput">
              <b-form-input id="passwordInput"
                            type="text"
                            v-model="password"
                            required
                            placeholder="Password">
              </b-form-input>
            </b-form-group>
            <b-form-group id="rePasswordInputGroup"
                          label="Type Your Password Again:"
                          label-for="rePasswordInput">
              <b-form-input id="rePasswordInput"
                            type="text"
                            v-model="repassword"
                            required
                            placeholder="Re-password">
              </b-form-input>
            </b-form-group>
            <b-button type="submit" class="margin-top" variant="warning">Register</b-button>
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