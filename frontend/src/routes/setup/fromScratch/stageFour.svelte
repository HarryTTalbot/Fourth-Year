<script>
  import { push, pop } from "svelte-spa-router";
  import dayjs from "dayjs";
  import { createEventDispatcher } from "svelte";
  import { fade } from "svelte/transition";
  import { Button, FormGroup, Input, Label, Container } from "sveltestrap";
  import { Modals, closeModal, openModal } from "svelte-modals";

  import API_CONFIG from "../../../api";
  import { ImportApi, FileTypeEnum } from "kumon_app_backend_api";
  import InfoModal from "../../../modals/InfoModal.svelte";

  /**
   * The import API client instance we're using.
   * @type {ImportApi}
   */
  export let importApi = new ImportApi(API_CONFIG);

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
   * Handler for import form submission.
   */
  async function handleImport() {
    try {
      await importApi.importCreate({
        name: "K-SIS Student Data Import",
        file: selectedFiles[0],
        type: FileTypeEnum.KSis,
      });

      // Open a modal to tell the user the task was successful
      openModal(InfoModal, {
        title: "Import Data",
        message: "Successfully imported data!",
      });

      nextStage();
    } catch (e) {
      // Open a modal to tell the user, the task has failed
      openModal(InfoModal, {
        title: "Import Data",
        message: "Could not import data!",
      });
    }
  }

  function nextStage() {
    dispatch("done");
  }
</script>

<Container>
  <p>
    This application features integration with K-SIS. If you want you can upload
    a K-SIS excel dump file here, and we will import all the student data so you
    don’t have to add them manually.
  </p>

  <p>
    This stage is completely optional, so press skip if you don’t want to (you
    can always do this once the application is set up!)
  </p>

  <div class="body">
    <p>
      Please upload the .xlsx K-SIS export dump file below and press "Import" to
      start the process.
    </p>
    <br />
    <form
      class="body"
      on:submit|preventDefault={async () => await handleImport()}
    >
      <FormGroup>
        <Label for="importFile">Choose a file:</Label>
        <Input
          id="importFile"
          type="file"
          accept=".xlsx"
          required
          bind:files={selectedFiles}
        />
      </FormGroup>

      <Button color="primary" type="submit">Import</Button>
    </form>
  </div>

  <br />
  <Button color="primary" on:click={nextStage}>Skip</Button>
</Container>
