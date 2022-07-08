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
    Icon,
    Tooltip,
  } from "sveltestrap";
  import { tick } from "svelte";
  import { push } from "svelte-spa-router";
  import { displayDate, displayTime } from "../../utils/displayDateTime";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../components/PaginationFilteringBar.svelte";

  import orderModal from "./modals/orderModal.svelte";
  import InfoModal from "./modals/InfoModal.svelte";
  import EditWorksheetModal from "./modals/EditWorksheetModal.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "./modals/ConfirmationModal.svelte";

  import AddWorksheetModal from "./modals/AddWorksheetModal.svelte";

  import WorksheetHelp from "./WorksheetHelp.svelte";

  import API_CONFIG from "../../api";
  import { WorksheetApi } from "kumon_app_backend_api";

  /**
   * The worksheet API client instance we're using.
   * @type {WorksheetApi}
   */
  let worksheetApi = new WorksheetApi(API_CONFIG);

  let pageFilterDetailsWorksheets = new PageFilter();
  let worksheetsList = [];
  let openHelp = false;

  var today = new Date();

  /**
   * Refreshes the list of worksheets.
   */
  async function refreshWorksheets() {
    try {
      // Send a request to the backend for the list of worksheets
      let response = await worksheetApi.worksheetList({
        page: pageFilterDetailsWorksheets.page,
        search: pageFilterDetailsWorksheets.filter,
      });
      // Update local worksheets list with the result of the request
      worksheetsList = response.results;

      // Updates the filter based on the current view
      pageFilterDetailsWorksheets.pageUpdate(response);
      pageFilterDetailsWorksheets.filter += " ";
      pageFilterDetailsWorksheets.filter =
        pageFilterDetailsWorksheets.filter.substring(
          0,
          pageFilterDetailsWorksheets.filter.length - 1
        );
    } catch (e) {
      // Inform the user the system could not load the worksheet list
      openModal(InfoModal, {
        title: "Worksheet List",
        message: "Could not load worksheet list!",
      });
    }
  }

  /**
   * Handler for ordering a worksheet
   * @param {number} id The ID of the worksheet.
   */
  async function handleOrderWorksheet(id) {
    // Opens the modal for ordering the specified worksheet
    openModal(orderModal, {
      id: id,
      onChangesSaved: async (_) => {
        await refreshWorksheets();
      },
    });
  }

  /**
   * Handler for editing a worksheet
   * @param {number} id The ID of the worksheet.
   */
  function handleEditWorksheet(id) {
    // opens the modal for editing the worksheet
    openModal(EditWorksheetModal, {
      id: id,
      // When the changes are saved (form submitted)
      onChangesSaved: async (_) => {
        await refreshWorksheets();
      },
    });
  }

  /**
   * Handler for adding a new worksheet
   */
  function handleAddWorksheet() {
    // Open the add worksheet modal
    openModal(AddWorksheetModal, {
      // When the form is submitted, refresh the list of worksheets
      onAdd: async (_) => {
        await refreshWorksheets();
      },
    });
  }

  /**
   * Handler for removing a worksheet.
   * @param {number} id The ID of the worksheet.
   */
  async function handleDeleteItem(id) {
    // Retrive information about worksheet
    let worksheet = await worksheetApi.worksheetRetrieve({ id: id });

    // Creates a confirmation message using the worksheet details
    let confirmationMessage =
      "Are you sure you want to delete this worksheet?\n\n" +
      "Subject: " +
      worksheet.subject.name +
      "\nLevel: " +
      worksheet.subjectLevel.name +
      "\nSet: " +
      worksheet.set;

    // Opens a confirmation modal that must be accepted to continue
    openModal(ConfirmationModal, {
      title: "Delete Worksheet",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        try {
          // Deletes the specified worksheet
          worksheetApi.worksheetDestroy({ id: id }).then((_) => {
            // Remove this worksheet from the displayed list
            worksheetsList = worksheetsList.filter(
              (worksheet) => worksheet.id !== id
            );

            // Second object is needed to "replace" the confirmation modal (otherwise it will re-open)
            openModal(
              InfoModal,
              {
                title: "Delete Worksheet",
                message: `Deleted Worksheet ${id}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          openModal(
            InfoModal,
            {
              title: "Delete Worksheet",
              message: `Could not delete worksheet ${id}!`,
            },
            { replace: true }
          );
        }
      },
    });
  }
</script>

<!-- Content of the page -->
<Container class="p-3">
  <Row>
    <Col>
      <h1>Worksheet Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpWorksheet"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpWorksheet" placement="top">
        User Guide for Worksheet Manager
      </Tooltip>
    </Col>
  </Row>
  <Row>
    <Col>
      <h2>Worksheet List</h2>
    </Col>

    <Col>
      <Button
        id="addWorksheet"
        color="success"
        style="float: right;"
        on:click={() => handleAddWorksheet()}
      >
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addWorksheet" placement="top">
        Add a New Worksheet
      </Tooltip>
    </Col>
  </Row>

  <PaginationFilteringBar
    refresh={() => refreshWorksheets()}
    pageFilter={pageFilterDetailsWorksheets}
  />

  <Table>
    <thead>
      <tr>
        <th>Subject</th>
        <th>Subject Level</th>
        <th>Set</th>
        <th>Quantity</th>
        <th>Edit</th>
        <th>Order</th>
        <th>Delete</th>
      </tr>
    </thead>
    {#await refreshWorksheets()}
      <tfoot class="info">
        <tr>
          <td colspan="7">Retrieving list of worksheets...</td>
        </tr>
      </tfoot>
    {:then}
      {#if worksheetsList.length === 0}
        <tfoot class="info">
          <tr>
            <td colspan="7">No worksheet data found</td>
          </tr>
        </tfoot>
      {:else}
        <tbody>
          {#each worksheetsList as worksheet}
            <tr>
              <td>{worksheet.subject.name}</td>
              <td>{worksheet.subjectLevel.name}</td>
              <td>{worksheet.set}</td>
              <td>{worksheet.quantity}</td>

              <!-- Buttons are contained within the same table -->
              <td>
                <Button
                  color="primary"
                  id="editWorksheet"
                  on:click={() => handleEditWorksheet(worksheet.id)}
                >
                  <Icon name="pen" />
                </Button>
                <Tooltip target="editWorksheet" placement="top">
                  Edit Worksheet Details
                </Tooltip>
              </td>

              <td>
                <Button
                  color="primary"
                  on:click={() => handleOrderWorksheet(worksheet.id)}
                >
                  Order
                </Button>
              </td>

              <td>
                <Button
                  color="danger"
                  id="deleteWorksheet"
                  on:click={() => handleDeleteItem(worksheet.id)}
                >
                  <Icon name="trash" />
                </Button>
                <Tooltip target="deleteWorksheet" placement="top">
                  Delete Worksheet
                </Tooltip>
              </td>
            </tr>
          {/each}
        </tbody>
      {/if}
    {:catch}
      <tfoot class="info">
        <tr>
          <td colspan="6">Could not retrieve list of worksheets!</td>
        </tr>
      </tfoot>
    {/await}
  </Table>

  <WorksheetHelp bind:open={openHelp} />
</Container>
