<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../api";
  import { BulkItemApi } from "kumon_app_backend_api";

  import InfoModal from "./InfoModal.svelte";
  import OrderForm from "../forms/OrderForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * The ID of the bulkItem currently being "ordered".
   * @type {number}
   */
  export let id;

  /**
   * Callback for when changes were saved for this bulk item.
   */
  export let onChangesSaved = (newDetails) => {};

  /**
   * The bulk items API instance currently in use.
   * @type {BulkItemApi}
   */
  let BulkItemLogApi = new BulkItemApi(API_CONFIG);

  /**
   * The backing element for the "order" form.
   * @type {orderForm}
   */
  let orderForm;

  /**
   * Handles submission of the order.
   * @param evt The new details that were chosen. Matches the API endpoint's format for bulk items.
   */
  async function handleSubmit(evt) {
    try {
      // Changes which API function to call depending on value in the form
      if (evt.type == "Withdrawal") {
        await BulkItemLogApi.bulkItemWithdrawCreate({
          itemWithdrawRequest: evt,
          id: id,
        });
      } else if (evt.type == "Restock") {
        await BulkItemLogApi.bulkItemRestockCreate({
          itemRestockRequest: evt,
          id: id,
        });
      }
      openModal(
        InfoModal,
        {
          title: "BulkItem " + evt.type,
          message: `Successfully created a new bulkItem log!`,
        },
        { replace: true }
      );

      onChangesSaved(evt);

      // Clear the form and refresh the list of bulk items
      orderForm.reset();
    } catch (e) {
      openModal(InfoModal, {
        title: "BulkItem " + evt.type,
        message: `Could not created a new bulkItem log!`,
      });
    }
  }

  /**
   * Resets the fields to their original values.
   */
  function resetFields() {
    orderForm.reset();
  }

  /**
   * Handler for editing a bulk item
   * @param {number} id The ID of the bulk item.
   */
  async function loadBulkItemDetails(id) {
    try {
      let details = await BulkItemLogApi.bulkItemRetrieve({ id: id });
      // Must be manually specified, otherwise the default values will not be present in the form
      details.type = "Withdrawal";
      orderForm.setDefaultValues(details);
      resetFields();
    } catch (e) {
      openModal(InfoModal, {
        title: "Order",
        message: `Could not load details for bulkItem ${id}!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadBulkItemDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={"Order "}>
    <ModalBody>
      <OrderForm
        id="add-bulkItem-log-form"
        bind:this={orderForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" type="submit" form="add-bulkItem-log-form">
        Make Order
      </Button>
    </ModalFooter>
  </Modal>
{/if}
