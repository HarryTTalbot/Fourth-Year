<script>
  import Select from "svelte-select";
  import { createEventDispatcher } from "svelte";
  import API_CONFIG from "../api";
  import { StudentsApi } from "kumon_app_backend_api";

  const dispatch = createEventDispatcher();

  // Link to backend api
  let studentsApi = new StudentsApi(API_CONFIG);

  /**
   * The ID of this input field.
   * @type {string}
   */
  export let id;
  /**
   * The ID of the student selected.
   * @type {int}
   */
  export let student;
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

  // The object of the current student selected
  let value;

  // Method to fetch the list of students and update the select box
  async function fetchStudents(filterText) {
    // Query the backend api
    let response = await studentsApi.studentsList({ search: filterText });
    response = response.results;

    let students = [];
    // Loop through students in response and add them to the dropdown
    for (let i = 0; i < response.length; i++) {
      students.push({
        value: response[i].id,
        label: response[i].lastName + ", " + response[i].firstName,
      });
    }

    // Search for the specific student
    if (student != "" && student != undefined && student != null) {
      response = await studentsApi.studentsRetrieve({ id: student });
      value = response.lastName + ", " + response.firstName;
    }

    return students;
  }

  // Method to handle a student being selected
  function handleSelect(event) {
    student = event.detail.value;
    invalid = false;
    dispatch("change", student); // Added to enable "on:change" functionality
  }

  // Method to handle a student no longer being selected
  export const handleClear = () => {
    value = null;
    student = null;
  };
</script>

{#await fetchStudents()}
  <p>Fetching a list of students...</p>
{:then}
  <div class="themed">
    <Select
      {id}
      loadOptions={fetchStudents}
      {value}
      hasError={invalid}
      on:select={handleSelect}
      on:clear={handleClear}
      placeholder="Search for a Student"
      noOptionsMessage="No Students Found"
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
