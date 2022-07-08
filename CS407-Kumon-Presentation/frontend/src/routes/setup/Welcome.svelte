<script>
  import { push } from "svelte-spa-router";
  import { Button, Input, Label } from "sveltestrap";

  // Import using .kumon export file
  function option1() {
    push("/welcome/import");
  }

  // Start from scratch
  function option2() {
    push("/welcome/setup");
  }
</script>

<main>
  <div class="title">
    <h1>Kumon Management System</h1>

    <p>
      This is a management application for Kumon centers to manage attendance,
      inventory, record sheets and more ...
    </p>
  </div>

  <div class="body">
    <p>Looks like the application hasnt been setup yet.</p>
    <p>There are two options to start from:</p>
    <br />
    <div class="options">
      <Label>1. Import from .kumon export file</Label><br />
      <div class="buttons">
        <Button on:click={option1} color="primary">Import Data</Button>
      </div>
      <br />
      <Label>2. Start from scratch</Label><br />
      <div class="buttons">
        <Button on:click={option2} color="primary">Start</Button>
      </div>
    </div>
  </div>
</main>

<style>
  main {
    width: 100%;
    max-height: 100%;
    max-width: 40%;
    margin-left: auto;
    margin-right: auto;
  }

  .title {
    text-align: center;
    margin-top: 5%;
  }

  .body {
    margin-top: 20%;
    margin-bottom: 20%;
    margin-left: auto;
    margin-right: auto;
    max-width: 35%;
    min-width: 250px;
    text-align: left;
  }

  .options {
    padding-left: 20px;
  }

  .buttons {
    padding-left: 25%;
  }
</style>
