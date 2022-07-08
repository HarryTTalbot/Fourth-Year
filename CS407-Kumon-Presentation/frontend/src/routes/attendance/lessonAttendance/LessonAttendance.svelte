<script>
  import { onMount } from "svelte";
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
  import { pop } from "svelte-spa-router";
  import StudentField from "../../../formFields/StudentField.svelte";

  import API_CONFIG from "../../../api";
  import { LessonApi, StudentsApi } from "kumon_app_backend_api";
  import InfoModal from "../../../modals/InfoModal.svelte";

  import { FileDownloader } from "../../../utils";
  import LessonAttendanceHelp from "./LessonAttendanceHelp.svelte";

  let lessonID = window.location.hash.substring(20);
  if (lessonID.includes("/")) {
    lessonID = lessonID.substring(0, lessonID.indexOf("/"));
  }
  let LessonDetails = { day: "Loading", class: "", start: "", subject: "" };
  let lessonApi = new LessonApi(API_CONFIG);
  let studentApi = new StudentsApi(API_CONFIG);
  let lessonStudents = [];
  let addComp;
  let studentToAdd = null;
  let present = 0;
  let status;
  let openHelp = false;
  /**
   * Whether we are refreshing the list of imports.
   * @type {boolean}
   */
  let isRefreshing = false;

  /**
   * The file downloader helper instance we're using.
   * @type {FileDownloader}
   */
  export let fileDownloader = new FileDownloader();

  async function refreshList() {
    isRefreshing = true;
    present = 0;
    let lessonInfo = await lessonApi.lessonRetrieve({ id: lessonID });
    let lessonDay = new Intl.DateTimeFormat("en-GB", {
      weekday: "long",
    }).format(lessonInfo.startDatetime);
    let lessonTime = new Intl.DateTimeFormat("en-GB", {
      hour: "numeric",
      minute: "numeric",
    }).format(lessonInfo.startDatetime);
    LessonDetails = {
      day: lessonDay,
      start: lessonTime,
      class: lessonInfo.classFk.name,
      subject: lessonInfo.subject.name,
    };
    // Get the attendance list for the lesson of lessonID
    try {
      let response = await lessonApi.lessonGetAttendanceList({ id: lessonID });
      lessonStudents = response;
    } catch (e) {}
    // Count the number of students present
    if (lessonStudents.length > 0) {
      for (const entry of lessonStudents) {
        if (entry.status === "P") {
          present = present + 1;
        }
      }
    }
    isRefreshing = false;
  }

  async function handleDownload() {
    // Get the document version to download for attendance
    try {
      let response = await lessonApi.lessonGetAttendanceSheetRetrieve({
        id: lessonID,
      });

      let filename = "Attendance" + ".pdf";

      fileDownloader.downloadBlob(response, filename);
    } catch (e) {}
  }

  async function handleAddStudent() {
    // Check if a student has been selected
    if (studentToAdd == null) {
      openModal(InfoModal, {
        title: "Add Student To Lesson",
        message: "You must select a student to add",
      });
      return;
    }
    // Check if the student is already in the class
    for (let i = 0; i < lessonStudents.length; i++) {
      if (lessonStudents[i].student.id == studentToAdd) {
        openModal(InfoModal, {
          title: "Add Student To Lesson",
          message: "You cannot add a student who is already in the lesson",
        });
        return;
      }
    }
    isRefreshing = true;
    // Get the details of the student
    let response = await studentApi.studentsRetrieve({ id: studentToAdd });
    let newStudent = {
      student: {
        id: response.id,
        kSisId: response.kSisId,
        firstName: response.firstName,
        middleName: response.middleName,
        lastName: response.lastName,
      },
      status: "P",
    };
    lessonStudents.push(newStudent);

    let studentAttendance = [{ student: newStudent.student.id, status: "P" }];

    await lessonApi.lessonSetAttendanceCreate({
      id: lessonID,
      lessonSetAttendanceRequest: studentAttendance,
    });

    isRefreshing = false;
    studentToAdd = null;
    addComp.handleClear();
  }

  async function handleSubmit() {
    // Submit the attendance i.e overwrite with new lessonStudents
    // Create studentAttendance array and loop through students, adding {student, attendance} pairs to the array
    let studentAttendance = [];
    for (const entry of lessonStudents) {
      studentAttendance.push({
        student: entry.student.id,
        status: entry.status,
      });
    }
    try {
      // Submit the {student:attendance} pairs to be added to the DB
      await lessonApi.lessonSetAttendanceCreate({
        id: lessonID,
        lessonSetAttendanceRequest: studentAttendance,
      });
      openModal(InfoModal, {
        title: "Submit Attendance",
        message: "Attendance Saved",
      });
      refreshList();
    } catch (e) {
      openModal(InfoModal, {
        title: "Submit Attendance",
        message:
          "Unable to save attendance! Please ensure every student has been assigned an attendance code",
      });
    }
  }

  function handleCancel() {
    // Go back to the previous page
    pop();
  }

  // Sets the status for all students
  function handleAll(status) {
    for (let i = 0; i < lessonStudents.length; i++) {
      if (lessonStudents[i].status == "") {
        lessonStudents[i].status = status;
      }
    }
  }

  /**
   * Refreshes classes when the page is loaded; Doesn't work when navigating  to the page via URL
   */
  onMount(async () => {
    await refreshList();
  });
</script>

<!-- Content of the page -->
<Container class="p-3">
  <Row>
    <Col xs="auto">
      <h1>
        {LessonDetails.day}
        {LessonDetails.start} — {LessonDetails.class}
        {LessonDetails.subject}
      </h1>
    </Col>

    <Col>
      <Button
        id="helpLessonAttendance"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpLessonAttendance" placement="top">
        User Guide for Lesson Attendance Manager
      </Tooltip>

      <Button
        id="DownloadAttendance"
        color="primary"
        on:click={handleDownload}
        style="float: right; margin-right:20px;"
      >
        <Icon name="download" />
      </Button>
      <Tooltip target="DownloadAttendance" placement="top">
        Download PDF of Attendance Sheet
      </Tooltip>
    </Col>
  </Row>
  <!-- Display how many students are in the class, and how many are present. Use ternary operators to ensure correct grammar -->
  <p>
    {lessonStudents.length}
    {lessonStudents.length > 1 ? "students" : "student"}, {present ===
    lessonStudents.length
      ? "all of which are present"
      : present > 1
      ? present + " of which are present"
      : present === 1
      ? present + " of which is present"
      : "none of which are present"}
  </p>

  <div>
    <Table>
      <!-- Student Table Headings -->
      <thead>
        <tr style="border-style : hidden">
          <td colspan="2">
            <StudentField bind:this={addComp} bind:student={studentToAdd} />
          </td>
          <td>
            <Row>
              <Col>
                <Button
                  id="AddStudent"
                  color="success"
                  on:click={handleAddStudent}
                >
                  <Icon name="plus-square" />
                </Button>
                <Tooltip target="AddStudent" placement="top">
                  Add Student To Register
                </Tooltip>
              </Col>
              <Col>
                <p style="text-align:right">Mark all unmarked students as</p>
              </Col>
            </Row>
          </td>
          <th id="AllP" style="text-align:center">
            <Button color="primary" on:click={() => handleAll("P")}>
              P <Icon name="check2" />
              <Tooltip target="AllP" placement="top">Present</Tooltip>
            </Button>
          </th>
          <th id="AllL" style="text-align:center">
            <Button color="primary" on:click={() => handleAll("L")}>
              L <Icon name="clock" />
              <Tooltip target="AllL" placement="top">Late</Tooltip>
            </Button>
          </th>
          <th id="AllA" style="text-align:center">
            <Button color="primary" on:click={() => handleAll("A")}>
              A <Icon name="calendar-check" />
              <Tooltip target="AllA" placement="top">
                Authorised Absence
              </Tooltip>
            </Button>
          </th>
          <th id="AllU" style="text-align:center">
            <Button color="primary" on:click={() => handleAll("U")}>
              U <Icon name="x-lg" />
              <Tooltip target="AllU" placement="top">
                Unauthorised Absence
              </Tooltip>
            </Button>
          </th>
        </tr>
        <tr>
          <th>First Name</th>
          <th>Middle Name</th>
          <th>Last Name</th>

          <th id="Present" style="text-align:center">
            P <Icon name="check2" /></th
          >
          <Tooltip target="Present" placement="top">Present</Tooltip>

          <th id="Late" style="text-align:center"> L <Icon name="clock" /></th>
          <Tooltip target="Late" placement="top">Late</Tooltip>

          <th id="Authorised" style="text-align:center">
            A <Icon name="calendar-check" /></th
          >
          <Tooltip target="Authorised" placement="top">
            Authorised Absence
          </Tooltip>

          <th id="Unauthorised" style="text-align:center">
            U <Icon name="x-lg" /></th
          >
          <Tooltip target="Unauthorised" placement="top">
            Unauthorised Absence
          </Tooltip>
        </tr>
      </thead>

      {#if isRefreshing}
        <!-- Whilst waiting for backend response -->
        <tfoot class="info">
          <tr>
            <td colspan="6">Retrieving list of students...</td>
          </tr>
        </tfoot>
      {:else if lessonStudents.length === 0}
        <!-- If no students are returned -->
        <tfoot class="info">
          <tr>
            <td colspan="6">No students assigned to this class</td>
          </tr>
        </tfoot>
      {:else}
        <!-- If students are returned -->
        <tbody>
          {#each lessonStudents as entry}
            <tr>
              <td>{entry.student.firstName}</td>
              <td>
                {#if entry.student.middleName != "" && entry.student.middleName != undefined}
                  {entry.student.middleName}
                {:else}
                  —
                {/if}
              </td>
              <td>{entry.student.lastName}</td>
              <!-- 4 radio buttons: Present, late, Auth absence, unauth absence, -->
              <td style="text-align:center"
                ><input
                  type="radio"
                  id="bigger"
                  bind:group={entry.status}
                  value={"P"}
                /></td
              >
              <td style="text-align:center"
                ><input
                  type="radio"
                  id="bigger"
                  bind:group={entry.status}
                  value={"L"}
                /></td
              >
              <td style="text-align:center"
                ><input
                  type="radio"
                  id="bigger"
                  bind:group={entry.status}
                  value={"A"}
                /></td
              >
              <td style="text-align:center"
                ><input
                  type="radio"
                  id="bigger"
                  bind:group={entry.status}
                  value={"U"}
                /></td
              >
            </tr>
          {/each}
        </tbody>
      {/if}
    </Table>
  </div>

  <div style="float: right;">
    <Button color="secondary" on:click={handleCancel}>Back</Button>
    <Button color="primary" on:click={handleSubmit}>Submit</Button>
  </div>

  <LessonAttendanceHelp bind:open={openHelp} />
</Container>

<style>
  input#bigger {
    transform: scale(1.5);
  }
</style>
