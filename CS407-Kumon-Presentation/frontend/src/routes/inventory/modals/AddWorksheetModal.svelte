<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../api";
  import { WorksheetApi } from "kumon_app_backend_api";

  export let worksheetApi = new WorksheetApi(API_CONFIG);

  import InfoModal from "./InfoModal.svelte";
  import AddWorksheetForm from "../forms/AddWorksheetForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * Callback for when a new worksheet is added.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for worksheets.
   */
  export let onAdd = (newDetails) => {};

  /**
   * The backing form component for the "Add Worksheet" form.
   * @type {WorksheetForm}
   */
  let addWorksheetForm;

  /**
   * Handles submission of the new worksheet details.
   * @param details The new details that were chosen. Matches the API endpoint's format for worksheets.
   */
  async function handleSubmit(details) {
    try {
      // await a response from the backend
      await worksheetApi.worksheetCreate({ worksheetEditRequest: details });

      // Reset the form (since svelte-modals re-uses the component instances)
      addWorksheetForm.reset();

      // Notify that we were successful
      openModal(
        InfoModal,
        {
          title: "Add Worksheet",
          message: "Successfully added worksheet!",
        },
        { replace: true }
      );

      onAdd(details);
    } catch (e) {
      openModal(InfoModal, {
        title: "Add Worksheet",
        message: `Could not save details for new worksheet!`,
      });
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Add Worksheet`}>
    <ModalBody>
      <AddWorksheetForm
        id="add-worksheet-form"
        bind:this={addWorksheetForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="add-worksheet-form" type="submit">
        Submit
      </Button>
    </ModalFooter>
  </Modal>
{/if}
