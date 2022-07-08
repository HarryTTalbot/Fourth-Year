<script>
  import { onMount } from "svelte";
  import { openModal } from "svelte-modals";
  import {
    Button,
    Container,
    Table,
    Collapse,
    FormGroup,
    Label,
    Input,
    Row,
    Col,
    Tooltip,
    Icon,
  } from "sveltestrap";

  import MainNavbar from "../components/MainNavbar.svelte";
  import API_CONFIG from "../api";
  import { StudentsApi } from "kumon_app_backend_api";
  import { ClassesApi } from "kumon_app_backend_api";
  import StudentField from "../formFields/StudentField.svelte";
  import ClassesField from "../formFields/ClassField.svelte";
  import InfoModal from "../modals/InfoModal.svelte";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../components/PaginationFilteringBar.svelte";
  import RecordSheetForm from "./recordSheet/forms/RecordSheetForm.svelte";

  import { RecordSheetApi } from "kumon_app_backend_api";
  import { FileDownloader } from "../utils";

  import RecordSheetGeneratorHelp from "./recordSheet/RecordSheetGeneratorHelp.svelte";

  // Import classes API to handle adding all students in a class to the list for the record sheet
  let classApi = new ClassesApi(API_CONFIG);
  let classes = [];
  let classID = null;

  // Import students API to handle adding individual students to the list for the record sheet
  let studentApi = new StudentsApi(API_CONFIG);
  let students = [];
  let studentID = null;

  // Import record sheet API to generate the record sheet itself, given the inputs from the form
  let recordSheetApi = new RecordSheetApi(API_CONFIG);

  // Initialise a set to store student objects of the students for whom to generate the record sheet
  let studentsSelected = [];

  let chosenClass = null; // Stores the value selected in the dropdown
  let focused = false;

  let studentToAdd; // Indicates if a student has been selected in the search
  let classToAdd; // Indicates if a class has been selected in the search
  let addStudentComp; // For clearing search contents
  let addClassComp; // For clearing search contents

  // Boolean to indicate if the help pane is open or closed
  let openHelp = false;

  /**
   * The backing form component for the "Add Student" form.
   * @type {RecordSheetForm}
   */
  let addRecordSheetForm;

  /**
   * Whether we are refreshing the list of imports.
   * @type {boolean}
   */
  let isRefreshing = false;

  /**
   * Refreshes the list of classes.
   */
  export async function refreshClasses() {
    isRefreshing = true;
    try {
      let response = await classApi.classesList({});
      classes = response.results;
    } catch (e) {}
    isRefreshing = false;
  }

  /**
   * Refreshes the list of students.
   * @param {number} cid The ID of the class we're refreshing the lists for.
   */
  export async function refreshStudents() {
    isRefreshing = true;

    try {
      let inClass = await classApi.classesGetStudentsList({ id: classID });
      let notInClass = await classApi.classesGetStudentsNotInClassList({
        id: classID,
        page: pageFilterNotInClass.page,
        search: pageFilterNotInClass.filter,
      });
    } catch (e) {}

    isRefreshing = false;
  }

  async function handleAddStudent() {
    // Check if a student has been selected
    if (studentToAdd == null) {
      openModal(InfoModal, {
        title: "Add Student To Record Sheet",
        message: "You must select a student to add",
      });
      return;
    }
    // Check if the student is already in the class
    for (let i = 0; i < studentsSelected.length; i++) {
      if (studentsSelected[i].id == studentToAdd) {
        openModal(InfoModal, {
          title: "Add Student To Record Sheet",
          message:
            "You cannot add a student who is already in the record sheet",
        });
        return;
      }
    }
    isRefreshing = true;
    // Get the details of the student
    let response = await studentApi.studentsRetrieve({ id: studentToAdd });

    studentsSelected.push(response);

    isRefreshing = false;
    //studentToAdd = null;
    addStudentComp.handleClear();
  }

  async function handleAddClass() {
    // Check if a student has been selected
    if (classToAdd == null) {
      openModal(InfoModal, {
        title: "Add Class To Record Sheet",
        message: "You must select a class to add",
      });
      return;
    }

    isRefreshing = true;
    // Get the students in the class
    let inClass = await classApi.classesGetStudentsList({ id: classToAdd });
    // Check if the student is already in the class.
    // Store the number of students already in the table at the start of the function call
    let startingLength = studentsSelected.length;
    // A variable to keep track of how many students have actually been added from the selected class
    let addedCounter = 0;
    // If there are already students in the table, and thus potentially duplicates between the table and the selected class
    if (startingLength > 0) {
      // Make pairwise comparisons between the ids of the students in the table and the students in the selected class
      for (let i = 0; i < inClass.length; i++) {
        for (let j = 0; j < startingLength; j++) {
          // If there's a match, don't add the student again. Move on to the next student in the class
          if (inClass[i].id == studentsSelected[j].id) {
            break;
          }
          // If the student from the class to add has been compared against every student already in the table without a match, add the student
          if (j == startingLength - 1) {
            studentsSelected.push(inClass[i]);
            addedCounter += 1;
          }
        }
      }
    } else {
      // If there are no students already selected, just add the whole class
      for (let i = 0; i < inClass.length; i++) {
        studentsSelected.push(inClass[i]);
        addedCounter += 1;
      }
    }

    isRefreshing = false;
    addClassComp.handleClear();

    if (addedCounter == 0) {
      openModal(InfoModal, {
        title: "Add Class To Record Sheet",
        message: "All members of this class are already in the record sheet",
      });
      return;
    }
  }

  /**
   * Handler for removing a student from the array.
   * @param {number} id The ID of the student we're removing.
   */
  async function handleRemoveStudent(id) {
    let student = await studentApi.studentsRetrieve({ id: id });

    try {
      isRefreshing = true;
      // Remove this student from the displayed list
      studentsSelected = studentsSelected.filter(
        (student) => student.id !== id
      );

      isRefreshing = false;
    } catch (e) {
      openModal(
        InfoModal,
        {
          title: "Remove Student",
          message: `Could not remove student ${id}!`,
        },
        { replace: true }
      );
    }
  }

  /**
   * Refreshes classes when the page is loaded
   */
  onMount(async () => {
    await refreshClasses();
  });

  async function handleSubmit(evt) {
    try {
      // Get the ids of all student objects in the table and store them in the array "ids"
      let ids = [];
      for (let i = 0; i < studentsSelected.length; i++) {
        ids.push(studentsSelected[i].id);
      }
      if (ids.length > 0) {
        /**
         * The file downloader helper instance we're using.
         * @type {FileDownloader}
         */
        let fileDownloader = new FileDownloader();
        evt.startDate.setHours(12, 0, 0);
        // Create a record sheet by sending the information from the form to the backend
        let response = await recordSheetApi.recordSheetCreateStudentSheetCreate(
          {
            studentRecordSheetRequest: {
              studentId: ids,
              subjectLevelId: evt.subjectLevel,
              startDate: evt.startDate,
              numDays: evt.days,
              sheetsPerDay: evt.numSheets,
              completionTime: evt.completionTime,
              type: "string",
            },
          }
        );
        // Give the record sheet a file name containing today's date
        let today = new Date();
        let filename = "Record-Sheet-" + today.toLocaleDateString("en-GB");

        fileDownloader.downloadBlob(response, filename);
      } else {
        // Open a modal to tell them to select more students
        openModal(InfoModal, {
          title: "Generate Record Sheet",
          message: "Please select at least one student",
        });
      }
      // A modal to be displayed if the record sheet has been generated successfully
      openModal(InfoModal, {
        title: "Generate Record Sheet",
        message:
          "Record sheet generated and downloaded! It should be accessible via a button at the bottom of the window",
      });
    } catch (e) {
      // Open a modal to tell them the creation was unsuccessful
      openModal(InfoModal, {
        title: "Generate Record Sheet",
        message: e.statusText,
      });
    }
  }
</script>

<main>
  <MainNavbar active="/recordsheet" />

  <Container class="p-3">
    <Row>
      <Col>
        <h1>Record Sheet Generator</h1>
      </Col>

      <!-- Create button for user guide -->
      <Col>
        <Button
          id="helpRecordSheet"
          color="dark"
          style="float: right;"
          on:click={() => (openHelp = !openHelp)}
        >
          <Icon name="question-square" />
        </Button>
        <Tooltip target="helpRecordSheet" placement="top">
          User Guide for Record Sheet Generator
        </Tooltip>
      </Col>
    </Row>

    <!-- Table to display students the user has selected, and for whom the record sheet will be generated -->
    <Table>
      <thead>
        <tr>
          <th>K-SIS ID</th>
          <th>First Name</th>
          <th>Last Name</th>
          <th />
        </tr>
      </thead>

      {#if isRefreshing}
        <tfoot class="info">
          <tr>
            <td colspan="4">Retrieving list of students...</td>
          </tr>
        </tfoot>
      {:else if studentsSelected.length === 0}
        <tfoot class="info">
          <tr>
            <td colspan="4">No students selected</td>
          </tr>
        </tfoot>
      {:else}
        <tbody>
          {#each studentsSelected as student}
            <tr>
              {#if student.kSisId}
                <td>{student.kSisId}</td>
              {:else}
                <td>N/A</td>
              {/if}
              <td>{student.firstName}</td>
              <td>{student.lastName}</td>
              <td>
                <!-- Button to remove a student from the table -->
                <Button
                  color="danger"
                  on:click={() => handleRemoveStudent(student.id)}
                  id="removeStudent{student.id}"
                >
                  <Icon name="trash" />
                  <Tooltip target="removeStudent{student.id}" placement="top">
                    Remove {student.lastName}, {student.firstName}
                  </Tooltip>
                </Button>
              </td>
            </tr>
          {/each}
        </tbody>
      {/if}
    </Table>

    <h5>Add a student:</h5>

    <!-- Create a search box for students -->
    <StudentField
      id="student"
      bind:this={addStudentComp}
      bind:student={studentToAdd}
      on:change={handleAddStudent}
    />

    <br />

    <h5>Add all students in a class:</h5>

    <!-- Create search box for classes -->
    <ClassesField
      id="class"
      bind:this={addClassComp}
      bind:classID={classToAdd}
      on:change={handleAddClass}
    />

    <br />
    <h3>Record Sheet Options</h3>
    <!-- Form for input needed to generate PDF  -->
    <RecordSheetForm
      id="add-record-sheet-form"
      bind:this={addRecordSheetForm}
      on:submit={async (e) => handleSubmit(e.detail)}
    />
    <br />
    <Button color="primary" form="add-record-sheet-form" type="submit">
      Submit
    </Button>
  </Container>
</main>

<RecordSheetGeneratorHelp bind:open={openHelp} />

<style>
  main {
    height: 100vh;
  }
</style>
