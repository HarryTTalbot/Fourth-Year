<script>
  import { push } from "svelte-spa-router";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";
  import API_CONFIG from "../../api";
  import { authToken } from "../../sessionStorage";
  import { get } from "svelte/store";
  import { AuthenticationApi } from "kumon_app_backend_api";
  import ForgotPasswordForm from "./forms/ForgotPasswordForm.svelte";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  // Whether the modal is open
  export let isOpen;

  // Staff details
  export let staffName = "";
  export let staffID = -1;

  // Form object
  let forgotPasswordForm;

  // Link to the backend api
  let api = new AuthenticationApi(API_CONFIG);

  async function handleSubmit(evt) {
    try {
      // Send a backend request to reset the password
      let requestDetails = evt.detail;
      requestDetails.staffId = staffID;
      await api.authenticationAdminSetPasswordCreate({
        setPasswordRequest: requestDetails,
      });

      // Close the modal
      isOpen = false;
      dispatch("done");
      closeModal();
    } catch (e) {
      // Display the errors
      if (e.status == 403) {
        forgotPasswordForm.setErrors("Unauthorised", "Unauthorised");
      } else {
        forgotPasswordForm.setErrors(
          "Invalid Password(s)",
          "Invalid Password(s)"
        );
      }
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={"Admin Overwrite Password"}>
    <ModalBody>
      <h3>Staff: {staffName}</h3>
      <ForgotPasswordForm
        id="forgot-form"
        bind:this={forgotPasswordForm}
        on:submit={handleSubmit}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button form="forgot-form" color="primary" type="submit"
        >Overwrite Password</Button
      >
    </ModalFooter>
  </Modal>
{/if}
