<script context="module">
  /**
   * @class Holds the various properties used in the `PaginationFilteringBar` component.
   * @property {int} size
   * @property {int} viewSize
   * @property {int} page
   * @property {string} filter
   * @property {boolean} previousPage
   * @property {boolean} nextPage
   * @function updatePage
   * @function changePage
   */
  export class PageFilter {
    constructor() {
      this.size = 0;
      this.page = 1;
      this.filter = "";
      this.lowerRange = 0;
      this.upperRange = 0;
      this.previousPage = false;
      this.nextPage = false;
    }
    // Function to update the object based upon a refresh of the current view
    pageUpdate(response) {
      // Update the size of all results matching the filter
      this.size = response.count;
      // Update the upper and lower range
      if (this.size == 0) {
        this.lowerRange = 0;
        this.upperRange = 0;
      } else {
        this.lowerRange = (this.page - 1) * 5 + 1;
        this.upperRange = (this.page - 1) * 5 + response.results.length;
      }
      // Update the variables on whether there is a previous and next page
      if (response.next == null) {
        this.nextPage = false;
      } else {
        this.nextPage = true;
      }
      if (response.previous == null) {
        this.previousPage = false;
      } else {
        this.previousPage = true;
      }
    }
    // Function to update the page shown
    pageChange(change) {
      // Update the current page variable
      this.page = this.page + change;
    }
  }
</script>

<script>
  import { Button, Input, Label, Row, Col } from "sveltestrap";
  // Parameters - object containing details of what to be displayed
  export let pageFilter;
  // Parameters - function to be called to refresh the current list shown
  export let refresh = () => {};
  // Function to change the page shown
  async function changePage(change) {
    pageFilter.pageChange(change);
    await refresh();
  }
  // Function to change the filter shown
  async function filterChange() {
    pageFilter.page = 1;
    await refresh();
  }
</script>

<div class="component">
  <!-- Filtering -->
  <div class="filtering">
    <Input
      placeholder="Filter Text"
      type="text"
      bind:value={pageFilter.filter}
      on:change={() => filterChange()}
    />
  </div>
  <!-- Pagination -->
  <div class="pagination">
    Showing {pageFilter.lowerRange}-{pageFilter.upperRange} out of {pageFilter.size}

    <div class="paginationButton">
      <Button
        color="primary"
        disabled={!pageFilter.previousPage}
        on:click={() => changePage(-1)}
      >
        Previous
      </Button>
    </div>
    <div class="paginationButton">
      <Button
        color="primary"
        disabled={!pageFilter.nextPage}
        on:click={() => changePage(1)}
      >
        Next
      </Button>
    </div>
  </div>
</div>

<style>
  .component {
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .filtering {
    margin-left: 0;
    margin-right: auto;
    width: 50%;
    float: left;
  }
  .pagination {
    margin-left: auto;
    margin-right: 0;
    float: right;
  }
  .paginationButton {
    margin-left: 5px;
  }
</style>
