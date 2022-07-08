<!--
@component
UI component for importing/exporting data.

Exported properties:
- `exportApi`: The `ExportApi` instance in use.
- `importApi`: The `ImportApi` instance in use.
- `fileDownloader`: The `FileDownloader` instance in use.

Events:
- `import`: Emitted when an import was successfully made.
  - No parameters provided.
-->
<script>
  import dayjs from "dayjs";
  import { createEventDispatcher } from "svelte";
  import { fade } from "svelte/transition";
  import {
    Button,
    FormGroup,
    Input,
    Label,
    Row,
    Col,
    Tooltip,
    Icon,
  } from "sveltestrap";
  import { Modals, closeModal, openModal } from "svelte-modals";

  import API_CONFIG from "../../../api";
  import { ExportApi, ImportApi, FileTypeEnum } from "kumon_app_backend_api";

  import { FileDownloader, Imports } from "../../../utils";

  import InfoModal from "../../../modals/InfoModal.svelte";

  import ImportHelp from "./ImportHelp.svelte";

  /**
   * The export API client instance we're using.
   * @type {ExportApi}
   */
  export let exportApi = new ExportApi(API_CONFIG);

  /**
   * The import API client instance we're using.
   * @type {ImportApi}
   */
  export let importApi = new ImportApi(API_CONFIG);

  /**
   * The file downloader helper instance we're using.
   * @type {FileDownloader}
   */
  export let fileDownloader = new FileDownloader();

  /**
   * Svelte event dispatcher instance.
   */
  const dispatch = createEventDispatcher();

  /**
   * Internal array holding the files we are attempting to import.
   */
  let selectedFiles = [];

  /**
   * The name of the import we are creating.
   */
  let importName = "";

  /**
   * The file we are attempting to import.
   * @type {File | null}
   */
  let importFile = null;

  /**
   * The type of file we are attempting to import.
   * @type {FileTypeEnum | null}
   */
  let importType = null;

  let openHelp = false;

  /**
   * Handler for import form submission.
   */
  async function handleImport() {
    try {
      // Send the import request to the backend
      await importApi.importCreate({
        name: importName,
        file: importFile,
        type: importType,
      });

      // Inform the user the import was successful
      openModal(InfoModal, {
        title: "Import Data",
        message: "Successfully imported data!",
      });

      dispatch("import");
    } catch (e) {
      // Inform the user the import was unsuccessful
      openModal(InfoModal, {
        title: "Import Data",
        message: "Could not import data!",
      });
    }
  }

  /**
   * Handler for database exports.
   */
  async function handleExport() {
    try {
      // Query the backend for an export file
      let blob = await exportApi.exportRetrieve();

      // Define the filename for the export file
      let dateStr = dayjs().format("YYYY-MM-DD_HH-mm-ss");
      let filename = `dump-${dateStr}.kumon`;

      // Set the file to be automatically downloaded
      fileDownloader.downloadBlob(blob, filename);
    } catch (e) {
      // If an error occurs, inform the user through a modal
      openModal(InfoModal, {
        title: "Export Data",
        message: "Could not retrieve data for exporting!",
      });
    }
  }

  // When a new file is chosen, update the chosen file and import type
  $: {
    if (selectedFiles && selectedFiles[0]) {
      importFile = selectedFiles[0];
      importType = Imports.getImportTypeForFile(importFile);
    }
  }
</script>

<div class="mb-3">
  <Row>
    <Col>
      <h1>Import/Export Data</h1>
    </Col>

    <Col>
      <Button
        id="helpImport"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpImport" placement="top">
        User Guide for Import/Export Manager
      </Tooltip>
    </Col>
  </Row>

  <Row>
    <Col>
      <h2>Import Data</h2>

      <p>Please choose a file and the type of file you are importing.</p>

      <form
        class="w-75"
        on:submit|preventDefault={async () => await handleImport()}
      >
        <FormGroup>
          <Label for="importName">Name of Import</Label>
          <Input id="importName" required bind:value={importName} />
        </FormGroup>

        <FormGroup>
          <Label for="importFile">File to Import</Label>
          <Input
            id="importFile"
            type="file"
            accept=".kumon,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            required
            bind:files={selectedFiles}
          />
        </FormGroup>

        <FormGroup>
          <Label for="importType">Import Type</Label>
          <Input id="importType" type="select" required bind:value={importType}>
            {#each Imports.IMPORT_TYPES as im}
              <option value={im.type}>{im.name}</option>
            {/each}
          </Input>
        </FormGroup>

        <Button color="primary" type="submit">Import</Button>
      </form>
    </Col>
    <Col>
      <div class="mb-3">
        <h2>Export Data</h2>

        <p>
          This will export all data currently present in the database. It can be
          re-imported later using the import form.
        </p>

        <Button color="primary" on:click={async () => await handleExport()}>
          Export All Data
        </Button>
      </div>
    </Col>
  </Row>

  <ImportHelp bind:open={openHelp} />
</div>
