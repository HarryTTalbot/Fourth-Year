<script>
  import { closeModal, openModal } from "svelte-modals";
  import {
    Container,
    Button,
    Card,
    Icon,
    Tooltip,
    CardText,
    Modal,
    ModalBody,
    ModalFooter,
  } from "sveltestrap";

  import UserGuide from "../UserGuide.svelte";

  // Whether the user guide is open
  let isOpen = false;
</script>

<Card body class="p-3 h-100">
  <h2>About the App</h2>

  <CardText>
    KMS is an application for assist in the managing of a Kumon center.
  </CardText>

  <CardText>
    Each page has an individual user guide which can be found by pressing the
    help button:
  </CardText>

  <CardText>
    <Button id="helpDashboard" color="dark">
      <Icon name="question-square" />
    </Button>
    <Tooltip target="helpDashboard" placement="top">User Guide</Tooltip>
  </CardText>

  <CardText>
    This button is typically in the top right hand corner of the page.
  </CardText>

  <CardText>
    A full user guide for how to do common tasks and what each page's
    functionality is, can be viewed by pressing the button below:
  </CardText>
  <CardText>
    <Button color="primary" on:click={() => (isOpen = !isOpen)}>
      User Guide
    </Button>
  </CardText>
</Card>

{#if isOpen}
  <Modal centered size="xl" {isOpen} header={`User Guide`} scrollable>
    <ModalBody>
      <UserGuide />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={() => (isOpen = !isOpen)}
        >Close</Button
      >
    </ModalFooter>
  </Modal>
{/if}
