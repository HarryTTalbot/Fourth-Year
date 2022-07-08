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
  import { LongTermAbsenceApi } from "kumon_app_backend_api";
  import AddressDisplay from "../../../utils/displayAddress.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import EditLongTermModal from "./modals/EditLongTermModal.svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";
  import { createEventDispatcher } from "svelte";

  let absenceApi = new LongTermAbsenceApi(API_CONFIG);

  const dispatch = createEventDispatcher();

  export let longTermId;

  let longTermInfo;

  /**
   * Refreshes the list of students.
   */
  async function getLongTermInfo() {
    try {
      longTermInfo = await absenceApi.longTermAbsenceRetrieve({
        id: longTermId,
      });
    } catch (e) {
      console.log(e);
      throw e;
    }
  }

  /**
   * Handler for editing a student.
   * @param {number} id The ID of the student.
   */
  async function handleEditLongTerm() {
    openModal(EditLongTermModal, {
      id: longTermId,
      onChangesSaved: async (newDetails) => {
        dispatch("edit", { longTermId: longTermId, newDetails: newDetails });
        await getLongTermInfo();
      },
    });
  }

  /**
   * Handler for removing a student.
   * @param {number} id The ID of the student.
   */
  async function handleRemoveLongTerm() {
    // Query the backend to get the long term absence details (as they are in the database)
    let absence = await absenceApi.longTermAbsenceRetrieve({ id: longTermId });

    // Formulate a confirmation message to the user
    let confirmationMessage =
      "Are you sure you want to delete this long term absence?\n\n" +
      "Name: " +
      absence.student.firstName +
      " " +
      absence.student.lastName;

    // Open a confirmation modal to ask the user to confirm the deletion
    openModal(ConfirmationModal, {
      title: "Delete Long Term Absence",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        // If the user confirms the deletion
        try {
          // Query the backend to remove the absence (uses Promise API)
          absenceApi.longTermAbsenceDestroy({ id: absence.id }).then((_) => {
            // Remove this student from the displayed list
            dispatch("delete", { longTermId: longTermId });

            // Open a modal to inform the user that the absence has been removed
            openModal(
              InfoModal,
              {
                title: "Delete Long Term Absence",
                message: `Deleted long term absence ${absence.student.firstName} ${absence.student.lastName}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          // Open a modal to inform the user that the deletion has been unsuccessful
          openModal(
            InfoModal,
            {
              title: "Delete Long Term Absence",
              message: `Could not mark ${absence.student.firstName} ${absence.student.lastName} for deletion!`,
            },
            { replace: true }
          );
        }
      },
    });
  }

  function close() {
    dispatch("close");
  }
</script>

<Card>
  {#await getLongTermInfo()}
    <p>Fetching Long Term Absence Data ....</p>
  {:then}
    <CardHeader>
      <Row>
        <Col xs="auto">
          <h3>Long Term Absence Details</h3>
        </Col>
        <Col>
          <Button
            color="danger"
            id="deleteLongTerm"
            on:click={() => handleRemoveLongTerm()}
          >
            <Icon name="trash" />
          </Button>
          <Tooltip target="deleteLongTerm" placement="top">
            Delete Long Term Absence
          </Tooltip>
        </Col>
        <Col>
          <Button
            outline
            color="secondary"
            id="closeLongTerm"
            style="float: right;"
            on:click={() => close()}
          >
            <Icon name="x" />
          </Button>
          <Tooltip target="closeLongTerm" placement="top">
            Close Long Term Absence Details
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
            id="editLongTerm"
            on:click={() => handleEditLongTerm()}
          >
            <Icon name="pen" />
          </Button>
          <Tooltip target="editLongTerm" placement="top">
            Edit Long Term Absence Details
          </Tooltip>
        </Col>
      </Row>

      <Row>
        <Col>
          <p class="spacing">
            <b> Start Date: </b>
            {displayDate(longTermInfo.startDate)} <br />

            <b> End Date: </b>
            {displayDate(longTermInfo.endDate)} <br />

            <b> Reason: </b>
            {longTermInfo.reason} <br />
          </p>
        </Col>

        <Col>
          <p class="spacing">
            <b> First Name: </b>
            {longTermInfo.student.firstName} <br />
            {#if longTermInfo.student.middleName}
              <b> Middle Name: </b> {longTermInfo.student.middleName} <br />
            {:else}
              <b> Middle Name: </b> n/a <br />
            {/if}
            <b> Last Name: </b>
            {longTermInfo.student.lastName} <br />

            <b> Date of Birth: </b>
            {displayDate(longTermInfo.student.dateOfBirth)} <br />

            {#if longTermInfo.student.joinDate}
              <b> Join Date: </b>
              {displayDate(longTermInfo.student.joinDate)} <br />
            {:else}
              <b> Join Date: </b> n/a <br />
            {/if}
            {#if longTermInfo.student.leaveDate}
              <b> Leave Date: </b>
              {displayDate(longTermInfo.student.leaveDate)} <br />
            {:else}
              <b> Leave Date: </b> n/a <br />
            {/if}

            <b> School: </b>
            {longTermInfo.student.school} <br />
            <b> Grade: </b>
            {longTermInfo.student.grade} <br />

            <b> Telephone Number: </b>
            {longTermInfo.student.phoneNumber} <br />
            <b> Email Address: </b>
            {longTermInfo.student.email} <br />

            <b> Address: </b> <br />
            <AddressDisplay address={longTermInfo.student.address} />
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
