<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../../api";
  import { LongTermAbsenceApi } from "kumon_app_backend_api";

  import InfoModal from "./../../../../modals/InfoModal.svelte";
  import AbsenceForm from "../../forms/LongTermForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * Callback for when a new student is added.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onAdd = (newDetails) => {};

  /**
   * The students API instance in use.
   * @type {StudentsApi}
   */
  let absenceApi = new LongTermAbsenceApi(API_CONFIG);

  let addLongTermForm;

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
      // Query the backend to create the new lesson member
      await absenceApi.longTermAbsenceCreate({
        longTermAbsenceEditRequest: parameters,
      });

      // Reset the form (since svelte-modals re-uses the component instances)
      addLongTermForm.reset();

      closeModal();

      // Notify that we were successful
      openModal(InfoModal, {
        title: "Add Long Term Absence",
        message: "Successfully added new long term absence!",
      });

      onAdd(parameters);
    } catch (e) {
      openModal(InfoModal, {
        title: "Add Long Term Absence",
        message: e.statusText,
      });
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Add Long Term Absence`}>
    <ModalBody>
      <AbsenceForm
        id="add-long-term-form"
        bind:this={addLongTermForm}
        on:submit={async (e) => handleSubmit(e)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="add-long-term-form" type="submit">
        Add Long Term Absence
      </Button>
    </ModalFooter>
  </Modal>
{/if}
