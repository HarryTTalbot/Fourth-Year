<script>
  import Router, { push } from "svelte-spa-router";
  import routes from "./routes";
  import { onMount } from "svelte";
  import { authToken } from "./sessionStorage";
  import { get } from "svelte/store";
  import { fade } from "svelte/transition";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import "bootstrap/dist/js/bootstrap";
  import "bootstrap/dist/css/bootstrap.min.css";
  import { AuthenticationApi } from "kumon_app_backend_api";
  import API_CONFIG, { getConfig } from "./api";

  // Check if the user should be redirected to the login page
  async function authenticate() {
    // Get the url extension of the current page
    let urlHash = window.location.hash;

    // 1 - Check if the user is on the welcome setup pages
    if (
      urlHash === "#/welcome/" ||
      urlHash === "#/welcome/import" ||
      urlHash === "#/welcome/setup" ||
      urlHash === "#/forgotAdminPassword"
    ) {
      return true;
    }

    // 2 - Check if the user is logged in
    if (get(authToken)) {
      return true;
    } else {
      // If the user is on the login page
      if (urlHash === "" || urlHash === "#/") {
        return true;
      }
      return false;
    }
  }
</script>

<main>
  <!-- Code for displaying any modal in the interface -->
  <Modals>
    <div
      slot="backdrop"
      class="backdrop"
      transition:fade
      on:click={closeModal}
    />
  </Modals>

  <!-- Check whether the login page should be loaded -->
  {#await authenticate()}
    <p>Loading ...</p>
  {:then code}
    {#if code}
      <!-- Display the website -->
      <Router {routes} />
    {:else}
      <!-- Display a link to the login -->
      <div class="link">
        <p>You are no longer logged in!</p>
        <a class="btn btn-outline-primary" href="/">Go to Login</a>
      </div>
    {/if}
  {:catch error}
    <h1>Something has gone wrong!</h1>
    <p>{error}</p>
  {/await}
</main>

<style>
  .link {
    margin: auto;
    width: 20%;
  }
</style>
