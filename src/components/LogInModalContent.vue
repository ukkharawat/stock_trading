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
      handleUsernameChange(event) {
        this.username = event
      },
      handlePasswordChange(event) {
        this.password = event
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
