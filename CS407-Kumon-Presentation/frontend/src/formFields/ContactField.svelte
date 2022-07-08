<script>
  import Select from "svelte-select";
  import { createEventDispatcher } from "svelte";
  import API_CONFIG from "../api";
  import { ContactsApi } from "kumon_app_backend_api";

  const dispatch = createEventDispatcher();

  // Link to contacts backend api
  let contactsApi = new ContactsApi(API_CONFIG);

  /**
   * The ID of this input field.
   * @type {string}
   */
  export let id;
  /**
   * The ID of the contact selected.
   * @type {int}
   */
  export let contact;
  /**
   * Whether the field is valid.
   * @type {bool}
   */
  export let invalid = false;
  /**
   * The feedback given to the user.
   * @type {string}
   */
  export let feedback;

  // The object of the current contact selected
  let value;

  // Method to fetch the list of contact and update the select box
  async function fetchContacts(filterText) {
    // Query the backend
    let response = await contactsApi.contactsList({ search: filterText });
    response = response.results;

    let contacts = [];
    // Loop through contacts in response and add them to the dropdown
    for (let i = 0; i < response.length; i++) {
      contacts.push({
        value: response[i].id,
        label: response[i].lastName + ", " + response[i].firstName,
      });
    }

    // Search for the specific contact
    if (contact != "" && contact != undefined && contact != null) {
      response = await contactsApi.contactsRetrieve({ id: contact });
      value = response.lastName + ", " + response.firstName;
    }

    return contacts;
  }

  // Method to handle a contact being selected
  function handleSelect(event) {
    contact = event.detail.value;
    invalid = false;
  }

  // Method to handle a contact no longer being selected
  export const handleClear = () => {
    value = null;
    contact = null;
  };
</script>

{#await fetchContacts()}
  <p>Fetching a list of contacts...</p>
{:then}
  <div class="themed">
    <Select
      {id}
      loadOptions={fetchContacts}
      {value}
      hasError={invalid}
      on:select={handleSelect}
      on:clear={handleClear}
      placeholder="Search for a Contact"
      noOptionsMessage="No Contacts Found"
    />
  </div>
  {#if invalid}
    <span class="error">{feedback}</span>
  {/if}
{/await}

<style>
  .error {
    display: block;
    font-size: 14px;
    color: #dc3545;
  }
  .themed {
    --height: 38px;
    --clearSelectTop: 0px;
    --clearSelectBottom: 0px;
    --errorBorder: 1px solid #dc3545;
  }
</style>
