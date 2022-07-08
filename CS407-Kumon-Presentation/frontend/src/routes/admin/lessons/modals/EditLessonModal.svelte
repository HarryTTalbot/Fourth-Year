<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import InfoModal from "../../../../modals/InfoModal.svelte";
  import LessonForm from "../../forms/LessonForm.svelte";

  import API_CONFIG from "../../../../api";
  import { LessonApi } from "kumon_app_backend_api";

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

  let editLessonForm;

  let lessonApi = new LessonApi(API_CONFIG);

  // Function to combine a day and time into single Date object
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

  async function loadLessonDetails(id) {
    try {
      let details = await lessonApi.lessonRetrieve({ id: id });

      details.starttime = displayTime(details.startDatetime);
      details.endtime = displayTime(details.endDatetime);
      details.classFk = details.classFk.id;
      details.subject = details.subject.id;
      details.subjectLevel = details.subjectLevel.id;

      editLessonForm.setDefaultValues(details);

      resetFields();
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit Lesson",
        message: `Could not load details for lesson ${id}!`,
      });
    }
  }

  /**
   * Resets the fields to their original values.
   */
  function resetFields() {
    editLessonForm.reset();
  }

  /**
   * Handles submission of the new student details.
   */
  async function handleSubmit(e) {
    let details = convertFormToAPI(e.detail);

    try {
      // Query the backend to update the details
      await lessonApi.lessonUpdate({
        id: e.detail.id,
        lessonEditRequest: details,
      });

      // Notify that we were successful
      onChangesSaved(details);

      closeModal();
      // Open a modal to say the operation was successfull
      openModal(InfoModal, {
        title: "Update Lesson",
        message: "Successfully updated the lesson!",
      });
    } catch (e) {
      // Open a modal to tell them the update was unsuccessful
      openModal(InfoModal, {
        title: "Update Lesson",
        message: "Unable to update lesson!",
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadLessonDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Edit Lesson ${id}...`}>
    <ModalBody>
      <LessonForm
        id="edit-lesson-form"
        bind:this={editLessonForm}
        on:submit={handleSubmit}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="warning" outline on:click={resetFields}>
        Reset to Original Values
      </Button>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="edit-lesson-form" type="submit">
        Save Changes
      </Button>
    </ModalFooter>
  </Modal>
{/if}
