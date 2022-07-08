<script>
  import { openModal } from "svelte-modals";
  import {
    Button,
    Container,
    Table,
    Row,
    Col,
    Icon,
    Tooltip,
  } from "sveltestrap";

  import API_CONFIG from "../../../api";
  import { ClassesApi } from "kumon_app_backend_api";
  import { tick } from "svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import AddClassModal from "./modals/AddClassModal.svelte";
  import EditClassModal from "./modals/EditClassModal.svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../../components/PaginationFilteringBar.svelte";

  import ClassDetails from "./ClassDetails.svelte";
  import ClassHelp from "./ClassesHelp.svelte";

  let classApi = new ClassesApi(API_CONFIG);
  let classes = [];
  let selectedClass;
  let pageFilterDetails = new PageFilter();
  let openHelp = false;

  async function refreshClasses() {
    try {
      // Get class information from backend
      let response = await classApi.classesList({
        page: pageFilterDetails.page,
        search: pageFilterDetails.filter,
      });
      classes = response.results;

      // Update list with pagination and filtering
      pageFilterDetails.pageUpdate(response);
      pageFilterDetails.filter += " ";
      pageFilterDetails.filter = pageFilterDetails.filter.substring(
        0,
        pageFilterDetails.filter.length - 1
      );
    } catch (e) {}
  }

  /**
   * Handler for adding a new class.
   */
  function handleAddClass() {
    openModal(AddClassModal, {
      onClassAdd: async () => {
        await refreshClasses();
      },
    });
  }

  async function handleViewClassDetails(id) {
    if (selectedClass === id) {
      selectedClass = undefined;
    } else {
      selectedClass = undefined;
      await tick();
      selectedClass = id;
    }
  }

  async function handleEdit(event) {
    await refreshClasses();
    await tick();
  }

  async function handleDelete(event) {
    selectedClass = undefined;
    await refreshClasses();
    await tick();
  }

  async function handleCloseView() {
    selectedClass = undefined;
    await tick();
  }
</script>

<Container class="p-3">
  <!-- Ideally we want the have the upcoming and previous classes available -->
  <Row>
    <Col>
      <h1>Class Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpClass"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpClass" placement="top">
        User Guide for Class Manager
      </Tooltip>
    </Col>
  </Row>
  <Row>
    <Col>
      <h2>Class List</h2>
    </Col>

    <Col>
      <Button
        id="addClass"
        color="success"
        style="float: right;"
        on:click={() => handleAddClass()}
      >
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addClass" placement="top">Add a New Class</Tooltip>
    </Col>
  </Row>

  <PaginationFilteringBar
    refresh={() => refreshClasses()}
    pageFilter={pageFilterDetails}
  />
  <Table>
    <thead>
      <tr>
        <th style="width: 50%">Class Name</th>
        <th style="width: 50%">Class Size</th>
      </tr>
    </thead>

    {#await refreshClasses()}
      <tfoot class="info">
        <td colspan="3">Retrieving list of classes...</td>
      </tfoot>
    {:then}
      {#if classes.length === 0}
        <tfoot class="info">
          <td colspan="3">No class data found</td>
        </tfoot>
      {:else}
        <tbody>
          {#each classes as cls}
            <tr
              class:selected={selectedClass === cls.id}
              on:click={() => handleViewClassDetails(cls.id)}
            >
              <td>{cls.name}</td>
              <td>{cls.size}</td>
            </tr>
          {/each}
        </tbody>
      {/if}
    {:catch}
      <tfoot class="info">
        <td colspan="3">Could not retrieve list of classes!</td>
      </tfoot>
    {/await}
  </Table>

  {#if selectedClass}
    <ClassDetails
      classId={selectedClass}
      on:edit={handleEdit}
      on:delete={handleDelete}
      on:close={handleCloseView}
    />
  {/if}

  <ClassHelp bind:open={openHelp} />
</Container>

<style>
  /* Centre any footers displaying information */
  .selected {
    background-color: #6c757d;
    color: white;
  }
  tbody tr:hover {
    background-color: #6c757d;
    color: white;
  }
</style>
