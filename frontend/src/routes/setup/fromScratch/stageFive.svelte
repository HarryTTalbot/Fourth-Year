<script>
  import { Button, Container, Icon, Tooltip } from "sveltestrap";
  import { createEventDispatcher } from "svelte";
  import UserGuide from "../../UserGuide.svelte";

  const dispatch = createEventDispatcher();

  function nextStage() {
    dispatch("done");
  }
</script>

<Container>
  <p>
    You have now done all you need to do for the set up process. Here we will
    briefly detail how to use the application.
  </p>

  <p>
    If you ever need help, you can access the user guide for any page by
    pressing this button:
  </p>

  <Button id="helpStage5" color="dark">
    <Icon name="question-square" />
  </Button>
  <Tooltip target="helpStage5" placement="top">User Guide</Tooltip>

  <p>It is usually located in the top right hand corner of a page.</p>

  <p>
    The dashboard contains a link to the application wide user guide which is
    also included below:
  </p>

  <UserGuide />

  <Button color="primary" on:click={nextStage}>Finish</Button>
</Container>
