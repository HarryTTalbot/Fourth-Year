<script>
  import dayjs from "dayjs";
  import { fade } from "svelte/transition";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import {
    Button,
    Container,
    Table,
    Row,
    Col,
    Icon,
    Input,
    Tooltip,
    Card,
    CardHeader,
    CardBody,
  } from "sveltestrap";
  import { tick } from "svelte";

  import API_CONFIG from "../../../api";
  import { LessonApi } from "kumon_app_backend_api";

  import AddressDisplay from "../../../utils/displayAddress.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import EditLessonModal from "./modals/EditLessonModal.svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";
  import { createEventDispatcher } from "svelte";

  let lessonApi = new LessonApi(API_CONFIG);

  const dispatch = createEventDispatcher();

  export let lessonId;

  let lessonInfo;

  /**
   * Refreshes the list of students.
   */
  async function getLessonInfo() {
    try {
      lessonInfo = await lessonApi.lessonRetrieve({ id: lessonId });
    } catch (e) {
      throw e;
    }
  }

  /**
   * Handler for editing a student.
   * @param {number} id The ID of the student.
   */
  async function handleEditLesson() {
    openModal(EditLessonModal, {
      id: lessonId,
      onChangesSaved: async (newDetails) => {
        dispatch("edit", { lessonId: lessonId, newDetails: newDetails });
        await getLessonInfo();
      },
    });
  }

  /**
   * Handler for removing a student.
   * @param {number} id The ID of the student.
   */
  async function handleRemoveLesson() {
    // Query the backend to get the lesson details (as they are in the database)
    let lesson = await lessonApi.lessonRetrieve({ id: lessonId });

    // Formulate a confirmation message to the user
    let lessonMessage =
      displayDate(lesson.startDatetime) +
      " " +
      displayTime(lesson.startDatetime) +
      " " +
      lesson.subject.name +
      " " +
      lesson.classFk.name;

    let confirmationMessage =
      "Are you sure you want to delete this lesson?\n\n" + lessonMessage;

    // Open a confirmation modal to ask the user to confirm the deletion
    openModal(ConfirmationModal, {
      title: "Delete Lesson",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        // If the user confirms the deletion
        try {
          // Query the backend to remove the lesson member (uses Promise API)
          lessonApi.lessonDestroy({ id: lesson.id }).then((_) => {
            // Remove this student from the displayed list
            dispatch("delete", { lessonId: lessonId });

            // NOTE: Second object is needed to "replace" the confirmation modal (otherwise it will re-open)
            openModal(
              InfoModal,
              {
                title: "Delete Lesson",
                message: `Deleted lesson ${lessonMessage}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          // Open a modal to inform the user that the deletion has been unsuccessful
          openModal(
            InfoModal,
            {
              title: "Delete Lesson",
              message: `Could not mark ${lessonMessage}  for deletion!`,
            },
            { replace: true }
          );
        }
      },
    });
  }

  function close() {
    dispatch("close");
  }
</script>

<Card>
  {#await getLessonInfo()}
    <p>Fetching Lesson Data ....</p>
  {:then}
    <CardHeader>
      <Row>
        <Col xs="auto">
          <h3>Lesson Details</h3>
        </Col>
        <Col>
          <Button
            color="danger"
            id="deleteLesson"
            on:click={() => handleRemoveLesson()}
          >
            <Icon name="trash" />
          </Button>
          <Tooltip target="deleteLesson" placement="top">Delete Lesson</Tooltip>
        </Col>
        <Col>
          <Button
            outline
            color="secondary"
            id="closeLesson"
            style="float: right;"
            on:click={() => close()}
          >
            <Icon name="x" />
          </Button>
          <Tooltip target="closeLesson" placement="top">
            Close Lesson Details
          </Tooltip>
        </Col>
      </Row>
    </CardHeader>
    <CardBody>
      <Row>
        <Col xs="auto">
          <h5>Details</h5>
        </Col>
        <Col>
          <Button
            color="primary"
            id="editLesson"
            on:click={() => handleEditLesson()}
          >
            <Icon name="pen" />
          </Button>
          <Tooltip target="editLesson" placement="top">
            Edit Lesson Details
          </Tooltip>
        </Col>
      </Row>

      <p class="spacing">
        <b> Date: </b>
        {displayDate(lessonInfo.startDatetime)} <br />

        <b> Start Time: </b>
        {displayTime(lessonInfo.startDatetime)} <br />

        <b> End Time: </b>
        {displayTime(lessonInfo.endDatetime)} <br />

        <b> Class: </b>
        {lessonInfo.classFk.name} <br />
        <b> Subject: </b>
        {lessonInfo.subject.name} <br />

        <b> Subject Level: </b>
        {lessonInfo.subjectLevel.name} <br />
      </p>
    </CardBody>
  {/await}
</Card>

<style>
  p.spacing {
    line-height: 1.5;
  }
</style>
