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
    Tooltip,
  } from "sveltestrap";
  import { tick } from "svelte";

  import API_CONFIG from "../../../api";
  import { StudentsApi } from "kumon_app_backend_api";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../../components/PaginationFilteringBar.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import AddStudentModal from "./modals/AddStudentModal.svelte";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";

  import StudentDetails from "./StudentDetails.svelte";
  import StudentHelp from "./StudentHelp.svelte";

  /**
   * The students API instance in use.
   * @type {StudentsApi}
   */
  let studentsApi = new StudentsApi(API_CONFIG);

  /**
   * List of students
   */
  let students = [];

  /**
   * The ID of the student currently selected.
   * @type {number}
   */
  let selectedStudent;

  let pageFilterDetailsStudents = new PageFilter();
  let openHelp = false;

  /**
   * Refreshes the list of students.
   */
  async function refreshStudents() {
    try {
      let response = await studentsApi.studentsList({
        page: pageFilterDetailsStudents.page,
        search: pageFilterDetailsStudents.filter,
      });

      students = response.results;

      pageFilterDetailsStudents.pageUpdate(response);
      pageFilterDetailsStudents.filter += " ";
      pageFilterDetailsStudents.filter =
        pageFilterDetailsStudents.filter.substring(
          0,
          pageFilterDetailsStudents.filter.length - 1
        );
    } catch (e) {
      openModal(InfoModal, {
        title: "Students List",
        message: `Could not fetch list of students!`,
      });
    }
  }

  /**
   * Handler for adding a new student.
   */
  function handleAddStudent() {
    openModal(AddStudentModal, {
      onAdd: async (_) => {
        await refreshStudents();
      },
    });
  }

  /**
   * Loads the student's current details into this form.
   * @param {number} id The ID of the student.
   */
  async function handleViewStudentDetails(id) {
    if (selectedStudent === id) {
      selectedStudent = undefined;
    } else {
      selectedStudent = undefined;
      await tick();
      selectedStudent = id;
    }
  }

  /**
   * Edit event handler
   * @param {details} event matches the api endpoint for students
   */
  function handleEdit(event) {
    let existingIndex = students.findIndex(
      (student) => student.id === event.detail.studentId
    );

    if (existingIndex >= 0) {
      students[existingIndex] = {
        id: event.detail.studentId,
        kSisId: event.detail.newDetails.kSisId,
        firstName: event.detail.newDetails.firstName,
        middleName: event.detail.newDetails.middleName,
        lastName: event.detail.newDetails.lastName,
        dateOfBirth: event.detail.newDetails.dateOfBirth,
        school: event.detail.newDetails.school,
        grade: event.detail.newDetails.grade,
      };
    }
  }

  /**
   * Delete event handler
   * @param {details} event matches the api endpoint for students
   */
  async function handleDelete(event) {
    selectedStudent = undefined;
    await refreshStudents();
    await tick();
  }

  async function handleCloseView() {
    selectedStudent = undefined;
    await tick();
  }
</script>

<Container class="p-3">
  <Row>
    <Col>
      <h1>Student Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpStudent"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpStudent" placement="top">
        User Guide for Student Manager
      </Tooltip>
    </Col>
  </Row>
  <Row>
    <Col>
      <h2>Student List</h2>
    </Col>

    <Col>
      <!-- Add a Student -->
      <Button
        id="addStudent"
        color="success"
        style="float: right;"
        on:click={() => handleAddStudent()}
      >
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addStudent" placement="top">Add a New Student</Tooltip>
    </Col>
  </Row>

  <!-- Add a Student -->
  <PaginationFilteringBar
    refresh={() => refreshStudents()}
    pageFilter={pageFilterDetailsStudents}
  />

  <Table id="studentTable">
    <thead>
      <tr>
        <th style="width: 10%">K-SIS ID</th>
        <th style="width: 15%">First Name</th>
        <th style="width: 15%">Middle Name</th>
        <th style="width: 15%">Last Name</th>
        <th style="width: 15%">Date of Birth</th>
        <th style="width: 25%">School</th>
        <th style="width: 5%">Grade</th>
      </tr>
    </thead>

    {#await refreshStudents()}
      <tfoot class="info">
        <tr>
          <td colspan="6">Retrieving list of students...</td>
        </tr>
      </tfoot>
    {:then}
      {#if students.length === 0}
        <tfoot class="info">
          <tr>
            <td colspan="6">No student data found</td>
          </tr>
        </tfoot>
      {:else}
        <tbody>
          {#each students as student}
            <tr
              class:selected={selectedStudent === student.id}
              on:click={() => handleViewStudentDetails(student.id)}
            >
              {#if student.kSisId}
                <td>{student.kSisId}</td>
              {:else}
                <td>N/A</td>
              {/if}

              <td>{student.firstName}</td>
              <td>{student.middleName}</td>
              <td>{student.lastName}</td>
              <td>{displayDate(student.dateOfBirth)}</td>
              <td>{student.school}</td>
              <td>{student.grade}</td>
            </tr>
          {/each}
        </tbody>
      {/if}
    {:catch}
      <tfoot class="info">
        <tr>
          <td colspan="6">Could not retrieve list of students!</td>
        </tr>
      </tfoot>
    {/await}
  </Table>

  {#if selectedStudent}
    <StudentDetails
      studentId={selectedStudent}
      on:edit={handleEdit}
      on:delete={handleDelete}
      on:close={handleCloseView}
    />
  {/if}

  <StudentHelp bind:open={openHelp} />
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
