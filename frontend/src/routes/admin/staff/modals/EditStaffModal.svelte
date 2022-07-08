<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../../api";
  import { StaffApi } from "kumon_app_backend_api";

  import InfoModal from "../../../../modals/InfoModal.svelte";
  import StaffForm from "../../forms/StaffForm.svelte";

  export let id;

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * Callback for when changes were saved for this student.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onStaffEdit = (newDetails) => {};

  let staffApi = new StaffApi(API_CONFIG); // Link to the backend api

  let staffForm;

  async function loadStaffDetails(id) {
    try {
      let details = await staffApi.staffRetrieve({ id: id });
      staffForm.setDefaultValues(details);
      staffForm.reset();
    } catch (e) {
      // TODO: Use error modal (once made)
      openModal(InfoModal, {
        title: "Edit Staff",
        message: `Could not load details for staff ${id}!`,
      });
    }
  }

  // Function to create a new staff member
  async function handleEditStaff(evt) {
    try {
      // Query the backend to update the details
      await staffApi.staffUpdate({
        id: evt.detail.id,
        staffRequest: evt.detail,
      });
      // Notify that we were successful
      onStaffEdit(evt.detail);

      closeModal();
      // Open a modal to say the operation was successfull
      openModal(InfoModal, {
        title: "Update Staff",
        message: "Successfully updated the staff member!",
      });
    } catch (e) {
      // Open a modal to tell them the update was unsuccessful
      openModal(InfoModal, {
        title: "Update Staff",
        message: "Unable to update staff!",
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadStaffDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`New Staff Member`}>
    <ModalBody>
      <StaffForm
        id="edit-staff-form"
        bind:this={staffForm}
        on:submit={handleEditStaff}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="warning" outline on:click={() => staffForm.reset()}>
        Reset to Original Values
      </Button>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" type="submit" form="edit-staff-form">
        Save Changes
      </Button>
    </ModalFooter>
  </Modal>
{/if}
