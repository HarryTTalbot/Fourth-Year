<script>
  import { closeModal, openModal } from "svelte-modals";
  import { Button, Modal, ModalBody, ModalFooter } from "sveltestrap";

  import API_CONFIG from "../../../../api";
  import { ContactsApi } from "kumon_app_backend_api";

  import ContactForm from "../../forms/ContactForm.svelte";
  import InfoModal from "../../../../modals/InfoModal.svelte";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * Callback for when a new contact is added.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for contacts.
   */
  export let onAdd = (newDetails) => {};

  /**
   * The contacts API instance currently in use.
   * @type {ContactsApi}
   */
  export let contactsApi = new ContactsApi(API_CONFIG);

  /**
   * The backing form element for the "Add Contact" form.
   * @type {ContactForm}
   */
  let addContactForm;

  /**
   * Handles submission of the new contact details.
   */
  async function handleSubmit(details) {
    try {
      await contactsApi.contactsCreate({ contactRequest: details });

      // Reset the form (since svelte-modals re-uses the component instances)
      addContactForm.reset();

      // Notify that we were successful
      openModal(
        InfoModal,
        {
          title: "Add Contact",
          message: "Successfully added contact!",
        },
        { replace: true }
      );

      onAdd(details);
    } catch (e) {
      openModal(InfoModal, {
        title: "Add Contact",
        message: `Could not save details for new contact!`,
      });
    }
  }
</script>

{#if isOpen}
  <Modal centered {isOpen} header={"Add Contact"}>
    <ModalBody>
      <ContactForm
        id="add-contact-form"
        bind:this={addContactForm}
        on:submit={async (e) => await handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="add-contact-form" type="submit">
        Submit
      </Button>
    </ModalFooter>
  </Modal>
{/if}
