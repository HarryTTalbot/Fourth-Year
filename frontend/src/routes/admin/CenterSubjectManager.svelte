<script>
  import { fade } from "svelte/transition";
  import { Modals, closeModal } from "svelte-modals";
  import { Container, TabContent, TabPane } from "sveltestrap";

  import SubjectManager from "./center/SubjectManager.svelte";
  import CenterManager from "./center/CenterManager.svelte";
</script>

<Container class="p-3">
  <TabContent>
    <TabPane tabId="centerManager" tab="Manage Center Details" active>
      <CenterManager />
    </TabPane>
    <TabPane tabId="subjectManager" tab="Manage Subjects Taught">
      <SubjectManager />
    </TabPane>
  </TabContent>
</Container>
