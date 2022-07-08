<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../api";
  import { BulkItemApi } from "kumon_app_backend_api";

  let bulkItemApi = new BulkItemApi(API_CONFIG);

  import InfoModal from "./InfoModal.svelte";
  import AddBulkItemForm from "../forms/AddBulkItemForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  export let id;

  /**
   * Callback for when a new student is added.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onChangesSaved = (newDetails) => {};

  /**
   * The backing form component for the "Add Bulk Item" form.
   * @type {addBulkItemForm}
   */
  // reuses the add bulk item form, as the attributes are identical
  let addBulkItemForm;

  /**
   * Loads the worksheet's current details into this form.
   * @param {number} id The ID of the worksheet.
   */
  async function loadBulkItemDetails(id) {
    try {
      let details = await bulkItemApi.bulkItemRetrieve({ id: id });
      addBulkItemForm.setDefaultValues(details);
      resetFields();
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit Bulk Item",
        message: `Could not load details for bulk item ${id}!`,
      });
    }
  }

  /**
   * Resets the fields to their original values.
   */
  function resetFields() {
    addBulkItemForm.reset();
  }

  /**
   * Handles submission of the new student details.
   */
  async function handleSubmit(details) {
    try {
      await bulkItemApi.bulkItemUpdate({ id: id, bulkItemRequest: details });

      // Reset the form (since svelte-modals re-uses the component instances)
      addBulkItemForm.reset();

      // Notify that we were successful
      openModal(
        InfoModal,
        {
          title: "Edit Bulk Item",
          message: "Successfully editted bulk item!",
        },
        { replace: true }
      );

      onChangesSaved(details);
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit Bulk Item",
        message: `Could not save details for new bulk item!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadBulkItemDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Edit Bulk Item`}>
    <ModalBody>
      <AddBulkItemForm
        id="edit-bulkitem-form"
        bind:this={addBulkItemForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="edit-bulkitem-form" type="submit">
        Submit
      </Button>
    </ModalFooter>
  </Modal>
{/if}
