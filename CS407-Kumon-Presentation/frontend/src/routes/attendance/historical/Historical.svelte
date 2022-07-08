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
    Tooltip,
    Icon,
    Card,
    CardHeader,
    CardBody,
  } from "sveltestrap";
  import { tick } from "svelte";
  import { push } from "svelte-spa-router";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";

  import API_CONFIG from "../../../api";
  import { LessonApi } from "kumon_app_backend_api";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../../components/PaginationFilteringBar.svelte";
  import HistoricalHelp from "./HistoricalHelp.svelte";

  let lessonApi = new LessonApi(API_CONFIG);

  let lessonsList = [];
  let currentID = null;

  var today = new Date();

  let view = false;
  let openHelp = false;

  let pageFilterDetails = new PageFilter();

  let currentPresent = 0;
  let currentAbsent = 0;

  async function refreshHistory() {
    try {
      let response = await lessonApi.lessonPastList({
        page: pageFilterDetails.page,
        search: pageFilterDetails.filter,
      });
      lessonsList = response.results;

      pageFilterDetails.pageUpdate(response);
      pageFilterDetails.filter += " ";
      pageFilterDetails.filter = pageFilterDetails.filter.substring(
        0,
        pageFilterDetails.filter.length - 1
      );
    } catch (e) {}
  }

  let currentLesson = null;

  async function handleView(id) {
    // Open the current lesson being viewed
    if (view == true) {
      view = false;
      currentID = null;
      return;
    }
    view = true;
    currentID = id;

    // Find the current lesson by iterating through all lessons until you find a match for the lesson's ID
    for (let i = 0; i < lessonsList.length; i++) {
      if (lessonsList[i].id === currentID) {
        currentLesson = lessonsList[i];
        break;
      }
    }

    // Obtain list of students in the lesson
    let lessonStudents = await lessonApi.lessonGetAttendanceList({ id: id });

    currentPresent = 0;
    currentAbsent = 0;

    // Count how many students are present. Store that number in the currentPresent variable, and the count of everyone else in the currentAbsent variable
    if (lessonStudents.length > 0) {
      for (const entry of lessonStudents) {
        if (entry.status === "P") {
          currentPresent++;
        } else {
          currentAbsent++;
        }
      }
    }
  }

  function handleViewAttendance() {
    // Open the lesson attendance page for the lesson selected
    push("/attendance/lesson/" + currentID);
  }

  function handleCancel() {
    // Close the current lesson being viewed
    view = false;
    currentID = null;
  }
</script>

<!-- Content of the page -->
<Container class="p-3">
  <Row>
    <Col>
      <h1>Past Attendance Records</h1>
    </Col>

    <Col>
      <Button
        id="helpHistorical"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpHistorical" placement="top">
        User Guide for Past Attendance Manager
      </Tooltip>
    </Col>
  </Row>

  <div>
    <PaginationFilteringBar
      refresh={() => refreshHistory()}
      pageFilter={pageFilterDetails}
    />
    <Table>
      <!-- History Table Headings -->
      <thead>
        <tr>
          <th style="width: 15%">Date</th>
          <th style="width: 8%">Start Time</th>
          <th style="width: 8%">End Time</th>
          <th style="width: 14%">Class</th>
          <th style="width: 20%">Subject</th>
          <th style="width: 5%">Level</th>
          <th style="width: 15%">Attendance Recorded</th>
          <th style="width: 15%">Attendance Modified</th>
        </tr>
      </thead>

      {#await refreshHistory()}
        <!-- Whilst waiting for backend response -->
        <tfoot class="info">
          <tr>
            <td colspan="6">Retrieving list of lessons...</td>
          </tr>
        </tfoot>
      {:then}
        {#if lessonsList.length === 0}
          <!-- If no lessons are returned -->
          <tfoot class="info">
            <tr>
              <td colspan="9">No past lesson data found</td>
            </tr>
          </tfoot>
        {:else}
          <!-- If lessons are returned -->
          <tbody>
            {#each lessonsList as lesson}
              <tr
                class:selected={currentID === lesson.id}
                on:click={() => handleView(lesson.id)}
              >
                <td>{displayDate(lesson.startDatetime)}</td>
                <td>{displayTime(lesson.startDatetime)}</td>
                <!-- Previously duration? -->
                <td>{displayTime(lesson.endDatetime)}</td>
                <td>{lesson.classFk.name}</td>
                <td>{lesson.subject.name}</td>
                <td>{lesson.subjectLevel.name}</td>
                <td
                  >{displayDate(lesson.createdAt)}
                  {displayTime(lesson.createdAt)}</td
                >
                <td
                  >{displayDate(lesson.lastModifiedAt)}
                  {displayTime(lesson.lastModifiedAt)}</td
                >
              </tr>
            {/each}
          </tbody>
        {/if}
      {:catch}
        <!-- If an error is returned -->
        <tfoot class="info">
          <tr>
            <td colspan="9">Could not retrieve list of lessons!</td>
          </tr>
        </tfoot>
      {/await}
    </Table>
  </div>

  {#if view === true}
    <Card>
      <CardHeader>
        <Row>
          <Col>
            <h2>Attendance Information</h2>
          </Col>

          <Col>
            <Button
              id="closeView"
              outline
              color="secondary"
              style="float: right;"
              on:click={handleCancel}
            >
              <Icon name="x" />
            </Button>
            <Tooltip target="closeView" placement="top">Close View</Tooltip>
          </Col>
        </Row>
      </CardHeader>

      <CardBody>
        <h5>
          {displayDate(currentLesson.startDatetime)}
          {displayTime(currentLesson.startDatetime)} - {displayTime(
            currentLesson.endDatetime
          )}
        </h5>
        <h5>
          {currentLesson.classFk.name}, {currentLesson.subject.name} - {currentLesson
            .subjectLevel.name}
        </h5>
        <p>{currentPresent} students present</p>
        <p>{currentAbsent} students absent</p>
        <p>
          Last Modified at: {displayDate(currentLesson.lastModifiedAt)}
          {displayTime(currentLesson.lastModifiedAt)}
        </p>
        <Button color="primary" on:click={handleViewAttendance}
          >View Attendance</Button
        >
      </CardBody>
    </Card>
  {/if}

  <HistoricalHelp bind:open={openHelp} />
</Container>

<style>
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
