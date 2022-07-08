<script>
  import { fade } from "svelte/transition";
  import { Modals, closeModal } from "svelte-modals";
  import { Container, TabContent, TabPane } from "sveltestrap";

  import Lendableitems from "./lendableitems.svelte";
  import LendableitemLogs from "./lendableitemLogs.svelte";
</script>

<!-- Uses two tabs -->

<Container class="p-3">
  <TabContent>
    <!-- Lendable Item Manager -->
    <TabPane tabId="lendableItems" tab="Manage Lendable Items" active>
      <Lendableitems />
    </TabPane>

    <!-- Loan Manager -->
    <TabPane tabId="lendableItemLogs" tab="Manage Loans">
      <LendableitemLogs />
    </TabPane>
  </TabContent>
</Container>
