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

  /**
   * Callback for when a new lendable item is added.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for lendable items.
   */
  export let onAdd = async (newDetails) => {};

  /**
   * The backing form component for the "Add Lendable Item" form.
   * @type {addLendableItemForm}
   */
  let addLendableItemForm;

  let lendableItemApi = new LendableItemApi(API_CONFIG);

  /**
   * Handles submission of the new lendable item details.
   * @param details The new details that were chosen. Matches the API endpoint's format for lendable items.
   */
  async function handleSubmit(details) {
    try {
      await lendableItemApi.lendableItemCreate({
        lendableItemEditRequest: details,
      });

      // Reset the form (since svelte-modals re-uses the component instances)
      addLendableItemForm.reset();

      // Notify that we were successful
      openModal(
        InfoModal,
        {
          title: "Add Lendable Item",
          message: "Successfully added lendable item!",
        },
        { replace: true }
      );
      onAdd(details);
    } catch (e) {
      openModal(InfoModal, {
        title: "Add Lendable Item",
        message: `Could not save details for new lendable item!`,
      });
    }
  }
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
