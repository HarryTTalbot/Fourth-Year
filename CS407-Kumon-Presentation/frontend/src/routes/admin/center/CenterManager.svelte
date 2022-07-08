<script>
  import { Button, Container, Icon, Tooltip, Row, Col } from "sveltestrap";
  import { createEventDispatcher } from "svelte";
  import CenterDetailsForm from "../../setup/forms/CenterDetailsForm.svelte";
  import { CenterDetailsApi } from "kumon_app_backend_api";
  import API_CONFIG, { getConfig } from "../../../api";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import { tick, onMount } from "svelte";
  import EditCenterDetailsModal from "./modals/EditCenterDetailsModal.svelte";
  import AddressDisplay from "../../../utils/displayAddress.svelte";
  import CenterDetailsHelp from "./CenterDetailsHelp.svelte";

  // Center Details object
  let details;

  // Whether the help window is open
  let openHelp = false;

  const dispatch = createEventDispatcher();

  // Function to refresh the center details
  async function refreshDetails() {
    try {
      // Link to the backend api
      let api = new CenterDetailsApi(getConfig());

      // Query the Backend
      details = await api.centerDetailsFetchRetrieve({});
    } catch (e) {}
  }

  async function handleEdit() {
    openModal(EditCenterDetailsModal, {
      onChangesSaved: async () => {
        // Refresh the staff list
        await refreshDetails();
      },
    });
  }
</script>

<!-- Content of the page -->
<Container class="p-3">
  <Row>
    <Col>
      <h1>Center Details Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpCenterDetails"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpCenterDetails" placement="top">
        User Guide for Center Details Manager
      </Tooltip>
    </Col>
  </Row>

  <Button id="editCenter" color="primary" on:click={handleEdit}>
    <Icon name="pen" />
  </Button>
  <Tooltip target="editCenter" placement="top">Update Center Details</Tooltip>
  {#await refreshDetails()}
    <p>Fetching center details...</p>
  {:then}
    {#if details}
      <p class="spacing">
        <b> Name: </b>
        {details.name} <br />
        <b> Phone Number: </b>
        {details.phoneNumber} <br />
        <b> Address: </b> <br />
        <AddressDisplay address={details.address} />
      </p>
    {:else}
      <p>Failed to fetch center details...</p>
    {/if}
  {:catch}
    <p>Failed to fetch center details...</p>
  {/await}
  <CenterDetailsHelp bind:open={openHelp} />
</Container>

<style>
  p.spacing {
    line-height: 1.5;
  }
</style>
