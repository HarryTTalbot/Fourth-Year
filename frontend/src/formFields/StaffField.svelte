<script>
	import Select from 'svelte-select';
  import { createEventDispatcher } from "svelte";
  import API_CONFIG from "../api";
  import { StaffApi } from "kumon_app_backend_api";

  const dispatch = createEventDispatcher();

  let staffApi = new StaffApi(API_CONFIG);

  /**
   * The ID of this input field.
   * @type {string}
   */
  export let id;
	/**
   * The ID of the staff selected.
   * @type {int}
   */
  export let staff;
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

	// The object of the current staff selected
  let value;

	// Method to fetch the list of students and update the select box
  async function fetchStaff(filterText) {
		let response = await staffApi.staffList({search:filterText});

		response = response.results;

		let staffList = [];
		// Loop through staff in response and add them to the dropdown
		for ( let i = 0; i < response.length; i++ ) {
			staffList.push({value : response[i].id, label : response[i].lastName + ", " + response[i].firstName});
		}

		// Search for the specific staff
		if( staff != "" && staff != undefined && staff != null){
			response = await staffApi.staffRetrieve({id: staff});
			value = response.lastName + ", " + response.firstName;
		}

		return staffList;
	}

	// Method to handle a staff being selected
  function handleSelect(event) {
    staff = event.detail.value;
		invalid = false;
		dispatch("change", staff); // Added to enable "on:change" functionality
  }

	// Method to handle a staff no longer being selected
	export const handleClear = () => {value = null; student = null;}

</script>
{#await fetchStaff()}
	<p> Fetching a list of staff... </p>
{:then}
	<div class="themed">
  <Select id={id} loadOptions={fetchStaff} value={value} hasError={invalid} on:select={handleSelect} on:clear={handleClear} placeholder="Search for a Staff Member" noOptionsMessage="No Staff Members Found"></Select>
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
    --errorBorder: 1px solid #dc3545;
  }
</style>
