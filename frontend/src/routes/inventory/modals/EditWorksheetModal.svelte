<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../api";
  import { WorksheetApi } from "kumon_app_backend_api";

  export let worksheetApi = new WorksheetApi(API_CONFIG);

  import InfoModal from "./InfoModal.svelte";

  import EditWorksheetForm from "../forms/EditWorksheetForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  export let id;

  /**
   * Callback for when a new worksheet is added.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for worksheets.
   */
  export let onChangesSaved = (newDetails) => {};

  /**
   * The backing form component for the "Add Worksheet" form.
   * @type {editWorksheetForm}
   */
  let editWorksheetForm;

  /**
   * Loads the worksheet's current details into this form.
   */
  async function loadWorksheetDetails() {
    try {
      // Retrieve worksheet details - id is obtained from private variable, not parameter
      let details = await worksheetApi.worksheetRetrieve({ id: id });
      details.subject = details.subject.id;
      details.subjectLevel = details.subjectLevel.id;
      editWorksheetForm.setDefaultValues(details);
      resetFields();
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit Worksheet",
        message: `Could not load details for worksheet ${id}!`,
      });
    }
  }

  /**
   * Resets the fields to their original values.
   */
  function resetFields() {
    editWorksheetForm.reset();
  }

  /**
   * Handles submission of the new worksheet details.
   */
  async function handleSubmit(details) {
    try {
      await worksheetApi.worksheetUpdate({
        id: id,
        worksheetEditRequest: details,
      });

      // Reset the form (since svelte-modals re-uses the component instances)
      editWorksheetForm.reset();

      // Notify that we were successful
      openModal(
        InfoModal,
        {
          title: "Edit Worksheet",
          message: "Successfully edited worksheet!",
        },
        { replace: true }
      );

      onChangesSaved(details);
    } catch (e) {
      openModal(InfoModal, {
        title: "Add Worksheet",
        message: `Could not save details for new worksheet!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadWorksheetDetails();
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Edit Worksheet`}>
    <ModalBody>
      <EditWorksheetForm
        id="edit-worksheet-form"
        bind:this={editWorksheetForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="edit-worksheet-form" type="submit">
        Submit
      </Button>
    </ModalFooter>
  </Modal>
{/if}
