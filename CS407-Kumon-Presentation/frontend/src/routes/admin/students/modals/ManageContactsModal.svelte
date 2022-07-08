<script>
  import { closeModal, openModal } from "svelte-modals";
  import {
    Button,
    Table,
    Input,
    Modal,
    ModalBody,
    ModalFooter,
    Icon,
    Tooltip,
  } from "sveltestrap";

  import ContactField from "../../../../formFields/ContactField.svelte";

  import InfoModal from "../../../../modals/InfoModal.svelte";

  import API_CONFIG from "../../../../api";
  import { StudentsApi } from "kumon_app_backend_api";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * The ID of the student currently being edited.
   * @type {number}
   */
  export let id;

  /**
   * The details of the student currently being edited.
   * @type {details} matches the student API endpoint
   */
  let studentDetails;

  /**
   * List of contacts associated with the chosen student
   */
  let contacts = [];

  /**
   * The ID of the contact being selected.
   * @type {number}
   */
  let newContact;

  let contactError;
  let contactComp;

  /**
   * The type of relationship being created.
   * @type {string} defaults to "Mother" to allow immediate submission
   */
  let newRelationship = "Mother";

  /**
   * The students API instance in use.
   * @type {StudentsApi}
   */
  let studentsApi = new StudentsApi(API_CONFIG);

  /**
   * Callback for when changes were saved for this student.
   * @param newDetails The new details that were chosen. Matches the API endpoint's format for students.
   */
  export let onClose = (newList) => {};

  /**
   * Loads the student's current details into this form.
   * @param {number} id The ID of the student.
   */
  async function loadStudentDetails(id) {
    try {
      studentDetails = await studentsApi.studentsRetrieve({ id: id });
      // Get the list of contacts associated with the chosen student
      contacts = await studentsApi.studentsGetContactsList({ id: id });
    } catch (e) {
      openModal(InfoModal, {
        title: "Manage Student Contacts",
        message: `Could not load details for student ${id}!`,
      });
    }
  }

  async function deleteContact(contact_id) {
    try {
      await studentsApi.studentsRemoveContactsCreate({
        id: id,
        studentRemoveContactsRequest: [{ contactId: contact_id }],
      });
      await loadStudentDetails(id);
    } catch (e) {
      openModal(InfoModal, {
        title: "Manage Student Contacts",
        message: `Could not remove the contact!`,
      });
    }
  }

  async function addContact() {
    try {
      // verifies if the contact has already been linked to the student
      for (let i = 0; i < contacts.length; i++) {
        if (contacts[i].contactId.id == newContact) {
          openModal(InfoModal, {
            title: "Manage Student Contacts",
            message: `Cannot add a duplicate contact`,
          });
          return;
        }
      }

      await studentsApi.studentsAddContactsCreate({
        id: id,
        studentAddContactsRequest: [
          { contactId: newContact, relationship: newRelationship },
        ],
      });

      await loadStudentDetails(id);

      newContact = null;
      contactComp.handleClear();
    } catch (e) {
      openModal(InfoModal, {
        title: "Manage Student Contacts",
        message: `Could not add the contact!`,
      });
    }
  }

  function close() {
    onClose(contacts);
    closeModal();
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadStudentDetails(id);
</script>

{#if isOpen && studentDetails != undefined}
  <Modal
    centered
    size="lg"
    {isOpen}
    header={`Manage Contacts for ${studentDetails.lastName}, ${studentDetails.firstName}`}
  >
    <ModalBody>
      <Table>
        <thead>
          <tr>
            <th style="width: 60%">Contact Name</th>
            <th style="width: 30%">Relationship</th>
            <th style="width: 10%" />
          </tr>
        </thead>
        <tbody>
          {#each contacts as contact}
            <tr>
              <td>
                {contact.contactId.lastName}, {contact.contactId.firstName}
              </td>
              <td>
                {contact.relationship}
              </td>
              <td>
                <Button
                  id={"deleteContactLink" + contact.contactId.id}
                  color="danger"
                  on:click={() => deleteContact(contact.contactId.id)}
                >
                  <Icon name="trash" />
                </Button>
                <Tooltip
                  target={"deleteContactLink" + contact.contactId.id}
                  placement="top"
                >
                  Remove {contact.contactId.lastName}, {contact.contactId
                    .firstName} as a Contact
                </Tooltip>
              </td>
            </tr>
          {/each}
          <tr>
            <td>
              <ContactField
                id="class"
                invalid={contactError}
                feedback={contactError}
                bind:contact={newContact}
                bind:this={contactComp}
              />
            </td>
            <td>
              <Input
                id="relationship"
                type="select"
                bind:value={newRelationship}
              >
                <option selected="selected">Mother</option>
                <option>Father</option>
                <option>Uncle</option>
                <option>Aunt</option>
                <option>Guardian</option>
                <option>Other</option>
              </Input>
            </td>
            <td>
              <Button
                id="addContactLink"
                color="success"
                on:click={() => addContact()}
              >
                <Icon name="plus-square" />
              </Button>
              <Tooltip target="addContactLink" placement="top">
                Add Contact
              </Tooltip>
            </td>
          </tr>
        </tbody>
      </Table>
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={close}>Back</Button>
    </ModalFooter>
  </Modal>
{/if}
