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
  } from "sveltestrap";
  import { tick } from "svelte";
  import { push } from "svelte-spa-router";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";

  import API_CONFIG from "../../../api";
  import { LessonApi } from "kumon_app_backend_api";
  import HomeHelp from "./HomeHelp.svelte";

  let lessonApi = new LessonApi(API_CONFIG);

  let lessonsList = [];

  var today = new Date();
  let openHelp = false;

  async function refreshLessons() {
    try {
      lessonsList = await lessonApi.lessonTodayList({});
    } catch (e) {}
  }

  function handleLessonSelect(id) {
    // Go to the page to record the attendance of the lesson
    push("/attendance/lesson/" + id);
  }
</script>

<!-- Content of the page -->
<Container class="p-3">
  <Row>
    <Col>
      <h1>Today's Lessons</h1>
    </Col>

    <Col>
      <Button
        id="helpToday"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpToday" placement="top">
        User Guide for Today's Lessons Manager
      </Tooltip>
    </Col>
  </Row>

  <Table>
    <!-- Absences Table Headings -->
    <thead>
      <tr>
        <th>Start Time</th>
        <th>End Time</th>
        <th>Class</th>
        <th>Subject</th>
        <th>Level</th>
        <th />
      </tr>
    </thead>

    {#await refreshLessons()}
      <!-- Whilst waiting for backend response -->
      <tfoot class="info">
        <tr>
          <td colspan="7">Retrieving list of lessons...</td>
        </tr>
      </tfoot>
    {:then}
      {#if lessonsList.length === 0}
        <!-- If no lessons are returned -->
        <tfoot class="info">
          <tr>
            <td colspan="7"
              >No lesson data found for {today
                .getDate()
                .toString()
                .padStart(2, "0")}/{(today.getMonth() + 1)
                .toString()
                .padStart(2, "0")}/{today.getYear() - 100}</td
            >
            <!-- Year is hard coded for now. Shouldn't be an issue until the year 2100 maybe? -->
          </tr>
        </tfoot>
      {:else}
        <!-- If lessons are returned -->
        <tbody>
          {#each lessonsList as lesson}
            <tr>
              <td>{displayTime(lesson.startDatetime)}</td>
              <!-- Previously duration? -->
              <td>{displayTime(lesson.endDatetime)}</td>
              <td>{lesson.classFk.name}</td>
              <td>{lesson.subject.name}</td>
              <td>{lesson.subjectLevel.name}</td>
              <td
                ><Button
                  color="primary"
                  on:click={() => handleLessonSelect(lesson.id)}
                  >Take Attendance</Button
                ></td
              >
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

  <HomeHelp bind:open={openHelp} />
</Container>
