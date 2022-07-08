<script>
  import Router from "svelte-spa-router";

  import Worksheets from "./inventory/Worksheets.svelte";
  import bulkitems from "./inventory/bulkitems.svelte";
  import lendableItemManager from "./inventory/lendableItemManager.svelte";
  import MainNavbar from "../components/MainNavbar.svelte";
  import NotFound from "./NotFound.svelte";

  const prefix = "/inventory";
  const routes = {
    "/worksheets": Worksheets,
    "/bulkitems": bulkitems,
    "/lendableitems": lendableItemManager,
    "*": NotFound,
  };
</script>

<main>
  <MainNavbar active="/inventory" />
  <Router {routes} {prefix} />
</main>

<style>
  main {
    height: 100vh;
  }
</style>
