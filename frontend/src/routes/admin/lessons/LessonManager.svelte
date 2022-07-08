<script>
  import { fade } from "svelte/transition";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import {
    Button,
    Container,
    Table,
    Input,
    Label,
    Row,
    Col,
    Icon,
    Tooltip,
  } from "sveltestrap";
  import { tick } from "svelte";

  import API_CONFIG from "../../../api";
  import { LessonApi } from "kumon_app_backend_api";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../../components/PaginationFilteringBar.svelte";

  import LessonForm from "../forms/LessonForm.svelte";

  import { displayDate, displayTime } from "../../../utils/displayDateTime";

  import InfoModal from "../../../modals/InfoModal.svelte";
  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import AddLessonModal from "./modals/AddLessonModal.svelte";

  import LessonDetails from "./LessonDetails.svelte";
  import LessonHelp from "./LessonHelp.svelte";

  // Variables needed in the page
  let lessonApi = new LessonApi(API_CONFIG); // Link to the backend api
  let lessonList = []; // List of lesson currently on display
  let currentID; // The current lesson member being viewed
  let openHelp = false;

  let pageFilterDetails = new PageFilter();

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

  // Function to refresh the list of lessons
  async function refreshLessons() {
    try {
      // Query the Backend with the page and search filter
      let response = await lessonApi.lessonList({
        page: pageFilterDetails.page,
        search: pageFilterDetails.filter,
      });

      // Save the list of lesson and the total number of lesson
      lessonList = response.results;

      pageFilterDetails.pageUpdate(response);
      pageFilterDetails.filter += " ";
      pageFilterDetails.filter = pageFilterDetails.filter.substring(
        0,
        pageFilterDetails.filter.length - 1
      );
    } catch (e) {
      // If there is an error throw an exception
      //throw e;
    }
  }

  // Function to open the details of a lesson member
  async function handleViewLesson(id) {
    if (currentID === id) {
      currentID = undefined;
    } else {
      currentID = undefined;
      await tick();
      currentID = id;
    }
  }

  // Function to open the create new lesson form
  async function openCreateForm() {
    openModal(AddLessonModal, {
      onAdd: async (_) => {
        await refreshLessons();
      },
    });
  }

  async function handleEdit(event) {
    await refreshLessons();
    await tick();
  }

  async function handleDelete(event) {
    currentID = undefined;
    await refreshLessons();
    await tick();
  }

  async function handleCloseView() {
    currentID = undefined;
    await tick();
  }
</script>

<!-- Content of the page -->
<Container class="p-3">
  <Row>
    <Col>
      <h1>Lesson Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpLesson"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpLesson" placement="top">
        User Guide for Lesson Manager
      </Tooltip>
    </Col>
  </Row>
  <Row>
    <Col>
      <h2>Lesson List</h2>
    </Col>

    <Col>
      <Button
        id="addLesson"
        color="success"
        style="float: right;"
        on:click={() => openCreateForm()}
      >
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addLesson" placement="top">Add a New Lesson</Tooltip>
    </Col>
  </Row>

  <!-- List of all lesson component of the page -->
  <PaginationFilteringBar
    refresh={() => refreshLessons()}
    pageFilter={pageFilterDetails}
  />

  <Table>
    <!-- Lesson Table Headings -->
    <thead>
      <tr>
        <th style="width: 20%">Date</th>
        <th style="width: 10%">Start</th>
        <th style="width: 10%">End</th>
        <th style="width: 15%">Class</th>
        <th style="width: 25%">Subject</th>
        <th style="width: 20%">Subject Level</th>
      </tr>
    </thead>

    {#await refreshLessons()}
      <!-- Whilst waiting for backend response -->
      <tfoot class="info">
        <tr>
          <td colspan="6">Retrieving list of lessons...</td>
        </tr>
      </tfoot>
    {:then}
      {#if lessonList.length === 0}
        <!-- If no lesson are returned -->
        <tfoot class="info">
          <tr>
            <td colspan="6">No lesson data found</td>
          </tr>
        </tfoot>
      {:else}
        <!-- If lesson are returned -->
        <tbody>
          {#each lessonList as lesson}
            <tr
              class:selected={currentID === lesson.id}
              on:click={() => handleViewLesson(lesson.id)}
            >
              <td>{displayDate(lesson.startDatetime)}</td>
              <td>{displayTime(lesson.startDatetime)}</td>
              <td>{displayTime(lesson.endDatetime)}</td>
              <td>{lesson.classFk.name}</td>
              <td>{lesson.subject.name}</td>
              <td>{lesson.subjectLevel.name}</td>
            </tr>
          {/each}
        </tbody>
      {/if}
    {:catch}
      <!-- If an error is returned -->
      <tfoot class="info">
        <tr>
          <td colspan="6">Could not retrieve list of lessons!</td>
        </tr>
      </tfoot>
    {/await}
  </Table>

  {#if currentID}
    <LessonDetails
      lessonId={currentID}
      on:edit={handleEdit}
      on:delete={handleDelete}
      on:close={handleCloseView}
    />
  {/if}

  <LessonHelp bind:open={openHelp} />
</Container>

<style>
  /* Centre any footers displaying information */
  tfoot.info > tr > td {
    text-align: center;
  }
  .selected {
    background-color: #6c757d;
    color: white;
  }
  tbody tr:hover {
    background-color: #6c757d;
    color: white;
  }
</style>
