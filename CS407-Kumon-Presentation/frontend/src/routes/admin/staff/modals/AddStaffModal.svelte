<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../../api";
  import { StaffApi } from "kumon_app_backend_api";

  import InfoModal from "../../../../modals/InfoModal.svelte";
  import NewAccount from "../../../authentication/NewAccount.svelte";
  import StaffForm from "../../forms/StaffForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * Callback for when changes were saved for this student.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onStaffAdd = () => {};

  let staffApi = new StaffApi(API_CONFIG); // Link to the backend api

  let staffForm;

  // Function to create a new staff member
  async function handleCreateStaff(evt) {
    try {
      // Query the backend to create the new staff member
      await staffApi.staffCreate({ staffCreateRequest: evt.detail });

      // Open a modal to confirm the staff member has been added
      openModal(
        InfoModal,
        {
          title: "Add Staff",
          message: "Successfully added new staff member!",
        },
        { replace: true }
      );

      // Clear the "add class" form and refresh the list of classes
      staffForm.reset();
      onStaffAdd();
    } catch (e) {
      // Open a modal to tell them the creation was unsuccessful
      openModal(InfoModal, {
        title: "Add Staff",
        message: e.statusText,
      });
    }
  }

  async function handleCreateAccount(evt) {
    try {
      openModal(NewAccount, {
        onAdd: async (details) => {
          evt.detail.username = details.detail.username;
          await handleCreateStaff(evt);
        },
      });
    } catch (e) {
      // Open a modal to tell them the creation was unsuccessful
      openModal(InfoModal, {
        title: "Add Staff",
        message: e.statusText,
      });
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`New Staff Member`}>
    <ModalBody>
      <StaffForm
        id="add-staff-form"
        bind:this={staffForm}
        on:submit={handleCreateAccount}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" type="submit" form="add-staff-form">Add</Button>
    </ModalFooter>
  </Modal>
{/if}
