<template>
  <div id="modal-box-content">
    <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-sm-6">
        <textInput :placeholder="'Username'"></textInput>
        <passwordInput :placeholder="'Password'"></passwordInput>
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
    components: {
      textInput,
      actionButton,
      passwordInput
    }
  }
</script>

<style>

  #modal-box-content {
    width: 100%;
    margin-top: 24px;
    padding-bottom: 24px;
  }
</style>
