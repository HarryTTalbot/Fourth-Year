<script>
  import { Button, Container } from "sveltestrap";
  import { createEventDispatcher } from "svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import SubjectManager from "../../admin/center/SubjectManager.svelte";

  const dispatch = createEventDispatcher();

  function nextStage() {
    dispatch("done");
  }
</script>

<Container>
  <p>
    Thirdly, we need to know the subjects being taught. You can always change
    these later, but it is recommended to only set them once.
  </p>

  <p>
    To add a subject press "New Subject". Once a subject has been added, you can
    add levels to it by pressing on the subject in the table.
  </p>

  <SubjectManager />

  <Button color="primary" on:click={nextStage}>Next</Button>
</Container>
