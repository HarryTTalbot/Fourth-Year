<script>
  import { fade } from "svelte/transition";
  import { Modals, closeModal } from "svelte-modals";
  import { Container, TabContent, TabPane } from "sveltestrap";

  import ContactsManager from "./students/ContactsManager.svelte";
  import StudentManager from "./students/StudentManager.svelte";
</script>

<Container class="p-3">
  <TabContent>
    <TabPane tabId="studentManager" tab="Manage Students" active>
      <StudentManager />
    </TabPane>

    <TabPane tabId="contactsManager" tab="Manage Contacts">
      <ContactsManager />
    </TabPane>
  </TabContent>
</Container>
