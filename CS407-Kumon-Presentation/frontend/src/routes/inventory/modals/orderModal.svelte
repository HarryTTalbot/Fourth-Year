<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../api";
  import { WorksheetApi } from "kumon_app_backend_api";

  import InfoModal from "./InfoModal.svelte";
  import OrderForm from "../forms/OrderForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * The ID of the worksheet currently being "ordered".
   * @type {number}
   */
  export let id;

  /**
   * Callback for when changes were saved for this student.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onChangesSaved = (newDetails) => {};

  /**
   * The classes API instance currently in use.
   * @type {ClassesApi}
   */
  let WorksheetLogApi = new WorksheetApi(API_CONFIG);

  /**
   * The backing element for the "Add Class" form.
   * @type {ClassForm}
   */
  let orderForm;

  /**
   * Handles submission of the new class details.
   */
  async function handleSubmit(evt) {
    try {
      if (evt.type == "Withdrawal") {
        await WorksheetLogApi.worksheetWithdrawCreate({
          itemWithdrawRequest: evt,
          id: id,
        });
      } else if (evt.type == "Restock") {
        await WorksheetLogApi.worksheetRestockCreate({
          itemRestockRequest: evt,
          id: id,
        });
      }
      openModal(
        InfoModal,
        {
          title: "Worksheet " + evt.type,
          message: `Successfully created a new worksheet log!`,
        },
        { replace: true }
      );

      onChangesSaved(evt);
    } catch (e) {
      openModal(InfoModal, {
        title: "Worksheet " + evt.type,
        message: `Could not created a new worksheet log!`,
      });
    }
  }

  /**
   * Resets the fields to their original values.
   */
  function resetFields() {
    orderForm.reset();
  }

  async function loadWorksheetDetails(id) {
    try {
      let details = await WorksheetLogApi.worksheetRetrieve({ id: id });
      details.type = "Withdrawal";
      orderForm.setDefaultValues(details);
      resetFields();
    } catch (e) {
      openModal(InfoModal, {
        title: "Order",
        message: `Could not load details for worksheet ${id}!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadWorksheetDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={"Order "}>
    <ModalBody>
      <OrderForm
        id="add-worksheet-log-form"
        bind:this={orderForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" type="submit" form="add-worksheet-log-form">
        Make Order
      </Button>
    </ModalFooter>
  </Modal>
{/if}
