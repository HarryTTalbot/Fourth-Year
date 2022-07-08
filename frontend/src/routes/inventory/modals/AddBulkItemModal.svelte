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

  /**
   * Callback for when a new bulk item is added.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for bulk items.
   */
  export let onAdd = (newDetails) => {};

  /**
   * The backing form component for the "Add Bulk Item" form.
   * @type {AddBulkItemForm}
   */
  let addBulkItemForm;

  /**
   * Handles submission of the new bulk item details.
   * @param details The new details that were chosen. Matches the API endpoint's format for bulk items.
   */
  async function handleSubmit(details) {
    try {
      await bulkItemApi.bulkItemCreate({ bulkItemRequest: details });

      // Reset the form (since svelte-modals re-uses the component instances)
      addBulkItemForm.reset();

      // Notify that we were successful
      openModal(
        InfoModal,
        {
          title: "Add Bulk Item",
          message: "Successfully added bulk item!",
        },
        { replace: true }
      );

      onAdd(details);
    } catch (e) {
      openModal(InfoModal, {
        title: "Add Bulk Item",
        message: `Could not save details for new bulk item!`,
      });
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Add Bulk Item`}>
    <ModalBody>
      <AddBulkItemForm
        id="add-bulkitem-form"
        bind:this={addBulkItemForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="add-bulkitem-form" type="submit">
        Submit
      </Button>
    </ModalFooter>
  </Modal>
{/if}
