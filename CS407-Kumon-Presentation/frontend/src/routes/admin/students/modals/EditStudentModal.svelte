<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import InfoModal from "../../../../modals/InfoModal.svelte";
  import StudentForm from "../../forms/StudentForm.svelte";

  import API_CONFIG from "../../../../api";
  import { StudentsApi } from "kumon_app_backend_api";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * The ID of the student currently being edited.
   * @type {number}
   */
  export let id;

  /**
   * Callback for when changes were saved for this student.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onChangesSaved = (newDetails) => {};

  /**
   * The backing element for the displayed form.
   * @type {StudentForm}
   */
  let editStudentForm;

  let studentsApi = new StudentsApi(API_CONFIG);

  /**
   * Loads the student's current details into this form.
   * @param {number} id The ID of the student.
   */
  async function loadStudentDetails(id) {
    try {
      let details = await studentsApi.studentsRetrieve({ id: id });
      editStudentForm.setDefaultValues(details);
      resetFields();
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit Student",
        message: `Could not load details for student ${id}!`,
      });
    }
  }

  /**
   * Resets the fields to their original values.
   */
  function resetFields() {
    editStudentForm.reset();
  }

  /**
   * Handles submission of the new student details.
   */
  async function handleSubmit(e) {
    try {
      await studentsApi.studentsUpdate({ id: id, studentRequest: e.detail });

      // Notify that we were successful
      onChangesSaved(e.detail);

      closeModal();
      openModal(InfoModal, {
        title: "Edit Student",
        message: `Successfully edited student ${id}!`,
      });
    } catch (e) {
      // TODO: Use error modal (once made)
      openModal(InfoModal, {
        title: "Edit Student",
        message: `Could not save new details for student ${id}!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadStudentDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Edit Student ${id}...`}>
    <ModalBody>
      <StudentForm
        id="edit-student-form"
        bind:this={editStudentForm}
        on:submit={handleSubmit}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="warning" outline on:click={resetFields}>
        Reset to Original Values
      </Button>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="edit-student-form" type="submit">
        Save Changes
      </Button>
    </ModalFooter>
  </Modal>
{/if}
