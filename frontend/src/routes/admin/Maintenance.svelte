<!--
@component
UI component for maintenance tasks.
-->
<script>
  import { Container, TabContent, TabPane } from "sveltestrap";

  import ImportExport from "./maintenance/ImportExport.svelte";
  import ViewImports from "./maintenance/ViewImports.svelte";
  import DeletedRecords from "./maintenance/DeletedRecords.svelte";

  /**
   * Component instance for the "View Imports" view.
   * @type {ViewImports}
   */
  let viewImportsComponent;
</script>

<Container class="p-3">
  <TabContent>
    <TabPane tabId="importExport" tab="Import/Export Data" active>
      <Container class="p-3">
        <ImportExport on:import={viewImportsComponent.refreshImports} />
        <ViewImports bind:this={viewImportsComponent} />
      </Container>
    </TabPane>
    <TabPane tabId="gdprRecords" tab="Deleted Records">
      <DeletedRecords />
    </TabPane>
  </TabContent>
</Container>
