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
    Card,
  } from "sveltestrap";
  import { tick } from "svelte";
  import { push } from "svelte-spa-router";
  import { displayDate, displayTime } from "../../utils/displayDateTime";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../components/PaginationFilteringBar.svelte";

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
   * Refreshes the list of items on loan.
   */
  async function refreshLendableItems() {
    try {
      let response = await itemLoanApi.itemLoanList({
        page: pageFilterDetailsItemLoans.page,
        search: pageFilterDetailsItemLoans.filter,
      });

      itemLoansList = response.results;

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

  async function handleOrderLendableItem(id) {
    openModal(orderModal, {
      id: id,
    });
  }

  function handleAddLendableItem() {
    openModal(AddLendableItemModal, {
      onAdd: async (_) => {
        await refreshLendableItems();
      },
    });
  }

  async function handleViewLogs(id) {
    // let response = await itemLoanApi.itemLoanHistoryList(id)
    let response = await itemLoanApi.itemLoanList({ id: id });
  }

  async function handleDeleteItemLoan(id) {
    let response = await itemLoanApi.itemLoanDestroy({ id: id });
  }

  async function handleReturnItem(id, quantity) {
    let response = await itemLoanApi.itemLoanReturnItemCreate({
      id: id,
      returnItemRequest: { quantity: quantity },
    });
    await refreshLendableItems();
  }

  let student = null;

  async function getStudent(id) {
    let response = await studentsApi.studentsRetrieve({ id: id });
    var details = [];
    details[0] = response.firstName;
    details[1] = response.lastName;

    student = details;

    return details;
  }
</script>

<Card body class="p-3 h-100">
  <h2>Inventory - Lendable Items</h2>

  <Table>
    <thead>
      <tr>
        <th>Item ID</th>
        <th>Quantity</th>
        <th>Student ID</th>
      </tr>
    </thead>
    {#await refreshLendableItems()}
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
              <td>{itemLoan.itemId}</td>
              <td>{itemLoan.quantity}</td>
              <td>{itemLoan.studentId}</td>
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
</Card>
