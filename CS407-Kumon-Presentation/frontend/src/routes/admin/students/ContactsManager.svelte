<script>
  import { onMount } from "svelte";
  import { openModal } from "svelte-modals";
  import {
    Button,
    Container,
    Table,
    Row,
    Col,
    Icon,
    Tooltip,
  } from "sveltestrap";
  import { tick } from "svelte";

  import API_CONFIG from "../../../api";
  import { ContactsApi } from "kumon_app_backend_api";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../../components/PaginationFilteringBar.svelte";

  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import AddContactModal from "./modals/AddContactModal.svelte";
  import EditContactModal from "./modals/EditContactModal.svelte";
  import ManageStudentsModal from "./modals/ManageStudentsModal.svelte";
  import InfoModal from "../../../modals/InfoModal.svelte";

  import ContactDetails from "./ContactDetails.svelte";
  import ContactHelp from "./ContactsHelp.svelte";

  /**
   * The contacts API instance in use.
   * @type {ContactsApi}
   */
  let contactsApi = new ContactsApi(API_CONFIG);

  /**
   * List of contacts associated with the chosen student
   */
  let contacts = [];

  /**
   * Whether the request has terminated.
   * @type {boolean}
   */
  let isRefreshing = false;

  /**
   * The ID of the contact selected.
   * @type {number}
   */
  let selectedContact;

  /**
   * Pagination filtering bar
   */
  let pageFilterDetails = new PageFilter();

  /**
   * Whether the help accordian is open or not.
   * @type {boolean}
   */
  let openHelp = false;

  /**
   * Refreshes the list of contacts.
   */
  async function refreshContacts() {
    isRefreshing = true;

    try {
      let response = await contactsApi.contactsList({
        page: pageFilterDetails.page,
        search: pageFilterDetails.filter,
      });
      contacts = response.results;

      pageFilterDetails.pageUpdate(response);
      pageFilterDetails.filter += " ";
      pageFilterDetails.filter = pageFilterDetails.filter.substring(
        0,
        pageFilterDetails.filter.length - 1
      );
    } catch (e) {
      openModal(InfoModal, {
        title: "Contacts List",
        message: `Could not load list of contacts!`,
      });
    }

    isRefreshing = false;
  }

  /**
   * Handler for adding a new contact.
   */
  function handleAddContact() {
    openModal(AddContactModal, {
      onAdd: async (_) => {
        await refreshContacts();
      },
    });
  }

  /**
   * Handler for viewing a contact
   * @param {number} id The ID of the contact.
   */
  async function handleViewContactDetails(id) {
    if (selectedContact === id) {
      selectedContact = undefined;
    } else {
      selectedContact = undefined;
      await tick();
      selectedContact = id;
    }
  }

  /**
   * Handler for viewing a contact
   * @param {details} event matches the api endpoint for the contact
   */
  function handleEdit(event) {
    let existingIndex = contacts.findIndex(
      (contact) => contact.id === event.detail.contactId
    );

    if (existingIndex >= 0) {
      contacts[existingIndex] = {
        id: event.detail.contactId,
        firstName: event.detail.newDetails.firstName,
        middleName: event.detail.newDetails.middleName,
        lastName: event.detail.newDetails.lastName,
      };
    }
  }

  /**
   * Handler for deleting a contact
   * @param {details} event matches the api endpoint for the contact
   */
  async function handleDelete(event) {
    selectedContact = undefined;
    await refreshContacts();
    await tick();
  }

  async function handleCloseView() {
    selectedContact = undefined;
    await tick();
  }

  onMount(async () => {
    await refreshContacts();
  });
</script>

<Container class="p-3">
  <Row>
    <Col>
      <h1>Contacts Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpContact"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpContact" placement="top">
        User Guide for Contacts Manager
      </Tooltip>
    </Col>
  </Row>
  <Row>
    <Col>
      <h2>Contacts List</h2>
    </Col>

    <Col>
      <Button
        id="addContact"
        color="success"
        style="float: right;"
        on:click={() => handleAddContact()}
      >
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addContact" placement="top">Add a New Contact</Tooltip>
    </Col>
  </Row>

  <PaginationFilteringBar
    refresh={() => refreshContacts()}
    pageFilter={pageFilterDetails}
  />

  <Table>
    <thead>
      <tr>
        <th style="width: 25%">First Name</th>
        <th style="width: 25%">Middle Name</th>
        <th style="width: 25%">Last Name</th>
        <th style="width: 25%">Email</th>
      </tr>
    </thead>

    {#if isRefreshing}
      <tfoot class="info">
        <tr>
          <td colspan="5">Retrieving list of contacts...</td>
        </tr>
      </tfoot>
    {:else if contacts.length === 0}
      <tfoot class="info">
        <tr>
          <td colspan="5">No contact data found</td>
        </tr>
      </tfoot>
    {:else}
      <tbody>
        {#each contacts as contact}
          <tr
            class:selected={selectedContact === contact.id}
            on:click={() => handleViewContactDetails(contact.id)}
          >
            <td>{contact.firstName}</td>
            <td>{contact.middleName}</td>
            <td>{contact.lastName}</td>
            <td>{contact.email}</td>
          </tr>
        {/each}
      </tbody>
    {/if}
  </Table>

  {#if selectedContact}
    <ContactDetails
      contactId={selectedContact}
      on:edit={handleEdit}
      on:delete={handleDelete}
      on:close={handleCloseView}
    />
  {/if}

  <ContactHelp bind:open={openHelp} />
</Container>

<style>
  /* Centre any footers displaying information */
  tfoot.info > tr > td {
    text-align: center;
  }
  .selected {
    background-color: #6c757d;
    color: white;
  }
  tbody tr:hover {
    background-color: #6c757d;
    color: white;
  }
</style>
