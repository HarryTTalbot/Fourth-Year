<script>
  import { Button, Container } from "sveltestrap";
  import { createEventDispatcher } from "svelte";
  import AdminAccountForm from "../forms/AdminAccountForm.svelte";
  import { AuthenticationApi } from "kumon_app_backend_api";
  import API_CONFIG from "../../../api";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import { authToken } from "../../../sessionStorage";

  // Object for the form
  let accountForm;

  // Link to the backend api
  let api = new AuthenticationApi(API_CONFIG);

  const dispatch = createEventDispatcher();

  async function handleSubmit(evt) {
    try {
      // Send a request to create an admin account
      await api.authenticationNewAdminAccountCreate({
        addAdminAccountRequest: evt.detail,
      });

      // Send a request to fetch the token for the API Configuration
      let response = await api.authenticationLoginCreate({
        authTokenRequest: evt.detail,
      });

      // Set the authentication token
      $authToken = "Token " + response.token;
      nextStage();
    } catch (e) {
      // Open a modal to tell the user that there was an issue
      openModal(InfoModal, {
        title: "Create Admin Account",
        message: "Could not create the admin account!",
      });
    }
  }

  function nextStage() {
    dispatch("done");
  }
</script>

<Container>
  <p>Firstly, you will need to set up an Administrator account.</p>
  <AdminAccountForm
    id="form"
    class="w-50"
    bind:this={accountForm}
    on:submit={handleSubmit}
  />
  <Button form="form" color="primary" type="submit">Create</Button>
</Container>
