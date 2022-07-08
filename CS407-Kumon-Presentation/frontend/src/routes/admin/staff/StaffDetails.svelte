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
  import { StaffApi } from "kumon_app_backend_api";

  import AddressDisplay from "../../../utils/displayAddress.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import EditStaffModal from "./modals/EditStaffModal.svelte";
  import ForgotPassword from "../../authentication/ForgotPassword.svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";
  import { createEventDispatcher } from "svelte";

  import { FileDownloader } from "../../../utils";

  let staffApi = new StaffApi(API_CONFIG); // Link to the backend api
  const dispatch = createEventDispatcher();

  export let staffId;

  let staffInfo;

  /**
   * The file downloader helper instance we're using.
   * @type {FileDownloader}
   */
  export let fileDownloader = new FileDownloader();

  /**
   * Refreshes the list of students.
   */
  async function getStaffInfo() {
    try {
      staffInfo = await staffApi.staffRetrieve({ id: staffId });
    } catch (e) {
      throw e;
    }
  }

  /**
   * Handler for editing a student.
   * @param {number} id The ID of the student.
   */
  async function handleEditStaff() {
    openModal(EditStaffModal, {
      id: staffId,
      onStaffEdit: (newDetails) => {
        dispatch("edit", { staffId: staffId, newDetails: newDetails });
        staffInfo = newDetails;
      },
    });
  }

  async function handleRemoveStaff() {
    // Query the backend to get the staff details (as they are in the database)
    let staff = await staffApi.staffRetrieve({ id: staffId });

    // Formulate a confirmation message to the user
    let confirmationMessage =
      "Are you sure you want to delete this staff member?\n\n" +
      "Name: " +
      staff.firstName +
      " " +
      staff.lastName;

    // Open a confirmation modal to ask the user to confirm the deletion
    openModal(ConfirmationModal, {
      title: "Delete Staff",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        // If the user confirms the deletion
        try {
          // Query the backend to remove the staff member (uses Promise API)
          staffApi.staffGdprDeleteDestroy({ id: staff.id }).then((_) => {
            // Remove this student from the displayed list
            dispatch("delete", { staffId: staffId });

            // Open a modal to inform the user that the staff member has been removed
            openModal(
              InfoModal,
              {
                title: "Delete Staff",
                message: `Deleted staff ${staff.firstName} ${staff.lastName}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          // Open a modal to inform the user that the deletion has been unsuccessful
          openModal(
            InfoModal,
            {
              title: "Delete Staff",
              message: `Could not mark ${staff.firstName} ${staff.lastName} for deletion!`,
            },
            { replace: true }
          );
        }
      },
    });
  }

  function openForgotPassword() {
    openModal(ForgotPassword, {
      staffName: staffInfo.lastName + ", " + staffInfo.firstName,
      staffID: staffId,
    });
  }

  // Function to fetch a GDPR report for the selected staff member
  async function handleGDPRRequest() {
    try {
      let response = await staffApi.staffGetDataRetrieve({ id: staffId });

      let dateStr = dayjs().format("YYYY-MM-DD_HH-mm-ss");

      let filename =
        staffInfo.lastName +
        "-" +
        staffInfo.firstName +
        "-Staff-Data-report-" +
        dateStr +
        ".pdf";

      fileDownloader.downloadBlob(response, filename);
    } catch (e) {}
  }

  function close() {
    dispatch("close");
  }
</script>

<Card>
  {#await getStaffInfo()}
    <p>Fetching Staff Data ....</p>
  {:then}
    <CardHeader>
      <Row>
        <Col xs="auto">
          <h3>{staffInfo.lastName}, {staffInfo.firstName}</h3>
        </Col>
        <Col>
          <Button
            color="danger"
            id="deleteStaff"
            on:click={() => handleRemoveStaff()}
          >
            <Icon name="trash" />
          </Button>
          <Tooltip target="deleteStaff" placement="top">Delete Staff</Tooltip>

          <Button
            color="info"
            id="downloadStaff"
            on:click={() => handleGDPRRequest()}
          >
            <Icon name="download" />
          </Button>
          <Tooltip target="downloadStaff" placement="top">
            Download Staff Data Report
          </Tooltip>

          <Button
            color="warning"
            id="forgotPassword"
            on:click={() => openForgotPassword()}
          >
            <Icon name="question-square" />
          </Button>
          <Tooltip target="forgotPassword" placement="top">
            Forgot Password
          </Tooltip>
        </Col>
        <Col>
          <Button
            outline
            color="secondary"
            id="closeStaff"
            style="float: right;"
            on:click={() => close()}
          >
            <Icon name="x" />
          </Button>
          <Tooltip target="closeStaff" placement="top">
            Close Staff Details
          </Tooltip>
        </Col>
      </Row>
    </CardHeader>
    <CardBody>
      <Row>
        <Col xs="auto">
          <h5>Details</h5>
        </Col>
        <Col>
          <Button
            color="primary"
            id="editStaff"
            on:click={() => handleEditStaff()}
          >
            <Icon name="pen" />
          </Button>
          <Tooltip target="editStaff" placement="top">
            Edit Staff Details
          </Tooltip>
        </Col>
      </Row>

      <p class="spacing">
        <b> First Name: </b>
        {staffInfo.firstName} <br />
        {#if staffInfo.middleName}
          <b> Middle Name: </b> {staffInfo.middleName} <br />
        {:else}
          <b> Middle Name: </b> n/a <br />
        {/if}
        <b> Last Name: </b>
        {staffInfo.lastName} <br />

        <b> Job Title: </b>
        {staffInfo.jobTitle} <br />

        {#if staffInfo.joinDate}
          <b> Start Employment Date: </b>
          {displayDate(staffInfo.joinDate)} <br />
        {:else}
          <b> Start Employment Date: </b> n/a <br />
        {/if}
        {#if staffInfo.leaveDate}
          <b> End Employment Date: </b>
          {displayDate(staffInfo.leaveDate)} <br />
        {:else}
          <b> End Employment Date: </b> n/a <br />
        {/if}
      </p>
    </CardBody>
  {/await}
</Card>

<style>
  p.spacing {
    line-height: 1.5;
  }
</style>
