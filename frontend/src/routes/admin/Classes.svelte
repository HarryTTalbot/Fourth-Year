<script>
  import { fade } from "svelte/transition";
  import { Modals, closeModal } from "svelte-modals";
  import { Container, TabContent, TabPane } from "sveltestrap";

  import ClassManager from "./classes/ClassManager.svelte";
  import AssignStudents from "./classes/AssignStudents.svelte";
</script>

<Container class="p-3">
  <h1>Class Manager</h1>
  <TabContent>
    <TabPane tabId="classManager" tab="Manage Classes" active>
      <ClassManager />
    </TabPane>
    <TabPane tabId="assignStudents" tab="Assign Students to Classes">
      <AssignStudents />
    </TabPane>
  </TabContent>
</Container>
