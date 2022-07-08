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
   * The ID of the contact currently being edited.
   * @type {number}
   */
  export let id;

  /**
   * Callback for when changes were saved for this contact.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for contact.
   */
  export let onChangesSaved = (newDetails) => {};

  /**
   * The contacts API instance currently in use.
   * @type {ContactsApi}
   */
  export let contactsApi = new ContactsApi(API_CONFIG);

  /**
   * The backing element for the displayed form.
   * @type {ContactForm}
   */
  let editContactForm;

  /**
   * Loads the contact's current details into this form.
   * @param {number} id The ID of the contact.
   */
  async function loadContactDetails(id) {
    try {
      let details = await contactsApi.contactsRetrieve({ id: id });
      editContactForm.setDefaultValues(details);
      editContactForm.reset();
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit Contact",
        message: `Could not load details for contact ${id}!`,
      });
    }
  }

  /**
   * Handles submission of the new contact details.
   */
  async function handleSubmit(details) {
    try {
      await contactsApi.contactsUpdate({ id: id, contactRequest: details });

      // Notify that we were successful
      openModal(
        InfoModal,
        {
          title: "Edit Contact",
          message: `Successfully edited contact ${id}!`,
        },
        { replace: true }
      );

      onChangesSaved(details);
    } catch (e) {
      openModal(InfoModal, {
        title: "Edit Contact",
        message: `Could not save new details for contact ${id}!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadContactDetails(id);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Edit Contact ${id}...`}>
    <ModalBody>
      <ContactForm
        id="edit-contact-form"
        bind:this={editContactForm}
        on:submit={async (e) => handleSubmit(e.detail)}
      />
    </ModalBody>
    <ModalFooter>
      <Button color="warning" outline on:click={() => editContactForm.reset()}>
        Reset to Original Values
      </Button>
      <Button color="secondary" outline on:click={closeModal}>Cancel</Button>
      <Button color="primary" form="edit-contact-form" type="submit">
        Save Changes
      </Button>
    </ModalFooter>
  </Modal>
{/if}
