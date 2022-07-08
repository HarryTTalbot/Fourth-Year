<!--
@component
UI component for viewing previous imports.

Exported properties:
- `fileDownloader`: The `FileDownloader` instance in use.
- `importApi`: The `ImportApi` instance in use.

Exported functions:
- `refreshImports`: Refreshes the list of imports.
-->
<script>
  import { onMount } from "svelte";
  import { fade } from "svelte/transition";
  import { Button, Table, Icon, Tooltip } from "sveltestrap";
  import { Modals, closeModal, openModal } from "svelte-modals";

  import API_CONFIG from "../../../api";
  import { ModelFile, ImportApi } from "kumon_app_backend_api";

  import { FileDownloader, Imports, Path } from "../../../utils";
  import { displayDate, displayTime } from "../../../utils/displayDateTime";

  import InfoModal from "../../../modals/InfoModal.svelte";

  /**
   * The file downloader instance we're using.
   * @type {FileDownloader}
   */
  export let fileDownloader = new FileDownloader();

  /**
   * The import API client instance we're using.
   * @type {ImportApi}
   */
  export let importApi = new ImportApi(API_CONFIG);

  /**
   * The current list of imports.
   * @type {ModelFile[]}
   */
  let imports = [];

  /**
   * Whether we are refreshing the list of imports.
   * @type {boolean}
   */
  let isRefreshing = false;

  /**
   * Refreshes the list of imports.
   */
  export async function refreshImports() {
    isRefreshing = true;

    // Query the backend
    try {
      let response = await importApi.importList();
      imports = response;
    } catch (e) {}

    isRefreshing = false;
  }

  /**
   * Downloads the specified import file.
   * @param {ModelFile} imp The import object we're downloading.
   */
  async function downloadImportFile(imp) {
    try {
      // Query the backend
      let blob = await importApi.importDownloadRetrieve({ id: imp.id });

      // Define the file name
      let filename = Path.basename(imp.file);

      // Use the file downloader to download the file
      fileDownloader.downloadBlob(blob, filename);
    } catch (e) {
      // If there is an error, inform the user with a modal
      openModal(InfoModal, {
        title: "Download Previous Import",
        message: "Could not download existing import!",
      });
    }
  }

  // On loading the page, get the list of imports
  onMount(async () => {
    await refreshImports();
  });
</script>

<div class="mb-3">
  <h2>View Previous Imports</h2>
  <p>
    This table shows all of the imports that were previously performed on the
    database.
  </p>

  <Table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Import Date</th>
        <th>Actions</th>
      </tr>
    </thead>

    {#if isRefreshing}
      <tfoot class="info">
        <tr>
          <td colspan="5">Retrieving list of imports...</td>
        </tr>
      </tfoot>
    {:else if imports.length === 0}
      <tfoot class="info">
        <tr>
          <td colspan="5">No previous imports found</td>
        </tr>
      </tfoot>
    {:else}
      <tbody>
        {#each imports as imp}
          <tr>
            <td>{imp.name}</td>
            <td>{Imports.getNameForImportType(imp.type)}</td>
            <td>{displayDate(imp.createdAt)}</td>
            <td>
              <Button
                id="downloadImport"
                color="primary"
                on:click={async () => await downloadImportFile(imp)}
              >
                <Icon name="download" />
              </Button>
              <Tooltip target="downloadImport" placement="top">
                Download
              </Tooltip>
            </td>
          </tr>
        {/each}
      </tbody>
    {/if}
  </Table>
</div>
