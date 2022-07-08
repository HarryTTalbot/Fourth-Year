<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../../api";
  import { LessonApi } from "kumon_app_backend_api";

  import InfoModal from "./../../../../modals/InfoModal.svelte";
  import LessonForm from "../../forms/LessonForm.svelte";

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
  let lessonApi = new LessonApi(API_CONFIG);

  let addLessonForm;

  function combineDateTime(date, time) {
    let newDate = new Date();
    newDate.setDate(date.getDate());
    newDate.setMonth(date.getMonth());
    newDate.setFullYear(date.getFullYear());
    newDate.setHours(time.substring(0, 2));
    newDate.setMinutes(time.substring(3, 5));
    newDate.setSeconds(0);
    return newDate;
  }

  function convertFormToAPI(formEvent) {
    let api = {
      startDatetime: combineDateTime(
        formEvent.startDatetime,
        formEvent.starttime
      ),
    };
    api.endDatetime = combineDateTime(
      formEvent.startDatetime,
      formEvent.endtime
    );
    api.classFk = formEvent.classFk;
    api.subjectLevel = formEvent.subjectLevel;

    return api;
  }

  /**
   * Handles submission of the new student details.
   */
  async function handleSubmit(evt) {
    let details = convertFormToAPI(evt.detail);

    try {
      // Query the backend to create the new lesson member
      await lessonApi.lessonCreate({ lessonEditRequest: details });

      // Reset the form (since svelte-modals re-uses the component instances)
      addLessonForm.reset();

      closeModal();

      // Notify that we were successful
      openModal(InfoModal, {
        title: "Add Lesson",
        message: "Successfully added new Lesson!",
      });

      onAdd(details);
    } catch (e) {
      // TODO: Use error modal (once made)
      openModal(InfoModal, {
        title: "Add Lesson",
        message: e.statusText,
      });
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Add Lesson`}>
    <ModalBody>
      <LessonForm
        id="add-lesson-form"
        bind:this={addLessonForm}
        on:submit={async (e) => handleSubmit(e)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="add-lesson-form" type="submit">
        Add Lesson
      </Button>
    </ModalFooter>
  </Modal>
{/if}
