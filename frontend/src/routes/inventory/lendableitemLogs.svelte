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
  } from "sveltestrap";
  import { tick } from "svelte";
  import { push } from "svelte-spa-router";
  import { displayDate, displayTime } from "../../utils/displayDateTime";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../components/PaginationFilteringBar.svelte";

  import orderModal from "./modals/LendableItemsOrderModal.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "./modals/ConfirmationModal.svelte";

  import AddLendableItemModal from "./modals/AddLendableItemModal.svelte";

  import API_CONFIG from "../../api";
  import { LendableItemApi } from "kumon_app_backend_api";
  let lendableItemApi = new LendableItemApi(API_CONFIG);

  import { ItemLoanApi } from "kumon_app_backend_api";
  let itemLoanApi = new ItemLoanApi(API_CONFIG);

  import { StudentsApi } from "kumon_app_backend_api";
  let studentsApi = new StudentsApi(API_CONFIG);

  let pageFilterDetailsItemLoans = new PageFilter();
  let itemLoansList = [];

  var today = new Date();

  /**
   * Refreshes the list of loans.
   */
  async function refreshLendableItemLoans() {
    try {
      // Send a request to the backend for the list of item loans/logs
      let response = await itemLoanApi.itemLoanList({
        page: pageFilterDetailsItemLoans.page,
        search: pageFilterDetailsItemLoans.filter,
      });
      // Update local item loan list with the result of the request
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
      throw e;
    }
  }

  /**
   * Handler for editing a worksheet
   * @param {number} id The ID of the worksheet.
   * @param {number} quantity The number of items that are being returned.
   */
  async function handleReturnItem(id, quantity) {
    // Sends a request to the backend, logging the item was returned
    // Quantity can be changed in future implementations to allow fractional returns.
    let response = await itemLoanApi.itemLoanReturnItemCreate({
      id: id,
      returnItemRequest: { quantity: quantity },
    });
    // Updates the list of logs
    await refreshLendableItemLoans();
  }

  let student = null;

  /**
   * Unused handler for getting a student record
   * @param {number} id The ID of the student.
   */
  async function handleGetStudent(id) {
    let response = await studentsApi.studentsRetrieve({ id: id });
    var details = [];
    details[0] = response.firstName;
    details[1] = response.lastName;
    student = details;
    return details;
  }
</script>

<!-- Content of the page -->
<Container class="p-3">
  <h1>Lendable Item Loans</h1>

  <PaginationFilteringBar
    refresh={() => refreshLendableItemLoans()}
    pageFilter={pageFilterDetailsItemLoans}
  />

  <Table>
    <thead>
      <tr>
        <th>Item ID</th>
        <th>Quantity</th>
        <th>Student ID</th>
        <!-- <th>First Name</th> -->
        <!-- <th>Last Name</th> -->
        <th>Return Items</th>
      </tr>
    </thead>
    {#await refreshLendableItemLoans()}
      <tfoot class="info">
        <tr>
          <td colspan="6">Retrieving list of Lendable Items...</td>
        </tr>
      </tfoot>
    {:then}
      {#if itemLoansList.length === 0}
        <tfoot class="info">
          <tr>
            <td colspan="6">No loan logs found</td>
          </tr>
        </tfoot>
      {:else}
        <tbody>
          {#each itemLoansList as itemLoan}
            <tr>
              <!-- <td>{itemLoan.id}</td> -->
              <td>{itemLoan.itemId}</td>
              <td>{itemLoan.quantity}</td>
              <td>{itemLoan.studentId}</td>

              <!-- Extension: Add additional details such as student name -->
              <!-- Currently disabled to provide anonymity for students -->

              <td>
                <Button
                  color="warning"
                  on:click={() =>
                    handleReturnItem(itemLoan.id, itemLoan.quantity)}
                >
                  Return
                </Button>
              </td>
            </tr>
          {/each}
        </tbody>
      {/if}
    {:catch}
      <tfoot class="info">
        <tr>
          <td colspan="6">Could not retrieve list of items!</td>
        </tr>
      </tfoot>
    {/await}
  </Table>
</Container>

<style>
</style>
