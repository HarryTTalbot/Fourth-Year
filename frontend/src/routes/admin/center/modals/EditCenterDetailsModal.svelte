<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import InfoModal from "../../../../modals/InfoModal.svelte";
  import CenterDetailsForm from "../../../setup/forms/CenterDetailsForm.svelte";

  import API_CONFIG, { getConfig } from "../../../../api";
  import { CenterDetailsApi } from "kumon_app_backend_api";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * Callback for when changes were saved for the center details.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format
   */
  export let onChangesSaved = (newDetails) => {};

  let form;

  /**
   * Loads the center's current details into this form.
   */
  async function loadCenterDetails() {
    try {
      // Link to the backend api
      let api = new CenterDetailsApi(getConfig());

      // Query the Backend
      let response = await api.centerDetailsFetchRetrieve({});

      // Set the values of the form
      form.setDefaultValues(response);
      resetFields();
    } catch (e) {}
  }

  /**
   * Resets the fields to their original values.
   */
  function resetFields() {
    editStudentForm.reset();
  }

  /**
   * Handles submission of the new center details.
   */
  async function handleSubmit(evt) {
    try {
      let api = new CenterDetailsApi(getConfig()); // Link to the backend api
      await api.centerDetailsCreate({ centerDetailsRequest: evt.detail });

      // Notify that we were successful
      onChangesSaved(e.detail);

      // Close the modal and open up another telling the user the task was successful
      closeModal();
      openModal(InfoModal, {
        title: "Set Center Details",
        message: "Successfully set the center details!",
      });
    } catch (e) {
      // Open up a new modal telling the user the task was not successful
      openModal(InfoModal, {
        title: "Set Center Details",
        message: "Could not set the center details!",
      });
    }
  }

  $: loadCenterDetails();
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Edit Center Details`}>
    <ModalBody>
      <CenterDetailsForm id="form" bind:this={form} on:submit={handleSubmit} />
    </ModalBody>
    <ModalFooter>
      <Button color="warning" outline on:click={resetFields}>
        Reset to Original Values
      </Button>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="form" type="submit">Save Changes</Button>
    </ModalFooter>
  </Modal>
{/if}
