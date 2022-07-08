<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Form, Modal, ModalBody, ModalFooter } from "sveltestrap";

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
   * The ID of the student currently being edited.
   * @type {number}
   */
  export let id;

  /**
   * Callback for when changes were saved for this class.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for classes.
   */
  export let onClassEdit = async () => {};

  /**
   * The classes API instance currently in use.
   */
  export let classApi = new ClassesApi(API_CONFIG);

  /**
   * The backing form element for the "Edit Class" form.
   * @type {ClassForm}
   */
  let editClassForm;

  /**
   * Loads the class's current details into this form.
   * @param {number} id The ID of the class.
   */
  async function loadClassDetails(id) {
    try {
      let details = await classApi.classesRetrieve({ id: id });
      editClassForm.setDefaultValues(details);
      editClassForm.reset();
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit Class",
        message: `Could not load details for class ${id}!`,
      });
    }
  }

  /**
   * Handles submission of the new class details.
   */
  async function handleSubmit(evt) {
    try {
      await classApi.classesUpdate({ id: id, classRequest: evt.detail });

      openModal(
        InfoModal,
        {
          title: "Edit Class",
          message: `Successfully edited class ${id}!`,
        },
        { replace: true }
      );

      // Notify that we were successful
      await onClassEdit();
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit Class",
        message: `Could not save new details for class ${id}!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadClassDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Edit Class ${id}...`}>
    <ModalBody>
      <ClassForm
        id="edit-class-form"
        bind:this={editClassForm}
        on:submit={handleSubmit}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="warning" outline on:click={() => editClassForm.reset()}>
        Reset to Original Values
      </Button>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" type="submit" form="edit-class-form">
        Save Changes
      </Button>
    </ModalFooter>
  </Modal>
{/if}
