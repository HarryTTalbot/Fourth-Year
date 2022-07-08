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
  import AddStudentModal from "./modals/AddStudentModal.svelte";
  import AddContactModal from "./modals/AddContactModal.svelte";
  import EditStudentModal from "./modals/EditStudentModal.svelte";
  import ManageContactsModal from "./modals/ManageContactsModal.svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";
  import { createEventDispatcher } from "svelte";

  import { FileDownloader } from "../../../utils";

  /**
   * The students API instance in use.
   * @type {StudentsApi}
   */
  let studentsApi = new StudentsApi(API_CONFIG);

  /**
   * The contacts API instance in use.
   * @type {ContactsApi}
   */
  let contactsApi = new ContactsApi(API_CONFIG);

  const dispatch = createEventDispatcher();

  /**
   * The ID of the student currently being edited.
   * @type {number}
   */
  export let studentId;

  /**
   * The details of the student currently being viewed.
   * @param {details} studentinfo matches the api endpoint for students
   */
  let studentInfo;

  /**
   * List of contacts associated with the chosen student
   */
  let contacts = [];

  /**
   * List of classes the student is a member of
   */
  let classes = [];

  /**
   * The ID of the contact currently being viewed.
   * @type {number}
   */
  let openContact;

  /**
   * The details of the contact currently being viewed.
   * @param {details} contactInfo matches the api endpoint for contacts
   */
  let contactInfo;

  /**
   * The ID of the class currently being viewed.
   * @type {number}
   */
  let openClass;

  /**
   * The details of the class currently being viewed.
   * @param {details} classInfo matches the api endpoint for classes
   */
  let classInfo;

  /**
   * The file downloader helper instance we're using.
   * @type {FileDownloader}
   */
  export let fileDownloader = new FileDownloader();

  /**
   * Refreshes the list of students.
   */
  async function getStudentInfo() {
    try {
      studentInfo = await studentsApi.studentsRetrieve({ id: studentId });

      contacts = await studentsApi.studentsGetContactsList({ id: studentId });

      classes = await studentsApi.studentsGetClassesList({ id: studentId });
    } catch (e) {
      console.log(e);
      throw e;
    }
  }

  /**
   * Handler for editing a student.
   * @param {number} id The ID of the student.
   */
  async function handleEditStudent() {
    openModal(EditStudentModal, {
      id: studentId,
      onChangesSaved: (newDetails) => {
        dispatch("edit", { studentId: studentId, newDetails: newDetails });
        studentInfo = newDetails;
      },
    });
  }

  /**
   * Handler for editing a student.
   * @param {number} id The ID of the student.
   */
  function handleContactsStudent() {
    openModal(ManageContactsModal, {
      id: studentId,
      onClose: (newList) => {
        contacts = newList;
        openContact = undefined;
      },
    });
  }

  /**
   * Handler for removing a student.
   * @param {number} id The ID of the student.
   */
  async function handleRemoveStudent() {
    let student = await studentsApi.studentsRetrieve({ id: studentId });
    let confirmationMessage =
      "Are you sure you want to delete this student?\n\n" +
      "Name: " +
      studentInfo.firstName +
      " " +
      studentInfo.lastName +
      "\nID: " +
      studentInfo.id +
      "\nK-SIS ID: " +
      studentInfo.kSisId;

    openModal(ConfirmationModal, {
      title: "Delete Student",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        try {
          // NOTE: Promise API used here since using async in this context probably isn't a good idea...
          studentsApi.studentsGdprDeleteDestroy({ id: studentId }).then((_) => {
            // Remove this student from the displayed list
            dispatch("delete", { studentId: studentId });

            // NOTE: Second object is needed to "replace" the confirmation modal (otherwise it will re-open)
            openModal(
              InfoModal,
              {
                title: "Delete Student",
                message: `Deleted student ${studentId}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          openModal(
            InfoModal,
            {
              title: "Delete Student",
              message: `Could not mark student ${studentId} for deletion!`,
            },
            { replace: true }
          );
        }
      },
    });
  }

  /**
   * Function to fetch a GDPR report for the selected student
   */
  async function handleGDPRRequest() {
    try {
      let response = await studentsApi.studentsGetDataRetrieve({
        id: studentId,
      });
      // Explicit format necessary to match the backend schema
      let dateStr = dayjs().format("YYYY-MM-DD_HH-mm-ss");
      // generates a filename automaticaloly based on the student
      let filename =
        studentInfo.lastName +
        "-" +
        studentInfo.firstName +
        "-Student-Data-report-" +
        dateStr +
        ".pdf";

      fileDownloader.downloadBlob(response, filename);
    } catch (e) {
      openModal(
        InfoModal,
        {
          title: "Report Generator",
          message: `Could not create a report for student ${studentId}!`,
        },
        { replace: true }
      );
    }
  }

  /**
   * Function to view a contact
   */
  async function handleViewContact() {
    try {
      contactInfo = undefined;
      await tick();
      contactInfo = await contactsApi.contactsRetrieve({ id: openContact });
    } catch (e) {
      console.log(e);
    }
  }

  function close() {
    dispatch("close");
  }
</script>

<Card>
  {#await getStudentInfo()}
    <p>Fetching Student Data ....</p>
  {:then}
    <CardHeader>
      <Row>
        <Col xs="auto">
          <h3>{studentInfo.lastName}, {studentInfo.firstName}</h3>
        </Col>
        <Col>
          <Button
            color="danger"
            id="deleteStudent"
            on:click={() => handleRemoveStudent()}
          >
            <Icon name="trash" />
          </Button>
          <Tooltip target="deleteStudent" placement="top">
            Delete Student
          </Tooltip>

          <Button
            color="info"
            id="downloadStudent"
            on:click={() => handleGDPRRequest()}
          >
            <Icon name="download" />
          </Button>
          <Tooltip target="downloadStudent" placement="top">
            Download Student Data Report
          </Tooltip>
        </Col>
        <Col>
          <Button
            outline
            color="secondary"
            id="closeStudent"
            style="float: right;"
            on:click={() => close()}
          >
            <Icon name="x" />
          </Button>
          <Tooltip target="closeStudent" placement="top">
            Close Student Details
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
                id="editStudent"
                on:click={() => handleEditStudent()}
              >
                <Icon name="pen" />
              </Button>
              <Tooltip target="editStudent" placement="top">
                Edit Student Details
              </Tooltip>
            </Col>
          </Row>

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
        </Col>
        <Col>
          <Row>
            <Col xs="auto">
              <h5>Contacts</h5>
            </Col>

            <Col>
              <Button
                color="primary"
                id="manageContacts"
                on:click={() => handleContactsStudent()}
              >
                <Icon name="pen" />
              </Button>
              <Tooltip target="manageContacts" placement="top">
                Manage Student Contacts
              </Tooltip>
            </Col>
          </Row>

          <p class="spacing">
            {studentInfo.firstName} has {contacts.length} associated contact(s)
            <br />
            {#if contacts.length > 0}
              Choose one to view their details: <br />
              <Input
                id="contact"
                type="select"
                bind:value={openContact}
                on:change={handleViewContact}
              >
                {#each contacts as contact}
                  <option value={contact.contactId.id}
                    >{contact.contactId.lastName}, {contact.contactId.firstName}
                    - {contact.relationship}</option
                  >
                {/each}
              </Input>
            {/if}
          </p>

          {#if contactInfo}
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
                <b> Mobile Telephone Number: </b>
                {contactInfo.phoneMobile} <br />
              {/if}
              <b> Email Address: </b>
              {contactInfo.email} <br />

              <b> Address: </b> <br />
              <AddressDisplay address={contactInfo.address} />
            </p>
          {/if}

          <h5>Classes</h5>

          <p class="spacing">
            {studentInfo.firstName} is in {classes.length} classes <br />
            {#if classes.length > 0}
              Below is a list of the classes: <br />
              <ul>
                {#each classes as cls}
                  <li>{cls.name}</li>
                {/each}
              </ul>
            {/if}
          </p>
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
