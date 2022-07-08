<script>
  import { push } from "svelte-spa-router";
  import { Button, Input, Label } from "sveltestrap";
  import API_CONFIG from "../../api";
  import { authToken } from "../../sessionStorage";
  import { get } from "svelte/store";
  import { AuthenticationApi } from "kumon_app_backend_api";
  import LoginForm from "./forms/LoginForm.svelte";
  import { onMount } from "svelte";

  // If the user is already logged in, go to the dashboard
  if (get(authToken)) {
    console.log(get(authToken));
    push("/dashboard");
  }

  // Form object
  let loginForm;

  // Link to the backend api
  let api = new AuthenticationApi(API_CONFIG);

  async function handleLogin(evt) {
    try {
      // Send a backend request to login
      let response = await api.authenticationLoginCreate({
        authTokenRequest: evt.detail,
      });

      // Set the local session storage
      $authToken = "Token " + response.token;

      // Refresh the page
      location.reload();
    } catch (e) {
      loginForm.setErrors(
        "Invalid Username and/or Password",
        "Invalid Username and/or Password"
      );
    }
  }

  // Check if the application is setup, if not, send to welcome pages
  onMount(async () => {
    try {
      await api.authenticationIsSetupRetrieve({});
    } catch (e) {
      push("#/welcome/");
    }
  });
</script>

<main>
  <div class="title">
    <h1>Kumon Management System</h1>

    <p>
      This is a management application for Kumon centers to manage attendance,
      inventory, record sheets and more ...
    </p>
  </div>

  <div class="form">
    <LoginForm id="login-form" bind:this={loginForm} on:submit={handleLogin} />
    <div class="loginButton">
      <Button form="login-form" color="primary" type="submit">Login</Button>
    </div>
  </div>

  <div class="forgot">
    <p>
      If you have forgotten your password please contact the system
      administrator (Kumon Instructor) who will be able to change it for you. If
      the administrator has forgotten their password press <a
        href="/#/forgotAdminPassword"
      >
        here
      </a>
    </p>
    ​
  </div>
</main>

<style>
  main {
    width: 100%;
    max-height: 100%;
    max-width: 40%;
    margin-left: auto;
    margin-right: auto;
  }

  .title {
    text-align: center;
    margin-top: 5%;
  }

  .form {
    margin-top: 20%;
    margin-bottom: 20%;
    margin-left: auto;
    margin-right: auto;
    max-width: 35%;
    min-width: 250px;
    text-align: left;
  }

  .form .loginButton {
    margin-top: 10px;
    float: right;
  }

  .forgot {
    padding-top: 15%;
    text-align: center;
    margin-bottom: 5%;
  }
</style>
