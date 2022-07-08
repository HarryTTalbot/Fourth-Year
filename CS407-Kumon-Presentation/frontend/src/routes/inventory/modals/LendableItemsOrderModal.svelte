<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../api";
  import { LendableItemApi } from "kumon_app_backend_api";
  import { ItemLoanApi } from "kumon_app_backend_api";

  import InfoModal from "./InfoModal.svelte";
  import LendForm from "../forms/LendForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * The ID of the lendableItem currently being "ordered".
   * @type {number}
   */
  export let id;

  /**
   * Callback for when changes were saved for this item order.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for orders.
   */
  export let onAdd = async (newDetails) => {};

  /**
   * The lendable item API instance currently in use.
   * @type {LendableItemApi}
   */
  let LendableItemLogApi = new LendableItemApi(API_CONFIG);
  /**
   * The item loan API instance currently in use.
   * @type {ItemLoanApi}
   */
  let itemLoanApi = new ItemLoanApi(API_CONFIG);

  /**
   * The backing element for the "Add Class" form.
   * @type {lendForm}
   */
  let lendForm;

  /**
   * Handles submission of the new class details.
   */
  async function handleSubmit(evt) {
    try {
      evt.itemId = id;
      await itemLoanApi.itemLoanCreate({ itemLoanRequest: evt, id: id });

      openModal(
        InfoModal,
        {
          title: "LendableItem " + evt.type,
          message: `Successfully created a new lendableItem log!`,
        },
        { replace: true }
      );

      onAdd(evt);
      lendForm.reset();
    } catch (e) {
      openModal(InfoModal, {
        title: "LendableItem " + evt.type,
        message: `Could not creat a new lendableItem log!`,
      });
    }
  }

  /**
   * Resets the fields to their original values.
   */
  function resetFields() {
    lendForm.reset();
  }

  /**
   * Handler for editing a lendable item
   * @param {number} id The ID of the lendable item.
   */
  async function loadLendableItemDetails(id) {
    try {
      let details = await LendableItemLogApi.lendableItemRetrieve({ id: id });
      details.type = "Withdrawal";
      lendForm.setDefaultValues(details);
      resetFields();
    } catch (e) {
      openModal(InfoModal, {
        title: "Order",
        message: `Could not load details for lendableItem ${id}!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadLendableItemDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={"Order "}>
    <ModalBody>
      <LendForm
        id="add-lendableItem-log-form"
        bind:this={lendForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" type="submit" form="add-lendableItem-log-form">
        Make Order
      </Button>
    </ModalFooter>
  </Modal>
{/if}
