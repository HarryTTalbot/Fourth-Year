<script>
  import { pop } from "svelte-spa-router";
</script>

<main>
  <h1>Page Not Found</h1>
  <button class="btn btn-primary" on:click={() => pop()}>Go Back</button>
</main>

<style>
  main {
    width: 100%;
    max-width: 400px;
    align-items: center;
    text-align: center;
    padding: 15px;
    margin: auto;
  }
</style>
