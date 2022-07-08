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

  import orderModal from "./modals/LendableItemsOrderModal.svelte";
  import InfoModal from "./modals/InfoModal.svelte";
  import EditLendableItemModal from "./modals/EditLendableItemModal.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "./modals/ConfirmationModal.svelte";

  import AddLendableItemModal from "./modals/AddLendableItemModal.svelte";

  import LendableItemHelp from "./LendableItemsHelp.svelte";

  import API_CONFIG from "../../api";
  import { LendableItemApi } from "kumon_app_backend_api";
  let lendableItemApi = new LendableItemApi(API_CONFIG);

  import { ItemLoanApi } from "kumon_app_backend_api";
  let itemLoanApi = new ItemLoanApi(API_CONFIG);

  let pageFilterDetailsLendableItems = new PageFilter();
  let lendableItemsList = [];
  let openHelp = false;

  var today = new Date();

  /**
   * Refreshes the list of items available for loan.
   */
  async function refreshLendableItems() {
    try {
      // Send a request to the backend for the list of lendable items
      let response = await lendableItemApi.lendableItemList({
        page: pageFilterDetailsLendableItems.page,
        search: pageFilterDetailsLendableItems.filter,
      });
      // let response = await lendableItemApi.lendableItemList();
      // Update local lendable item list with the result of the request
      lendableItemsList = response.results;

      // Updates the filter based on the current view
      pageFilterDetailsLendableItems.pageUpdate(response);
      pageFilterDetailsLendableItems.filter += " ";
      pageFilterDetailsLendableItems.filter =
        pageFilterDetailsLendableItems.filter.substring(
          0,
          pageFilterDetailsLendableItems.filter.length - 1
        );
    } catch (e) {
      // Inform the user the system could not load the lendable item list
      openModal(InfoModal, {
        title: "Lendable Item List",
        message: "Could not load lendable item list!",
      });
    }
  }

  /**
   * Refreshes the list of item logs/loans
   */
  async function refreshItemLogs() {
    try {
      // Send a request to the backend for the list of item loans
      let response = await itemLoanApi.itemLoanList({
        page: pageFilterDetailsItemLoans.page,
        search: pageFilterDetailsItemLoans.filter,
      });
      // Update local list with the result of the request
      itemLoansList = response.results;

      // Updates the filter based on the current view
      pageFilterDetailsItemLoans.pageUpdate(response);
      pageFilterDetailsItemLoans.filter += " ";
      pageFilterDetailsItemLoans.filter =
        pageFilterDetailsItemLoans.filter.substring(
          0,
          pageFilterDetailsItemLoans.filter.length - 1
        );
    } catch (e) {
      // Inform the user the system could not load the lendable item list
      openModal(InfoModal, {
        title: "Lendable Item Loan List",
        message: "Could not load lendable item list!",
      });
    }
  }

  /**
   * Handler for ordering a worksheet
   * @param {number} id The ID of the lendable item.
   */
  async function handleOrderLendableItem(id) {
    // Opens the modal for ordering the specified lendable item
    openModal(orderModal, {
      id: id,
      onAdd: async (_) => {
        await refreshLendableItems();
      },
    });
  }

  /**
   * Handler for editing a lendable item
   * @param {number} id The ID of the lendable item.
   */
  function handleEditLendableItem(id) {
    // Opens the modal for editing the item
    openModal(EditLendableItemModal, {
      id: id,
      // When the changes are saved (form submitted)
      onChangesSaved: (newDetails) => {
        // Find the index of the changed item
        let existingIndex = lendableItemsList.findIndex(
          (lendableItem) => lendableItem.id === id
        );
        // Update the entry in the local items list
        if (existingIndex >= 0) {
          lendableItemsList[existingIndex] = {
            id: id,
            name: newDetails.name,
            quantityAvailable: newDetails.quantityAvailable,
          };
        }
      },
    });
  }

  /**
   * Handler for adding a new item
   */
  function handleAddLendableItem() {
    // Open the add item modal
    openModal(AddLendableItemModal, {
      // When the form is submitted, refresh the list of items
      onAdd: async (_) => {
        await refreshLendableItems();
      },
    });
  }

  /**
   * Handler for removing a lendable item.
   * @param {number} id The ID of the lendable item.
   */
  async function handleDeleteItem(id) {
    // Retrieve information about item
    let lendableItem = await lendableItemApi.lendableItemRetrieve({ id: id });

    // Creates a confirmation message using the item details
    let confirmationMessage =
      "Are you sure you want to delete this lendableItem?\n\n" +
      "Name: " +
      lendableItem.name;

    // Opens a confirmation modal that must be accepted to continue
    openModal(ConfirmationModal, {
      title: "Delete Lendable Item",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        try {
          // Deletes the specified item
          lendableItemApi.lendableItemDestroy({ id: id }).then((_) => {
            // Remove this item from the displayed list
            lendableItemsList = lendableItemsList.filter(
              (lendableItem) => lendableItem.id !== id
            );

            // Second object is needed to "replace" the confirmation modal (otherwise it will re-open)
            openModal(
              InfoModal,
              {
                title: "Delete Lendable Item",
                message: `Deleted Lendable Item ${id}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          openModal(
            InfoModal,
            {
              title: "Delete Lendable Item",
              message: `Could not mark lendableItem ${id} for deletion!`,
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
      <h1>Lendable Items Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpLendableItem"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpLendableItem" placement="top">
        User Guide for lendable Items Manager
      </Tooltip>
    </Col>
  </Row>
  <Row>
    <Col>
      <h2>Lendable Items List</h2>
    </Col>

    <Col>
      <Button
        id="addLendableItem"
        color="success"
        style="float: right;"
        on:click={() => handleAddLendableItem()}
      >
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addLendableItem" placement="top">
        Add a New Lendable Item
      </Tooltip>
    </Col>
  </Row>

  <PaginationFilteringBar
    refresh={() => refreshLendableItems()}
    pageFilter={pageFilterDetailsLendableItems}
  />

  <Table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Quantity Available</th>
        <th>Edit</th>
        <th>Make an order</th>
        <th>Delete</th>
      </tr>
    </thead>
    {#await refreshLendableItems()}
      <tfoot class="info">
        <tr>
          <td colspan="5">Retrieving list of Lendable Items...</td>
        </tr>
      </tfoot>
    {:then}
      {#if lendableItemsList.length === 0}
        <tfoot class="info">
          <tr>
            <td colspan="5">No lendable items found</td>
          </tr>
        </tfoot>
      {:else}
        <tbody>
          {#each lendableItemsList as lendableItem}
            <tr>
              <td>{lendableItem.id}</td>
              <td>{lendableItem.name}</td>
              <td>{lendableItem.quantityAvailable}</td>
              <td>
                <Button
                  color="primary"
                  id="editLendableItem"
                  on:click={() => handleEditLendableItem(lendableItem.id)}
                >
                  <Icon name="pen" />
                </Button>
                <Tooltip target="editLendableItem" placement="top">
                  Edit Lendable Item Details
                </Tooltip>
              </td>

              <td>
                <Button
                  color="primary"
                  on:click={() => handleOrderLendableItem(lendableItem.id)}
                >
                  Lend out
                </Button>
              </td>

              <td>
                <Button
                  color="danger"
                  id="deleteLendableItem"
                  on:click={() => handleDeleteItem(lendableItem.id)}
                >
                  <Icon name="trash" />
                </Button>
                <Tooltip target="deleteLendableItem" placement="top">
                  Delete Lendable Item
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

  <LendableItemHelp bind:open={openHelp} />
</Container>
