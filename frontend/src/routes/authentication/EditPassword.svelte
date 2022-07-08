<script>
  import { push } from "svelte-spa-router";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";
  import API_CONFIG from "../../api";
  import { authToken } from "../../sessionStorage";
  import { get } from "svelte/store";
  import { AuthenticationApi } from "kumon_app_backend_api";
  import EditPasswordForm from "./forms/EditPasswordForm.svelte";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  // Whether the modal is open
  export let isOpen;

  // Form object
  let editPasswordForm;

  // Link to the backend api
  let api = new AuthenticationApi(API_CONFIG);

  async function handleSubmit(evt) {
    try {
      // Send a backend request to edit the pasword
      await api.authenticationEditPasswordCreate({
        editPasswordRequest: evt.detail,
      });

      // Close the modal
      isOpen = false;
      closeModal();
      dispatch("done");
    } catch (e) {
      // Display the errors
      editPasswordForm.setErrors(
        "Invalid Password(s)",
        "Invalid Password(s)",
        "Invalid Password(s)"
      );
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={"Change Password"}>
    <ModalBody>
      <EditPasswordForm
        id="edit-form"
        bind:this={editPasswordForm}
        on:submit={handleSubmit}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button form="edit-form" color="primary" type="submit"
        >Change Password</Button
      >
    </ModalFooter>
  </Modal>
{/if}
