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
  import { ClassesApi, StudentsApi } from "kumon_app_backend_api";

  import AddressDisplay from "../../../utils/displayAddress.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import EditClassModal from "./modals/EditClassModal.svelte";
  import AssignStudentsModal from "./modals/AssignStudentsModal.svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";
  import { createEventDispatcher } from "svelte";

  import { FileDownloader } from "../../../utils";

  let studentsApi = new StudentsApi(API_CONFIG);
  let classApi = new ClassesApi(API_CONFIG);
  const dispatch = createEventDispatcher();

  export let classId;

  let classInfo;
  let students = [];
  let openStudent;
  let studentInfo;

  /**
   * Refreshes the list of students.
   */
  async function getClassInfo() {
    try {
      classInfo = await classApi.classesRetrieve({ id: classId });

      students = await classApi.classesGetStudentsList({ id: classId });

      openStudent = undefined;
      studentInfo = undefined;
    } catch (e) {}
  }

  /**
   * Handler for editing a student.
   * @param {number} id The ID of the student.
   */
  async function handleEditClass() {
    openModal(EditClassModal, {
      id: classId,
      onClassEdit: async () => {
        dispatch("edit");
        await getClassInfo();
      },
    });
  }

  /**
   * Handler for editing a student.
   * @param {number} id The ID of the student.
   */
  function handleStudents() {
    openModal(AssignStudentsModal, {
      classID: classId,
      onEdit: async () => {
        dispatch("edit");
        await getClassInfo();
      },
    });
  }

  /**
   * Handler for removing a student.
   * @param {number} id The ID of the student.
   */
  async function handleRemoveClass() {
    let cls = await classApi.classesRetrieve({ id: classId });
    let confirmationMessage =
      "Are you sure you want to delete this class?\n\n" +
      "Name: " +
      cls.name +
      "\nID: " +
      cls.id;

    // Display a modal to confirm deletion of a class
    openModal(ConfirmationModal, {
      title: "Delete Class",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        try {
          // NOTE: Promise API used here as better than async in this context
          classApi.classesDestroy({ id: classId }).then((_) => {
            // Remove this student from the displayed list
            dispatch("delete", { classId: classId });

            // NOTE: Second object is needed to "replace" the confirmation modal (otherwise it will re-open)
            openModal(
              InfoModal,
              {
                title: "Delete Class",
                message: `Deleted class ${classId}.`,
              },
              {
                replace: true,
              }
            );
          });
        } catch (e) {
          openModal(
            InfoModal,
            {
              title: "Delete Class",
              message: `Could not mark class ${classId} for deletion!`,
            },
            {
              replace: true,
            }
          );
        }
      },
    });
  }

  // Retrieve information about a student if they are viewed, using the student ID
  async function handleViewStudent() {
    try {
      studentInfo = undefined;
      await tick();
      studentInfo = await studentsApi.studentsRetrieve({ id: openStudent });
    } catch (e) {}
  }

  function close() {
    dispatch("close");
  }
</script>

<Card>
  {#await getClassInfo()}
    <p>Fetching Student Data ....</p>
  {:then}
    <CardHeader>
      <Row>
        <Col xs="auto">
          <h3>Class Details</h3>
        </Col>
        <Col>
          <Button
            color="danger"
            id="deleteClass"
            on:click={() => handleRemoveClass()}
          >
            <Icon name="trash" />
          </Button>
          <Tooltip target="deleteClass" placement="top">Delete Class</Tooltip>
        </Col>
        <Col>
          <Button
            outline
            color="secondary"
            id="closeClass"
            style="float: right;"
            on:click={() => close()}
          >
            <Icon name="x" />
          </Button>
          <Tooltip target="closeClass" placement="top">
            Close Class Details
          </Tooltip>
        </Col>
      </Row>
    </CardHeader>
    <CardBody>
      <Row>
        <Col>
          <Row>
            <Col xs="auto">
              <h5>Details</h5>
            </Col>
            <Col>
              <Button
                color="primary"
                id="editClass"
                on:click={() => handleEditClass()}
              >
                <Icon name="pen" />
              </Button>
              <Tooltip target="editClass" placement="top">
                Edit Class Details
              </Tooltip>
            </Col>
          </Row>

          <p class="spacing">
            <b> Name: </b>
            {classInfo.name} <br />

            <b> Size: </b>
            {classInfo.size} <br />
          </p>
        </Col>
        <Col>
          <Row>
            <Col xs="auto">
              <h5>Students</h5>
            </Col>

            <Col>
              <Button
                color="primary"
                id="manageStudents"
                on:click={() => handleStudents()}
              >
                <Icon name="pen" />
              </Button>
              <Tooltip target="manageStudents" placement="top">
                Manage Students
              </Tooltip>
            </Col>
          </Row>

          <p class="spacing">
            {classInfo.name} has {students.length} associated student(s) <br />
            {#if students.length > 0}
              Choose one to view their details: <br />
              <Input
                id="student"
                type="select"
                bind:value={openStudent}
                on:change={handleViewStudent}
              >
                {#each students as student}
                  <option value={student.id}
                    >{student.lastName}, {student.firstName}</option
                  >
                {/each}
              </Input>
            {/if}
          </p>

          <!-- Display student details if selected -->
          {#if studentInfo}
            <p class="spacing">
              <b> First Name: </b>
              {studentInfo.firstName} <br />
              {#if studentInfo.middleName}
                <b> Middle Name: </b> {studentInfo.middleName} <br />
              {:else}
                <b> Middle Name: </b> n/a <br />
              {/if}
              <b> Last Name: </b>
              {studentInfo.lastName} <br />

              <b> Date of Birth: </b>
              {displayDate(studentInfo.dateOfBirth)} <br />

              {#if studentInfo.joinDate}
                <b> Join Date: </b> {displayDate(studentInfo.joinDate)} <br />
              {:else}
                <b> Join Date: </b> n/a <br />
              {/if}
              {#if studentInfo.leaveDate}
                <b> Leave Date: </b> {displayDate(studentInfo.leaveDate)} <br />
              {:else}
                <b> Leave Date: </b> n/a <br />
              {/if}

              <b> School: </b>
              {studentInfo.school} <br />
              <b> Grade: </b>
              {studentInfo.grade} <br />

              <b> Telephone Number: </b>
              {studentInfo.phoneNumber} <br />
              <b> Email Address: </b>
              {studentInfo.email} <br />

              <b> Address: </b> <br />
              <AddressDisplay address={studentInfo.address} />
            </p>
          {/if}
        </Col>
      </Row>
    </CardBody>
  {/await}
</Card>

<style>
  p.spacing {
    line-height: 1.5;
  }
</style>
