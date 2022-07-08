<script>
  import { Button, Container } from "sveltestrap";
  import { createEventDispatcher } from "svelte";
  import CenterDetailsForm from "../forms/CenterDetailsForm.svelte";
  import { CenterDetailsApi } from "kumon_app_backend_api";
  import API_CONFIG, { getConfig } from "../../../api";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { Modals, closeModal, openModal } from "svelte-modals";

  let detailsForm;

  const dispatch = createEventDispatcher();

  async function handleSubmit(evt) {
    try {
      // Link to the backend api
      let api = new CenterDetailsApi(getConfig());

      // Query the backend to set the center details
      await api.centerDetailsCreate({ centerDetailsRequest: evt.detail });
      nextStage();
    } catch (e) {
      // Show a modal if the query was unsuccessful
      openModal(InfoModal, {
        title: "Set Center Details",
        message: "Could not set the center details!",
      });
    }
  }

  function nextStage() {
    dispatch("done");
  }
</script>

<Container>
  <p>Secondly, we need to know some information on your Kumon center.</p>
  <CenterDetailsForm
    id="form"
    class="w-50"
    bind:this={detailsForm}
    on:submit={handleSubmit}
  />
  <Button form="form" color="primary" type="submit">Next</Button>
</Container>
