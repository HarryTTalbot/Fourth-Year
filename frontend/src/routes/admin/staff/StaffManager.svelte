<script>
  import dayjs from "dayjs";
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
    Icon,
    Tooltip,
  } from "sveltestrap";
  import { tick } from "svelte";

  import API_CONFIG from "../../../api";
  import { StaffApi } from "kumon_app_backend_api";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../../components/PaginationFilteringBar.svelte";

  import InfoModal from "../../../modals/InfoModal.svelte";
  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import AddStaffModal from "./modals/AddStaffModal.svelte";
  import NewAccount from "../../authentication/NewAccount.svelte";

  import StaffDetails from "./StaffDetails.svelte";
  import StaffHelp from "./StaffHelp.svelte";

  // Variables needed in the page
  let staffApi = new StaffApi(API_CONFIG); // Link to the backend api
  let staffList = []; // List of staff currently on display
  let currentID; // The current staff member being viewed
  let openHelp = false;

  let pageFilterDetails = new PageFilter();

  // Function to refresh the list of staff
  async function refreshStaff() {
    try {
      // Query the Backend with the page and search filter
      let response = await staffApi.staffList({
        page: pageFilterDetails.page,
        search: pageFilterDetails.filter,
      });

      // Save the list of staff and the total number of staff
      staffList = response.results;

      pageFilterDetails.pageUpdate(response);
      pageFilterDetails.filter += " ";
      pageFilterDetails.filter = pageFilterDetails.filter.substring(
        0,
        pageFilterDetails.filter.length - 1
      );
    } catch (e) {
      // If there is an error throw an exception
      throw e;
    }
  }

  // Function to open the details of a staff member
  async function handleViewStaff(id) {
    if (currentID === id) {
      currentID = undefined;
    } else {
      currentID = undefined;
      await tick();
      currentID = id;
    }
  }

  // Function to open the create new staff form
  async function openCreateForm() {
    openModal(AddStaffModal, {
      onStaffAdd: async () => {
        // Refresh the staff list
        await refreshStaff();
      },
    });
  }

  function handleEdit(event) {
    let existingIndex = staffList.findIndex(
      (staff) => staff.id === event.detail.staffId
    );

    if (existingIndex >= 0) {
      staffList[existingIndex] = {
        id: event.detail.staffId,
        firstName: event.detail.newDetails.firstName,
        middleName: event.detail.newDetails.middleName,
        lastName: event.detail.newDetails.lastName,
        jobTitle: event.detail.newDetails.jobTitle,
      };
    }
  }

  async function handleDelete(event) {
    currentID = undefined;
    await refreshStaff();
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
      <h1>Staff Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpStaff"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpStaff" placement="top">
        User Guide for Staff Manager
      </Tooltip>
    </Col>
  </Row>
  <Row>
    <Col>
      <h2>Staff List</h2>
    </Col>

    <Col>
      <Button
        id="addStaff"
        color="success"
        style="float: right;"
        on:click={() => openCreateForm()}
      >
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addStaff" placement="top">
        Add a New Staff Member
      </Tooltip>
    </Col>
  </Row>

  <!-- List of all staff component of the page -->
  <PaginationFilteringBar
    refresh={() => refreshStaff()}
    pageFilter={pageFilterDetails}
  />
  <Table class="table">
    <!-- Staff Table Headings -->
    <thead>
      <tr>
        <th style="width: 25%">First Name</th>
        <th style="width: 25%">Middle Name</th>
        <th style="width: 25%">Last Name</th>
        <th style="width: 25%">Job Title</th>
      </tr>
    </thead>

    {#await refreshStaff()}
      <!-- Whilst waiting for backend response -->
      <tfoot class="info">
        <tr>
          <td colspan="6">Retrieving list of staff...</td>
        </tr>
      </tfoot>
    {:then}
      {#if staffList.length === 0}
        <!-- If no staff are returned -->
        <tfoot class="info">
          <tr>
            <td colspan="6">No staff data found</td>
          </tr>
        </tfoot>
      {:else}
        <!-- If staff are returned -->
        <tbody>
          {#each staffList as staff}
            <tr
              class:selected={currentID === staff.id}
              on:click={() => handleViewStaff(staff.id)}
            >
              <td>{staff.firstName}</td>
              <td>{staff.middleName}</td>
              <td>{staff.lastName}</td>
              <td>{staff.jobTitle}</td>
            </tr>
          {/each}
        </tbody>
      {/if}
    {:catch}
      <!-- If an error is returned -->
      <tfoot class="info">
        <tr>
          <td colspan="6">Could not retrieve list of staff!</td>
        </tr>
      </tfoot>
    {/await}
  </Table>

  {#if currentID}
    <StaffDetails
      staffId={currentID}
      on:edit={handleEdit}
      on:delete={handleDelete}
      on:close={handleCloseView}
    />
  {/if}

  <StaffHelp bind:open={openHelp} />
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
