<script>
  import { push, pop } from "svelte-spa-router";
  import StageOne from "./fromScratch/StageOne.svelte";
  import StageTwo from "./fromScratch/StageTwo.svelte";
  import StageThree from "./fromScratch/StageThree.svelte";
  import StageFour from "./fromScratch/StageFour.svelte";
  import StageFive from "./fromScratch/StageFive.svelte";
  import { Progress, Container } from "sveltestrap";
  import { tick } from "svelte";

  // Stage of the process the user is currently at
  let stage = 1;

  // Whether the user is between stages
  let isRefreshing = false;

  function nextStage() {
    if (stage < 5) {
      isRefreshing = true;
      tick();
      stage++;
      isRefreshing = false;
    } else {
      // The setup is complete, go to login
      push("/");
    }
  }
</script>

<Container>
  {#if isRefreshing}
    Wait a second...
  {:else}
    <Container class="header">
      <h1>Kumon Management System</h1>
    </Container>

    <Container class="progressPart">
      <Progress value={stage - 1} max="4" />
    </Container>

    <Container class="content">
      {#if stage == 1}
        <StageOne on:done={nextStage} />
      {:else if stage == 2}
        <StageTwo on:done={nextStage} />
      {:else if stage == 3}
        <StageThree on:done={nextStage} />
      {:else if stage == 4}
        <StageFour on:done={nextStage} />
      {:else if stage == 5}
        <StageFive on:done={nextStage} />
      {/if}
    </Container>
  {/if}
</Container>
