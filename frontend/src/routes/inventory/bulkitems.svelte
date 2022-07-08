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

  import orderModal from "./modals/bulkItemOrderModal.svelte";
  import InfoModal from "./modals/InfoModal.svelte";
  import EditBulkItemModal from "./modals/EditBulkItemModal.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "./modals/ConfirmationModal.svelte";

  import AddBulkItemModal from "./modals/AddBulkItemModal.svelte";

  import BulkItemHelp from "./BulkItemHelp.svelte";

  import API_CONFIG from "../../api";
  import { BulkItemApi } from "kumon_app_backend_api";
  let bulkItemApi = new BulkItemApi(API_CONFIG);

  let pageFilterDetailsBulkitems = new PageFilter();
  let bulkitemsList = [];
  let openHelp = false;

  var today = new Date();

  /**
   * Refreshes the list of items on loan.
   */
  async function refreshBulkItems() {
    try {
      // Send a request to the backedn for the list of bulk items
      let response = await bulkItemApi.bulkItemList({
        page: pageFilterDetailsBulkitems.page,
        search: pageFilterDetailsBulkitems.filter,
      });
      // Update local bulk items list with the result of the request
      bulkitemsList = response.results;

      // Updates the filter based on the current view
      pageFilterDetailsBulkitems.pageUpdate(response);
      pageFilterDetailsBulkitems.filter += " ";
      pageFilterDetailsBulkitems.filter =
        pageFilterDetailsBulkitems.filter.substring(
          0,
          pageFilterDetailsBulkitems.filter.length - 1
        );
    } catch (e) {
      // Inform the user the system could not load the bulk item list
      openModal(InfoModal, {
        title: "Bulk Item List",
        message: "Could not load bulk items list!",
      });
    }
  }

  /**
   * Handler for ordering a bulk item
   * @param {number} id The ID of the item.
   */
  async function handleOrderBulkItem(id) {
    // Opens the modal for ordering the specified worksheet
    openModal(orderModal, {
      id: id,
      onChangesSaved: async (_) => {
        await refreshBulkItems();
      },
    });
  }

  /**
   * Handler for editing a worksheet
   * @param {number} id The ID of the worksheet.
   */
  function handleEditBulkItem(id) {
    // opens the modal for editing the bulk item
    openModal(EditBulkItemModal, {
      id: id,
      // When the changes are saved (form submitted)
      onChangesSaved: (newDetails) => {
        // Find the index of the changed item
        let existingIndex = bulkitemsList.findIndex(
          (bulkitem) => bulkitem.id === id
        );
        // Update the entry in the local worksheets list
        if (existingIndex >= 0) {
          bulkitemsList[existingIndex] = {
            id: id,
            name: newDetails.name,
            quantity: newDetails.quantity,
          };
        }
      },
    });
  }

  /**
   * Handler for adding a new bulk item
   */
  function handleAddBulkitem() {
    // Open the add bulk item modal
    openModal(AddBulkItemModal, {
      // When the form is submitted, refresh the list of bulk items
      onAdd: async (_) => {
        await refreshBulkItems();
      },
    });
  }

  /**
   * Handler for removing a student.
   * @param {number} id The ID of the item.
   */
  async function handleDeleteItem(id) {
    // Retrive information about item
    let bulkItem = await bulkItemApi.bulkItemRetrieve({ id: id });

    // Generate a confirmation message using the item details
    let confirmationMessage =
      "Are you sure you want to delete this bulkItem?\n\n" +
      "Name: " +
      bulkItem.name;

    // Opens a confirmation modal that must be accepted to continue
    openModal(ConfirmationModal, {
      title: "Delete Bulk Item",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        try {
          // Deletes the specified item
          bulkItemApi.bulkItemDestroy({ id: id }).then((_) => {
            // Remove this bulk item from the displayed list
            bulkitemsList = bulkitemsList.filter(
              (bulkItem) => bulkItem.id !== id
            );

            // Second object is needed to "replace" the confirmation modal (otherwise it will re-open)
            openModal(
              InfoModal,
              {
                title: "Delete Bulk Item",
                message: `Deleted Bulk Item ${id}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          console.log(e);
          openModal(
            InfoModal,
            {
              title: "Delete Bulk Item",
              message: `Could not mark bulkItem ${id} for deletion!`,
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
      <h1>Bulk Item Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpBulkItem"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpBulkItem" placement="top">
        User Guide for BulkItem Manager
      </Tooltip>
    </Col>
  </Row>
  <Row>
    <Col>
      <h2>BulkItem List</h2>
    </Col>

    <Col>
      <!-- Add a BulkItem -->
      <Button
        id="addBulkItem"
        color="success"
        style="float: right;"
        on:click={() => handleAddBulkitem()}
      >
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addBulkItem" placement="top">Add a New BulkItem</Tooltip>
    </Col>
  </Row>

  <PaginationFilteringBar
    refresh={() => refreshBulkItems()}
    pageFilter={pageFilterDetailsBulkitems}
  />

  <Table>
    <thead>
      <tr>
        <!-- <th>ID</th> -->
        <th>Item Name</th>
        <th>Quantity</th>
        <th>Edit</th>
        <th>Order</th>
        <th>Delete</th>
      </tr>
    </thead>
    {#await refreshBulkItems()}
      <tfoot class="info">
        <tr>
          <td colspan="5">Retrieving list of bulk items...</td>
        </tr>
      </tfoot>
    {:then}
      {#if bulkitemsList.length === 0}
        <tfoot class="info">
          <tr>
            <td colspan="5">No bulk item data found</td>
          </tr>
        </tfoot>
      {:else}
        <tbody>
          {#each bulkitemsList as bulkitem}
            <tr>
              <td>{bulkitem.name}</td>
              <td>{bulkitem.quantity}</td>
              <td>
                <Button
                  color="primary"
                  id="editBulkItem"
                  on:click={() => handleEditBulkItem(bulkitem.id)}
                >
                  <Icon name="pen" />
                </Button>
                <Tooltip target="editBulkItem" placement="top">
                  Edit Bulk Item Details
                </Tooltip>
              </td>

              <td>
                <Button
                  color="primary"
                  on:click={() => handleOrderBulkItem(bulkitem.id)}
                >
                  Order
                </Button>
              </td>

              <td>
                <Button
                  color="danger"
                  id="deleteBulkItem"
                  on:click={() => handleDeleteItem(bulkitem.id)}
                >
                  <Icon name="trash" />
                </Button>
                <Tooltip target="deleteBulkItem" placement="top">
                  Delete Bulk Item
                </Tooltip>
              </td>
            </tr>
          {/each}
        </tbody>
      {/if}
    {:catch}
      <tfoot class="info">
        <tr>
          <td colspan="6">Could not retrieve list of bulk items!</td>
        </tr>
      </tfoot>
    {/await}
  </Table>

  <BulkItemHelp bind:open={openHelp} />
</Container>

<style>
</style>
