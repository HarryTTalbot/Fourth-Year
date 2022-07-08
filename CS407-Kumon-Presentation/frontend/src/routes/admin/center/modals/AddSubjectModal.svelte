<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../../api";
  import { SubjectApi } from "kumon_app_backend_api";

  import InfoModal from "../../../../modals/InfoModal.svelte";
  import NewAccount from "../../../authentication/NewAccount.svelte";
  import SubjectForm from "../../forms/SubjectForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * Callback for when changes were saved for this student.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onSubjectAdd = () => {};

  // Link to the backend api
  let subjectApi = new SubjectApi(API_CONFIG);

  // Form object
  let subjectForm;

  // Function to create a new staff member
  async function handleCreateSubject(evt) {
    try {
      // Query the backend to create the new subject
      await subjectApi.subjectCreate({ subjectRequest: evt.detail });

      // Clear the "add class" form and refresh the list of classes
      subjectForm.reset();
      onSubjectAdd();
      closeModal();

      // Open a modal to confirm the subject has been added
      openModal(InfoModal, {
        title: "Add Subject",
        message: "Successfully added new Subject!",
      });
    } catch (e) {
      // Open a modal to tell them the creation was unsuccessful
      openModal(InfoModal, {
        title: "Add Subject",
        message: e.statusText,
      });
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`New Subject`}>
    <ModalBody>
      <SubjectForm
        id="add-subject-form"
        bind:this={subjectForm}
        on:submit={handleCreateSubject}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" type="submit" form="add-subject-form">Add</Button>
    </ModalFooter>
  </Modal>
{/if}
