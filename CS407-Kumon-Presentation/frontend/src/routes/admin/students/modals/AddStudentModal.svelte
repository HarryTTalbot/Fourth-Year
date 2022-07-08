<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../../api";
  import { StudentsApi } from "kumon_app_backend_api";

  import InfoModal from "./../../../../modals/InfoModal.svelte";
  import StudentForm from "../../forms/StudentForm.svelte";

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
  export let studentsApi = new StudentsApi(API_CONFIG);

  /**
   * The backing form component for the "Add Student" form.
   * @type {StudentForm}
   */
  let addStudentForm;

  /**
   * Handles submission of the new student details.
   * @type {details} matches the API endpoint
   */
  async function handleSubmit(details) {
    try {
      await studentsApi.studentsCreate({ studentRequest: details });

      // Reset the form (since svelte-modals re-uses the component instances)
      addStudentForm.reset();

      // Notify that we were successful
      openModal(
        InfoModal,
        {
          title: "Add Student",
          message: "Successfully added student!",
        },
        { replace: true }
      );

      onAdd(details);
    } catch (e) {
      // TODO: Use error modal (once made)
      openModal(InfoModal, {
        title: "Add Student",
        message: `Could not save details for new student!`,
      });
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Add Student`}>
    <ModalBody>
      <StudentForm
        id="add-student-form"
        bind:this={addStudentForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="add-student-form" type="submit">Add</Button>
    </ModalFooter>
  </Modal>
{/if}
