<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../api";
  import { LendableItemApi } from "kumon_app_backend_api";

  import InfoModal from "./InfoModal.svelte";
  import AddLendableItemForm from "../forms/AddLendableItemForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  export let id;

  /**
   * Callback for when a new lendable item is added.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for lendable items.
   */
  export let onChangesSaved = async (newDetails) => {};

  /**
   * The backing form component for the "Add Lendable Item" form.
   * @type {addLendableItemForm}
   */
  let addLendableItemForm;

  let lendableItemApi = new LendableItemApi(API_CONFIG);

  /**
   * Loads the worksheet's current details into this form.
   * @param {number} id The ID of the worksheet.
   */
  async function loadLendableItemDetails(id) {
    try {
      let details = await lendableItemApi.lendableItemRetrieve({ id: id });
      addLendableItemForm.setDefaultValues(details);
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
    addLendableItemForm.reset();
  }

  /**
   * Handles submission of the new student details.
   */
  async function handleSubmit(details) {
    try {
      // await bulkItemApi.bulkItemUpdate({ id: id, bulkItemRequest: details });
      await lendableItemApi.lendableItemUpdate({
        id: id,
        lendableItemEditRequest: details,
      });
      // Reset the form (since svelte-modals re-uses the component instances)
      addLendableItemForm.reset();

      // Notify that we were successful
      openModal(
        InfoModal,
        {
          title: "Edit LendableItem",
          message: "Successfully edited lendableItem!",
        },
        { replace: true }
      );
      onChangesSaved(details);
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit LendableItem",
        message: `Could not save details for new lendableItem!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadLendableItemDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={"Add LendableItem "}>
    <ModalBody>
      <AddLendableItemForm
        id="add-lendableItem-form"
        bind:this={addLendableItemForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" type="submit" form="add-lendableItem-form">
        Submit
      </Button>
    </ModalFooter>
  </Modal>
{/if}
