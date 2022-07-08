<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import InfoModal from "../../../../modals/InfoModal.svelte";
  import AbsenceForm from "../../forms/LongTermForm.svelte";

  import API_CONFIG from "../../../../api";
  import { LongTermAbsenceApi } from "kumon_app_backend_api";

  import { displayDate, displayTime } from "../../../../utils/displayDateTime";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  export let id;

  /**
   * Callback for when changes were saved for this student.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onChangesSaved = async (newDetails) => {};

  let editLongTermForm;

  let absenceApi = new LongTermAbsenceApi(API_CONFIG);

  async function loadAbsenceDetails(id) {
    try {
      let details = await absenceApi.longTermAbsenceRetrieve({ id: id });

      details.studentDetails = details.student;
      details.student = details.student.id;
      if (details.reason.startsWith("Other")) {
        details.otherDetail = details.reason.substring(
          7,
          details.reason.length - 1
        );
        details.reason = "Other";
      }

      editLongTermForm.setDefaultValues(details);

      resetFields();
    } catch (e) {
      openModal(InfoModal, {
        title: "Update Long Term Absence",
        message: `Could not load details for Long Term Absence ${id}!`,
      });
    }
  }

  /**
   * Resets the fields to their original values.
   */
  function resetFields() {
    editLongTermForm.reset();
  }

  /**
   * Handles submission of the new student details.
   */
  async function handleSubmit(evt) {
    let parameters = evt.detail;
    // If the reason is other, update the reason
    if (parameters.reason == "Other") {
      parameters.reason += " (" + parameters.otherDetail + ")";
    }

    try {
      // Query the backend to update the details
      await absenceApi.longTermAbsenceUpdate({
        id: evt.detail.id,
        longTermAbsenceEditRequest: parameters,
      });

      // Notify that we were successful
      onChangesSaved(parameters);

      closeModal();
      // Open a modal to say the operation was successfull
      openModal(InfoModal, {
        title: "Update Long Term Absence",
        message: "Successfully updated the long term absence!",
      });
    } catch (e) {
      // Open a modal to tell them the update was unsuccessful
      openModal(InfoModal, {
        title: "Update Long Term Absence",
        message: "Unable to update long term absence!",
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadAbsenceDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Edit Long Term Absence ${id}...`}>
    <ModalBody>
      <AbsenceForm
        id="edit-long-term-form"
        bind:this={editLongTermForm}
        on:submit={handleSubmit}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="warning" outline on:click={resetFields}>
        Reset to Original Values
      </Button>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="edit-long-term-form" type="submit">
        Save Changes
      </Button>
    </ModalFooter>
  </Modal>
{/if}
