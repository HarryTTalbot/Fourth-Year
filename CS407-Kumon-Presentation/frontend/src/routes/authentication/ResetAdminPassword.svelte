<script>
  import { push } from "svelte-spa-router";
  import { Button, Input, Label } from "sveltestrap";
  import API_CONFIG from "../../api";
  import { authToken } from "../../sessionStorage";
  import { get } from "svelte/store";
  import { AuthenticationApi } from "kumon_app_backend_api";
  import ResetAdminPasswordForm from "./forms/ForgotAdminPasswordForm.svelte";
  import InfoModal from "../../modals/InfoModal.svelte";
  import { Modals, closeModal, openModal } from "svelte-modals";

  // If the user is already logged in, go to the dashboard
  if (get(authToken)) {
    console.log(get(authToken));
    push("/dashboard");
  }

  // Form object
  let resetForm;

  // Link to the backend api
  let api = new AuthenticationApi(API_CONFIG);

  async function handleReset(evt) {
    try {
      // Send a backend request to reset the pasword
      await api.authenticationAdminForgotPasswordCreate({
        forgotAdminPasswordRequest: evt.detail,
      });

      // Open a confirmation modal
      openModal(InfoModal, {
        title: "Reset Admin Password",
        message: "Admin Password Successfully Reset!",
      });

      // Go to the login page
      push("/");
    } catch (e) {
      // Display the errors
      resetForm.setErrors(
        "Invalid Username and/or Password",
        "Invalid Username and/or Password",
        "Invalid Username and/or Password"
      );
    }
  }
</script>

<main>
  <div class="title">
    <h1>Reset Admin Password</h1>

    <p>
      To reset the admin password you have to enter the passcode you created
      when first setting up the application. Without this, you will be unable to
      change the password
    </p>
  </div>

  <div class="form">
    <ResetAdminPasswordForm
      id="reset-form"
      bind:this={resetForm}
      on:submit={handleReset}
    />
    <div class="resetButton">
      <Button form="reset-form" color="primary" type="submit"
        >Reset Password</Button
      >
    </div>
  </div>

  <div class="forgot">
    <p>
      If you cannot remember your passcode, your only option is to reset the
      application which will cause you to lose all data. To do this press <a
        href="/#/reset"
      >
        reset
      </a>
    </p>
    ​
  </div>
</main>

<style>
  main {
    width: 100%;
    max-width: 40%;
    max-height: 100%;
    margin-left: auto;
    margin-right: auto;
  }

  .title {
    text-align: center;
    margin-top: 5%;
  }

  .form {
    margin-top: 10%;
    margin-bottom: 10%;
    margin-left: auto;
    margin-right: auto;
    max-width: 35%;
    min-width: 250px;
    text-align: left;
  }

  .form .resetButton {
    margin-top: 10px;
    float: right;
  }

  .forgot {
    padding-top: 10%;
    text-align: center;
    margin-bottom: 5%;
  }
</style>
