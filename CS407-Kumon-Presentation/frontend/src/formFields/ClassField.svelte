<script>
  import Select from "svelte-select";
  import { createEventDispatcher } from "svelte";
  import API_CONFIG from "../api";
  import { ClassesApi } from "kumon_app_backend_api";

  const dispatch = createEventDispatcher();

  // Link to classes backend api
  let classesApi = new ClassesApi(API_CONFIG);

  /**
   * The ID of this input field.
   * @type {string}
   */
  export let id;
  /**
   * The ID of the class selected.
   * @type {int}
   */
  export let classID;
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
  // Value of the select statement
  let value;

  // Method to fetch the list of students and update the select box
  async function fetchClasses(filterText) {
    // Query the backend api
    let response;
    response = await classesApi.classesList({ search: filterText });
    response = response.results;

    let classes = [];
    // Loop through classes in response and add them to the dropdown
    for (let i = 0; i < response.length; i++) {
      classes.push({ value: response[i].id, label: response[i].name });
    }

    // Search for the specific class
    if (classID != "" && classID != undefined && classID != null) {
      response = await classesApi.classesRetrieve({ id: classID });
      value = response.name;
    }

    return classes;
  }

  // Method to handle a class being selected
  function handleSelect(event) {
    classID = event.detail.value;

    invalid = false;
    dispatch("change", classID);
  }

  // Method to handle a class no longer being selected
  export const handleClear = () => {
    value = null;
    classID = null;
  };
</script>

{#await fetchClasses()}
  <p>Fetching a list of classes...</p>
{:then}
  <div class="themed">
    <Select
      {id}
      loadOptions={fetchClasses}
      {value}
      hasError={invalid}
      on:select={handleSelect}
      on:clear={handleClear}
      placeholder="Search for a Class"
      noOptionsMessage="No Classes Found"
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
