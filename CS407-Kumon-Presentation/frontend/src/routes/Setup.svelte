<script>
  import Router from "svelte-spa-router";

  import Welcome from "./setup/Welcome.svelte";
  import ImportKumon from "./setup/ImportKumon.svelte";
  import FromScratch from "./setup/FromScratch.svelte";
  import NotFound from "./NotFound.svelte";

  const prefix = "/welcome";
  const routes = {
    "/": Welcome,
    "/import": ImportKumon,
    "/setup": FromScratch,
    "*": NotFound,
  };
</script>

<main>
  <Router {routes} {prefix} />
</main>

<style>
  main {
    height: 100vh;
  }
</style>
