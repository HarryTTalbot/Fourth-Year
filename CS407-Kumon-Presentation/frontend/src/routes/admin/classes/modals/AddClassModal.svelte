<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../../api";
  import { ClassesApi } from "kumon_app_backend_api";

  import InfoModal from "../../../../modals/InfoModal.svelte";
  import ClassForm from "../../forms/ClassForm.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * Callback for when changes were saved for this student.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onClassAdd = async () => {};

  /**
   * The classes API instance currently in use.
   * @type {ClassesApi}
   */
  let classApi = new ClassesApi(API_CONFIG);

  /**
   * The backing element for the "Add Class" form.
   * @type {ClassForm}
   */
  let addClassForm;

  /**
   * Handles submission of the new class details.
   */
  async function handleSubmit(evt) {
    try {
      await classApi.classesCreate({ classRequest: evt.detail });

      openModal(
        InfoModal,
        {
          title: "Add Class",
          message: `Successfully added class!`,
        },
        { replace: true }
      );

      // Clear the "add class" form and refresh the list of classes
      addClassForm.reset();
      await onClassAdd();
    } catch (e) {
      // TODO: Use error modal (once made)
      console.log(e);
      openModal(InfoModal, {
        title: "Add Class",
        message: `Could not add new class!`,
      });
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Add Class`}>
    <ModalBody>
      <ClassForm
        id="add-class-form"
        bind:this={addClassForm}
        on:submit={handleSubmit}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" type="submit" form="add-class-form">
        Add Class
      </Button>
    </ModalFooter>
  </Modal>
{/if}
