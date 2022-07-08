<script>
  import { Container, Button, Card } from "sveltestrap";
  import { push } from "svelte-spa-router";
  import { displayDate, displayTime } from "../../utils/displayDateTime";

  import API_CONFIG from "../../api";
  import { LessonApi } from "kumon_app_backend_api";

  // Link to backend api
  let lessonApi = new LessonApi(API_CONFIG);

  // Number of lessons in the current day
  let no_lessons = 0;

  // Object containing the information on the current lesson, if there is none it remains null
  let current_lesson = null;

  // Object containing the information on the next lesson, if there is none it remains null
  let next_lesson = null;

  // Method to get the details of the lessons in the current day
  async function getDetails() {
    // Query the backend api
    let response = await lessonApi.lessonTodayList({});

    // Get the number of lessons
    no_lessons = response.length;

    // If there are no lessons, return
    if (no_lessons == 0) {
      return true;
    }

    // If there are lessons, find the current one (if any) and the next one (if any)
    let now = new Date();

    for (let i = 0; i < response.length; i++) {
      if (response[i].startDatetime <= now && response[i].endDatetime >= now) {
        current_lesson = response[i];
        if (i + 1 < response.length) {
          next_lesson = response[i + 1];
        }
      }
    }
  }

  // Function to go to the page to record the attendance of the lesson
  function takeAttendance(id) {
    push("/attendance/lesson/" + current_lesson.id);
  }
</script>

<Card body class="p-3 h-100">
  {#await getDetails()}
    <h2>Right now</h2>
    <p>Retrieving Information...</p>
  {:then}
    <!-- Display the number of lessons on current day -->
    {#if no_lessons == 0}
      <h2>Right now</h2>
      <p>There are no lessons today</p>
    {:else}
      <!-- Display the current lesson -->
      <h2>Current Lesson</h2>
      {#if current_lesson != null}
        <p>
          {displayTime(current_lesson.startDatetime)} - {displayTime(
            current_lesson.endDatetime
          )}
        </p>
        <p>
          {current_lesson.classFk.name}
          {current_lesson.subject.name}
          {current_lesson.subjectLevel.name}
        </p>

        <Button color="primary" on:click={() => takeAttendance()}
          >Take Attendance</Button
        >
      {:else}
        <p>There is no lesson right now</p>
      {/if}
      <!-- Display the next lesson on current day -->
      {#if next_lesson != null}
        <h2>Next Lesson</h2>

        <p>
          {displayTime(next_lesson.startDatetime)} - {displayTime(
            next_lesson.endDatetime
          )}
        </p>
        <p>
          {next_lesson.classFk.name}
          {next_lesson.subject.name}
          {next_lesson.subjectLevel.name}
        </p>
      {/if}
    {/if}
  {:catch}
    <p>Could not retrieve information...</p>
  {/await}
</Card>
