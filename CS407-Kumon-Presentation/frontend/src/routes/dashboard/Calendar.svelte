<script>
  import { displayDate, displayTime } from "../../utils/displayDateTime";
  import {
    Button,
    Container,
    Table,
    Input,
    Label,
    Row,
    Col,
    Card,
  } from "sveltestrap";
  import { tick } from "svelte";
  import { push } from "svelte-spa-router";
  import API_CONFIG from "../../api";
  import { LessonApi } from "kumon_app_backend_api";

  // Link to backend api
  let lessonApi = new LessonApi(API_CONFIG);

  // List of lessons in the current day
  let lessonsList = [];

  // Function to get a list of today's lessons
  async function refreshLessons() {
    // Query the backend api
    lessonsList = await lessonApi.lessonTodayList({});
  }
</script>

<Card body class="p-3 h-100">
  <h2>Today's Lessons</h2>
  {#await refreshLessons()}
    <p>Fetching today's lessons...</p>
  {:then}
    {#if lessonsList.length == 0}
      <p>There are no lessons today</p>
    {:else}
      <Table class="table table-sm">
        <!-- Absences Table Headings -->
        <thead>
          <tr>
            <th>Start Time</th>
            <th>End Time</th>
            <th>Class</th>
            <th>Subject</th>
            <th>Level</th>
          </tr>
        </thead>

        <tbody>
          {#each lessonsList as lesson}
            <tr>
              <td>{displayTime(lesson.startDatetime)}</td>
              <td>{displayTime(lesson.endDatetime)}</td>
              <td>{lesson.classFk.name}</td>
              <td>{lesson.subject.name}</td>
              <td>{lesson.subjectLevel.name}</td>
            </tr>
          {/each}
        </tbody>
      </Table>
    {/if}
  {:catch}
    <p>Could not get today's lessons...</p>
  {/await}
</Card>
