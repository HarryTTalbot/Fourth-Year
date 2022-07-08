<script>
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
  import { tick } from "svelte";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";
  import API_CONFIG from "../../../api";
  import { LongTermAbsenceApi } from "kumon_app_backend_api";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../../components/PaginationFilteringBar.svelte";

  import AbsenceForm from "../forms/LongTermForm.svelte";

  import InfoModal from "../../../modals/InfoModal.svelte";
  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import AddLongTermModal from "./modals/AddLongTermModal.svelte";

  import LongTermDetails from "./LongTermDetails.svelte";
  import LongTermHelp from "./LongTermHelp.svelte";

  let absenceApi = new LongTermAbsenceApi(API_CONFIG); // Link to the backend api

  let absencesList = [];
  let currentID = null;
  let absenceForm;
  let openHelp = false;

  let pageFilterDetails = new PageFilter();

  async function refreshAbsences() {
    try {
      // Query the Backend with the page and search filter
      let response = await absenceApi.longTermAbsenceList({
        page: pageFilterDetails.page,
        search: pageFilterDetails.filter,
      });

      // Save the list of staff and the total number of staff
      absencesList = response.results;

      // Update list with pagination and filtering
      pageFilterDetails.pageUpdate(response);
      pageFilterDetails.filter += " ";
      pageFilterDetails.filter = pageFilterDetails.filter.substring(
        0,
        pageFilterDetails.filter.length - 1
      );
    } catch (e) {}
  }

  function handleOpenCreate() {
    openModal(AddLongTermModal, {
      onAdd: async (_) => {
        await refreshAbsences();
      },
    });
  }

  async function handleViewAbsence(id) {
    if (currentID === id) {
      currentID = undefined;
    } else {
      currentID = undefined;
      await tick();
      currentID = id;
    }
  }

  async function handleEdit(event) {
    await refreshAbsences();
    await tick();
  }

  async function handleDelete(event) {
    currentID = undefined;
    await refreshAbsences();
    await tick();
  }

  async function handleCloseView() {
    currentID = undefined;
    await tick();
  }
</script>

<!-- Content of the page -->
<Container class="p-3">
  <Row>
    <Col>
      <h1>Long Term Absences</h1>
    </Col>

    <Col>
      <Button
        id="helpLongTerm"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpLongTerm" placement="top">
        User Guide for Long Term Absences Manager
      </Tooltip>
    </Col>
  </Row>

  <div>
    <Row>
      <Col>
        <h2>Existing Long Term Absences</h2>
      </Col>
      <Col>
        <Button
          id="addAbsence"
          color="success"
          style="float: right;"
          on:click={() => handleOpenCreate()}
        >
          <Icon name="plus-square" />
        </Button>
        <Tooltip target="addAbsence" placement="top">
          Add a New Long Term Absence
        </Tooltip>
      </Col>
    </Row>
    <PaginationFilteringBar
      refresh={() => refreshAbsences()}
      pageFilter={pageFilterDetails}
    />
    <Table>
      <!-- Absences Table Headings -->
      <thead>
        <tr>
          <th style="width: 15%">First Name</th>
          <th style="width: 15%">Last Name</th>
          <th style="width: 15%">Start</th>
          <th style="width: 15%">End</th>
          <th style="width: 40%">Reason</th>
        </tr>
      </thead>

      {#await refreshAbsences()}
        <!-- Whilst waiting for backend response -->
        <tfoot class="info">
          <tr>
            <td colspan="6">Retrieving list of absences...</td>
          </tr>
        </tfoot>
      {:then}
        {#if absencesList.length === 0}
          <!-- If no staff are returned -->
          <tfoot class="info">
            <tr>
              <td colspan="6">No absence data found</td>
            </tr>
          </tfoot>
        {:else}
          <!-- If staff are returned -->
          <tbody>
            <!-- Display information about each long term absence in the table -->
            {#each absencesList as absence}
              <tr
                class:selected={currentID === absence.id}
                on:click={() => handleViewAbsence(absence.id)}
              >
                <td>{absence.student.firstName}</td>
                <td>{absence.student.lastName}</td>
                <td>{displayDate(absence.startDate)}</td>
                <td>{displayDate(absence.endDate)}</td>
                <td>{absence.reason}</td>
              </tr>
            {/each}
          </tbody>
        {/if}
      {:catch}
        <!-- If an error is returned -->
        <tfoot class="info">
          <tr>
            <td colspan="6">Could not retrieve list of absences!</td>
          </tr>
        </tfoot>
      {/await}
    </Table>
  </div>

  {#if currentID}
    <LongTermDetails
      longTermId={currentID}
      on:edit={handleEdit}
      on:delete={handleDelete}
      on:close={handleCloseView}
    />
  {/if}

  <LongTermHelp bind:open={openHelp} />
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
