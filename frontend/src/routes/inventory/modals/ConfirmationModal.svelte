<script context="module">
  /**
   * Enum for the types of buttons for this confirmation dialog.
   * @readonly
   * @enum {string}
   */
  export const BUTTONS = Object.freeze({
    /** Yes/No Buttons */
    yesNo: "yesNo",

    /** Ok/Cancel Buttons */
    okCancel: "okCancel",
  });
</script>

<script>
  import { closeModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * The title of this modal.
   * @type {string}
   */
  export let title;

  /**
   * The message for this modal.
   * @type {string}
   */
  export let message;

  /**
   * The button labels to use for this modal.
   * @type {string}
   */
  export let buttons = BUTTONS.okCancel;

  /**
   * Callback for a positive response (i.e. confirmation) from this modal.
   */
  export let onConfirm = () => {};

  /**
   * Callback for a negative response (i.e. cancellation) from this modal.
   * By default, this just closes the modal.
   */
  export let onCancel = () => {
    closeModal();
  };

  let confirmLabel = "";
  let cancelLabel = "";

  /**
   * Handle the response that was chosen.
   * @param {boolean} confirmed
   */
  function handleResponse() {
    // await onResponse(confirmed);
  }

  $: switch (buttons) {
    case BUTTONS.yesNo:
      confirmLabel = "Yes";
      cancelLabel = "No";
      break;
    case BUTTONS.okCancel:
    default:
      confirmLabel = "OK";
      cancelLabel = "Cancel";
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={title}>
    <ModalBody>
      <span class="body">{message}</span>
    </ModalBody>

    <ModalFooter>
      <Button color="secondary" on:click={onCancel}>
        {cancelLabel}
      </Button>
      <Button color="primary" on:click={onConfirm}>
        {confirmLabel}
      </Button>
    </ModalFooter>
  </Modal>
{/if}

<style>
  span.body {
    white-space: break-spaces;
  }
</style>
