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
  import { StudentsApi, StaffApi } from "kumon_app_backend_api";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../../components/PaginationFilteringBar.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";

  import DeletedRecordsHelp from "./DeletedRecordsHelp.svelte";

  let studentsApi = new StudentsApi(API_CONFIG);
  let staffApi = new StaffApi(API_CONFIG);
  let students = [];
  let staffList = [];
  let openHelp = false;

  /**
   * Refreshes the list of deleted students and staff.
   */
  async function refresh() {
    students = await studentsApi.studentsListDeletedList({});

    staffList = await staffApi.staffListDeletedList({});
  }

  /**
   * Sends a request to the backend to restore a student
   */
  async function restoreStudent(studentId) {
    try {
      // Query the backend to restore the student
      await studentsApi.studentsGdprRestoreCreate({ id: studentId });

      // Remove the student from the list
      await refresh();

      // Open a modal to inform that the restoration was successful
      openModal(
        InfoModal,
        {
          title: "Restore Student",
          message: `Successfully restored!`,
        },
        { replace: true }
      );
    } catch (e) {
      // Open a modal to inform the user that the restoration has been unsuccessful
      openModal(
        InfoModal,
        {
          title: "Restore Student",
          message: `Could not restore!`,
        },
        { replace: true }
      );
    }
  }

  /**
   * Sends a request to the backend to restore a staff member
   */
  async function restoreStaff(staffId) {
    try {
      // Query the backend to restore the staff member
      await staffApi.staffGdprRestoreCreate({ id: staffId });

      // Remove the staff member from the list
      await refresh();

      // Open a modal to inform that the restoration was successful
      openModal(
        InfoModal,
        {
          title: "Restore Staff",
          message: `Successfully restored!`,
        },
        { replace: true }
      );
    } catch (e) {
      // Open a modal to inform the user that the restoration has been unsuccessful
      openModal(
        InfoModal,
        {
          title: "Restore Staff",
          message: `Could not restore!`,
        },
        { replace: true }
      );
    }
  }

  /**
   * Sends a request to the backend to delete a staff member
   */
  async function permanentlyDeleteStaff(staffId) {
    // Query the backend to get the staff details (as they are in the database)
    let staff = await staffApi.staffRetrieve({ id: staffId });

    // Formulate a confirmation message to the user
    let confirmationMessage =
      "Are you sure you want to permanently delete this staff member?\n\n" +
      "Name: " +
      staff.firstName +
      " " +
      staff.lastName;

    // Open a confirmation modal to ask the user to confirm the deletion
    openModal(ConfirmationModal, {
      title: "Permanently Delete Staff",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        // If the user confirms the deletion
        try {
          // Query the backend to remove the staff member (uses Promise API)
          staffApi.staffDestroy({ id: staff.id }).then((_) => {
            // Remove the staff member from the list
            staffList = staffList.filter(function (value, index, arr) {
              return value.id != staff.id;
            });

            // Open a modal to inform the user that the staff member has been removed
            openModal(
              InfoModal,
              {
                title: "Permanently Delete Staff",
                message: `Permanently Deleted staff ${staff.firstName} ${staff.lastName}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          // Open a modal to inform the user that the deletion has been unsuccessful
          openModal(
            InfoModal,
            {
              title: "Permanently Delete Staff",
              message: `Could not permanently delete ${staff.firstName} ${staff.lastName}!`,
            },
            { replace: true }
          );
        }
      },
    });
  }

  /**
   * Sends a request to the backend to delete a student
   */
  async function permanentlyDeleteStudent(studentId) {
    let student = await studentsApi.studentsRetrieve({ id: studentId });
    let confirmationMessage =
      "Are you sure you want to permanently delete this student?\n\n" +
      "Name: " +
      student.firstName +
      " " +
      student.lastName +
      "\nID: " +
      student.id +
      "\nK-SIS ID: " +
      student.kSisId;

    openModal(ConfirmationModal, {
      title: "Permanently Delete Student",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        try {
          // NOTE: Promise API used here since using async in this context probably isn't a good idea...
          studentsApi.studentsDestroy({ id: studentId }).then((_) => {
            // Remove this student from the displayed list
            students = students.filter(function (value, index, arr) {
              return value.id != studentId;
            });

            // NOTE: Second object is needed to "replace" the confirmation modal (otherwise it will re-open)
            openModal(
              InfoModal,
              {
                title: "Permanently Delete Student",
                message: `Permanently Deleted student ${studentId}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          openModal(
            InfoModal,
            {
              title: "Permanently Delete Student",
              message: `Could not delete student!`,
            },
            { replace: true }
          );
        }
      },
    });
  }
</script>

<Container class="p-3">
  <Row>
    <Col>
      <h1>Deleted Records Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpDeletedRecords"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpDeletedRecords" placement="top">
        User Guide for Deleted Records Manager
      </Tooltip>
    </Col>
  </Row>
  <h2>Student List</h2>

  <Table id="studentTable">
    <thead>
      <tr>
        <th style="width: 15%">First Name</th>
        <th style="width: 15%">Middle Name</th>
        <th style="width: 15%">Last Name</th>
        <th style="width: 15%">Date of Birth</th>
        <th style="width: 15%">Deleted on</th>
        <th style="width: 15%">Permanent Deletion</th>
        <th colspan="2" style="width: 10%" />
      </tr>
    </thead>

    {#await refresh()}
      <tfoot class="info">
        <tr>
          <td colspan="8">Retrieving list of students...</td>
        </tr>
      </tfoot>
    {:then}
      {#if students.length === 0}
        <tfoot class="info">
          <tr>
            <td colspan="8">No deleted student data found</td>
          </tr>
        </tfoot>
      {:else}
        <tbody>
          {#each students as student}
            <tr>
              <td>{student.firstName}</td>
              <td>{student.middleName}</td>
              <td>{student.lastName}</td>
              <td>{displayDate(student.dateOfBirth)}</td>
              <td>{displayDate(student.deletedAt)}</td>
              <td>{displayDate(student.permanentDeletionDate)}</td>
              <td>
                <Button
                  color="success"
                  id={"restore" + student.id}
                  on:click={() => restoreStudent(student.id)}
                >
                  <Icon name="arrow-counterclockwise" />
                </Button>
                <Tooltip target={"restore" + student.id} placement="top">
                  Restore {student.lastName}, {student.firstName}
                </Tooltip>
              </td>
              <td>
                <Button
                  color="danger"
                  id={"delete" + student.id}
                  on:click={() => permanentlyDeleteStudent(student.id)}
                >
                  <Icon name="trash" />
                </Button>
                <Tooltip target={"delete" + student.id} placement="top">
                  Permanently Delete {student.lastName}, {student.firstName}
                </Tooltip>
              </td>
            </tr>
          {/each}
        </tbody>
      {/if}
    {:catch}
      <tfoot class="info">
        <tr>
          <td colspan="8">Could not retrieve list of students!</td>
        </tr>
      </tfoot>
    {/await}
  </Table>

  <h2>Staff List</h2>

  <Table id="staffTable">
    <thead>
      <tr>
        <th style="width: 15%">First Name</th>
        <th style="width: 15%">Middle Name</th>
        <th style="width: 15%">Last Name</th>
        <th style="width: 15%">Job Title</th>
        <th style="width: 15%">Deleted on</th>
        <th style="width: 15%">Permanent Deletion</th>
        <th colspan="2" style="width: 10%" />
      </tr>
    </thead>

    {#await refresh()}
      <tfoot class="info">
        <tr>
          <td colspan="8">Retrieving list of staff...</td>
        </tr>
      </tfoot>
    {:then}
      {#if students.length === 0}
        <tfoot class="info">
          <tr>
            <td colspan="8">No deleted staff data found</td>
          </tr>
        </tfoot>
      {:else}
        <tbody>
          {#each staffList as staff}
            <tr>
              <td>{staff.firstName}</td>
              <td>{staff.middleName}</td>
              <td>{staff.lastName}</td>
              <td>{staff.jobTitle}</td>
              <td>{displayDate(staff.deletedAt)}</td>
              <td>{displayDate(staff.permanentDeletionDate)}</td>
              <td>
                <Button
                  color="success"
                  id={"restoreStaff" + staff.id}
                  on:click={() => restoreStaff(staff.id)}
                >
                  <Icon name="arrow-counterclockwise" />
                </Button>
                <Tooltip target={"restoreStaff" + staff.id} placement="top">
                  Restore {staff.lastName}, {staff.firstName}
                </Tooltip>
              </td>
              <td>
                <Button
                  color="danger"
                  id={"deleteStaff" + staff.id}
                  on:click={() => permanentlyDeleteStaff(staff.id)}
                >
                  <Icon name="trash" />
                </Button>
                <Tooltip target={"deleteStaff" + staff.id} placement="top">
                  Permanently Delete {staff.lastName}, {staff.firstName}
                </Tooltip>
              </td>
            </tr>
          {/each}
        </tbody>
      {/if}
    {:catch}
      <tfoot class="info">
        <tr>
          <td colspan="8">Could not retrieve list of staff!</td>
        </tr>
      </tfoot>
    {/await}
  </Table>

  <DeletedRecordsHelp bind:open={openHelp} />
</Container>

<style>
  /* Centre any footers displaying information */
  tfoot.info > tr > td {
    text-align: center;
  }
</style>
