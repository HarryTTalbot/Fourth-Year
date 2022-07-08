<script>
  import { push } from "svelte-spa-router";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";
  import API_CONFIG from "../../api";
  import { authToken } from "../../sessionStorage";
  import { get } from "svelte/store";
  import { AuthenticationApi } from "kumon_app_backend_api";
  import NewAccountForm from "./forms/NewAccountForm.svelte";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  // Whether the modal is open
  export let isOpen;

  // Form object
  let newAccountForm;

  export let onAdd = (newDetails) => {};

  // Link to the backend api
  let api = new AuthenticationApi(API_CONFIG);

  async function handleSubmit(evt) {
    try {
      // Send backend request to create a new account
      await api.authenticationNewAccountCreate({
        addAccountRequest: evt.detail,
      });

      // Close the modal
      isOpen = false;
      dispatch("done");
      onAdd(evt);
    } catch (e) {
      // Display the errors
      newAccountForm.setErrors(
        "Invalid Username and/or Password(s)",
        "Invalid Username and/or Password(s)",
        "Invalid Username and/or Password(s)"
      );
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={"Setup Login Details"}>
    <ModalBody>
      <NewAccountForm
        id="account-form"
        bind:this={newAccountForm}
        on:submit={handleSubmit}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button form="account-form" color="primary" type="submit"
        >Set Login Details</Button
      >
    </ModalFooter>
  </Modal>
{/if}
