<script>
  import { closeModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  export let isOpen, title, message;
</script>

{#if isOpen}
  <Modal centered {isOpen} header={title}>
    <ModalBody>{message}</ModalBody>
    <ModalFooter>
      <Button color="primary" on:click={closeModal}>Close</Button>
    </ModalFooter>
  </Modal>
{/if}
