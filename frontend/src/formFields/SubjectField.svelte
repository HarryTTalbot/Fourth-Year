<script>
  import Select from "svelte-select";
  import { createEventDispatcher } from "svelte";
  import { Label } from "sveltestrap";
  import API_CONFIG from "../api";
  import { SubjectApi } from "kumon_app_backend_api";

  const dispatch = createEventDispatcher();

  // Link to backend api
  let subjectsApi = new SubjectApi(API_CONFIG);

  /**
   * The ID of this input field.
   * @type {string}
   */
  export let id;
  export let idLevel;
  /**
   * The ID of the subject selected.
   * @type {int}
   */
  export let subjectID;
  /**
   * The ID of the subject Level selected.
   * @type {int}
   */
  export let levelID;
  /**
   * Whether the field is valid.
   * @type {bool}
   */
  export let invalidSubject = false;
  export let invalidLevel = false;
  /**
   * The feedback given to the user.
   * @type {string}
   */
  export let feedbackSubject;
  export let feedbackLevel;

  // The list of subjects
  let subjects = [];
  let subject = null;

  // The list of all subject levels
  let levels = [];
  let level = null;

  // Method to fetch the list of subjects and update the select box
  async function fetchSubjects(filterText) {
    // Query the backend api
    let response = await subjectsApi.subjectList({ filter: filterText });

    // Loop through subject in response and add them to the dropdown
    response.forEach(addToList);
    function addToList(item, index, arr) {
      subjects.push({ value: item.id, label: item.name });
      if (item.id == subjectID) {
        subject = item.name;
      }
    }
    if (subject != null) {
      await handleSelect({ detail: { value: subjectID } });
    }
  }

  // Method to handle a subject being selected
  async function handleSelect(event) {
    invalidSubject = false;

    // Fetch the levels for that subject
    let response = await subjectsApi.subjectGetLevelsList({
      id: event.detail.value,
    });

    // Loop through subject in response and add them to the dropdown
    response.forEach(addToList);
    function addToList(item, index, arr) {
      levels.push({ value: item.id, label: item.name });
      if (item.id == levelID) {
        level = item.name;
      }
    }
    subjectID = event.detail.value;
    dispatch("change", subjectID);
    console.log(levels);
  }

  // Method to handle a subject no longer being selected
  function handleClear() {
    subjectID = null;
    levelID = null;
    levels = [];
  }

  function handleSelectLevel(event) {
    levelID = event.detail.value;
    invalidLevel = false;
    dispatch("change", levelID);
  }

  // Method to handle a subject no longer being selected
  function handleClearLevel() {
    levelID = null;
  }
</script>

{#await fetchSubjects()}
  <p>Fetching a list of subjects...</p>
{:then}
  <div class="themed">
    <Select
      {id}
      items={subjects}
      value={subject}
      hasError={invalidSubject}
      on:select={handleSelect}
      on:clear={handleClear}
      placeholder="Select a Subject"
      noOptionsMessage="No Subjects Found"
    />
    {#if invalidSubject}
      <span class="error">{feedbackSubject}</span>
    {/if}
    {#if subjectID != null}
      <Label>Subject Level</Label>
      <Select
        id={idLevel}
        items={levels}
        value={level}
        hasError={invalidLevel}
        on:select={handleSelectLevel}
        on:clear={handleClearLevel}
        placeholder="Select a Subject Level"
        noOptionsMessage="No Subject Levels Found"
      />
      {#if invalidLevel}
        <span class="error">{feedbackLevel}</span>
      {/if}
    {/if}
  </div>
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
