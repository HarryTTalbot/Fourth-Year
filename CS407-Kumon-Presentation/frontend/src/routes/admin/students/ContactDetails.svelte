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
  import { ContactsApi, StudentsApi } from "kumon_app_backend_api";

  import StudentForm from "../forms/StudentForm.svelte";
  import AddressDisplay from "../../../utils/displayAddress.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import AddContactModal from "./modals/AddContactModal.svelte";
  import EditContactModal from "./modals/EditContactModal.svelte";
  import ManageStudentsModal from "./modals/ManageStudentsModal.svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";
  import { createEventDispatcher } from "svelte";

  /**
   * The students API instance currently in use.
   * @type {StudentsApi}
   */
  let studentsApi = new StudentsApi(API_CONFIG);

  /**
   * The contacts API instance currently in use.
   * @type {ContactsApi}
   */
  let contactsApi = new ContactsApi(API_CONFIG);

  const dispatch = createEventDispatcher();

  /**
   * The ID of the contact currently being edited.
   * @type {number}
   */
  export let contactId;

  /**
   * The details of the student currently being edited.
   * @type {details} matches the student API endpoint
   */
  let studentInfo;

  /**
   * List of students associated with the chosen student
   */
  let students = [];

  /**
   * The ID of the contact currently being edited.
   * @type {number}
   */
  let openStudent;

  /**
   * The details of the contact currently being edited.
   * @type {details} matches the contact API endpoint
   */
  let contactInfo;

  /**
   * Refreshes the list of students.
   */
  async function getContactInfo() {
    try {
      contactInfo = await contactsApi.contactsRetrieve({ id: contactId });
      students = await contactsApi.contactsGetStudentsList({ id: contactId });
    } catch (e) {
      openModal(InfoModal, {
        title: "View contact details",
        message: `Could not load details for contact ${contactId}!`,
      });
    }
  }

  /**
   * Handler for editing a student.
   * @param {number} id The ID of the student.
   */
  async function handleEditContact() {
    openModal(EditContactModal, {
      id: contactId,
      onChangesSaved: (newDetails) => {
        dispatch("edit", { contactId: contactId, newDetails: newDetails });
        contactInfo = newDetails;
      },
    });
  }

  /**
   * Handler for editing a student.
   * @param {number} id The ID of the student.
   */
  function handleStudentContacts() {
    openModal(ManageStudentsModal, {
      id: contactId,
      onClose: (newList) => {
        students = newList;
        openStudent = undefined;
      },
    });
  }

  /**
   * Handler for removing a student.
   * @param {number} id The ID of the student.
   */
  async function handleRemoveContact() {
    let contact = await contactsApi.contactsRetrieve({ id: contactId });
    let confirmationMessage =
      "Are you sure you want to delete this contact?\n\n" +
      "Name: " +
      contact.firstName +
      " " +
      contact.lastName +
      "\nID: " +
      contact.id;

    openModal(ConfirmationModal, {
      title: "Delete Contact",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        try {
          contactsApi.contactsDestroy({ id: contactId }).then((_) => {
            // Remove this contact from the displayed list
            dispatch("delete", { contactId: contactId });

            // Second object is needed to "replace" the confirmation modal (otherwise it will re-open)
            openModal(
              InfoModal,
              {
                title: "Delete Contact",
                message: `Deleted contact ${id}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          openModal(
            InfoModal,
            {
              title: "Delete Contact",
              message: `Could not mark contact ${id} for deletion!`,
            },
            { replace: true }
          );
        }
      },
    });
  }

  async function handleViewStudent() {
    try {
      studentInfo = undefined;
      // Wait for any other API requests to complete
      await tick();
      studentInfo = await studentsApi.studentsRetrieve({ id: openStudent });
    } catch (e) {
      openModal(InfoModal, {
        title: "View student details",
        message: `Could not load details for student ${openStudent}!`,
      });
    }
  }

  function close() {
    dispatch("close");
  }
</script>

<Card>
  {#await getContactInfo()}
    <p>Fetching Contact Data ....</p>
  {:then}
    <CardHeader>
      <Row>
        <Col xs="auto">
          <h3>{contactInfo.lastName}, {contactInfo.firstName}</h3>
        </Col>
        <Col>
          <Button
            color="danger"
            id="deleteContact"
            on:click={() => handleRemoveContact()}
          >
            <Icon name="trash" />
          </Button>
          <Tooltip target="deleteContact" placement="top">
            Delete Contact
          </Tooltip>
        </Col>
        <Col>
          <Button
            outline
            color="secondary"
            id="closeContact"
            style="float: right;"
            on:click={() => close()}
          >
            <Icon name="x" />
          </Button>
          <Tooltip target="closeContact" placement="top">
            Close Contact Details
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
                id="editContact"
                on:click={() => handleEditContact()}
              >
                <Icon name="pen" />
              </Button>
              <Tooltip target="editContact" placement="top">
                Edit Contact Details
              </Tooltip>
            </Col>
          </Row>

          <p class="spacing">
            <b> First Name: </b>
            {contactInfo.firstName} <br />
            {#if contactInfo.middleName}
              <b> Middle Name: </b> {contactInfo.middleName} <br />
            {:else}
              <b> Middle Name: </b> n/a <br />
            {/if}
            <b> Last Name: </b>
            {contactInfo.lastName} <br />

            {#if contactInfo.phoneHome}
              <b> Home Telephone Number: </b> {contactInfo.phoneHome} <br />
            {/if}
            {#if contactInfo.phoneBusiness}
              <b> Business Telephone Number: </b>
              {contactInfo.phoneBusiness} <br />
            {/if}
            {#if contactInfo.phoneMobile}
              <b> Mobile Telephone Number: </b> {contactInfo.phoneMobile} <br />
            {/if}
            <b> Email Address: </b>
            {contactInfo.email} <br />

            <b> Address: </b> <br />
            <AddressDisplay address={contactInfo.address} />
          </p>
        </Col>
        <Col>
          <Row>
            <Col xs="auto">
              <h5>Associated Students</h5>
            </Col>

            <Col>
              <Button
                color="primary"
                id="manageStudents"
                on:click={() => handleStudentContacts()}
              >
                <Icon name="pen" />
              </Button>
              <Tooltip target="manageStudents" placement="top">
                Manage Associated Students
              </Tooltip>
            </Col>
          </Row>

          <p class="spacing">
            {contactInfo.firstName} has {students.length} associated students(s)
            <br />
            {#if students.length > 0}
              Choose one to view their details: <br />
              <Input
                id="contact"
                type="select"
                bind:value={openStudent}
                on:change={handleViewStudent}
              >
                {#each students as student}
                  <option value={student.studentId.id}
                    >{student.studentId.lastName}, {student.studentId.firstName}
                    - {student.relationship}</option
                  >
                {/each}
              </Input>
            {/if}
          </p>

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
