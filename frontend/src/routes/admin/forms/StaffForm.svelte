<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import { defaultStaff, STAFF_SCHEMA } from "./schemas";
  import DateField from "../../../formFields/DateField.svelte";

  const dispatch = createEventDispatcher();

  const {
    form,
    errors,
    handleChange,
    handleReset,
    handleSubmit,
    updateInitialValues,
    updateValidateField,
  } = createForm({
    initialValues: defaultStaff(),
    validationSchema: STAFF_SCHEMA,
    onSubmit: (values) => dispatch("submit", values),
  });

  /**
   * The ID of the form, used for identifying the form in HTML.
   * @type {string}
   */
  export let id;

  /**
   * Updates the default values to display.
   * @param values
   */
  export function setDefaultValues(values) {
    updateInitialValues(values);
  }

  /**
   * Function for handling a change to a wrapper input component.
   * Needed since `handleChange` can't find the corresponding DOM element...
   * @param {string} field The field to update.
   */
  function handleChangeComponent(field) {
    updateValidateField(field, $form[field]);
  }

  /**
   * Function for resetting the values in the form.
   */
  export function reset() {
    handleReset();
  }
</script>

<form {id} {...$$restProps} on:submit={handleSubmit}>
  <!-- First Name -->
  <FormGroup>
    <Label for="firstName">First Name</Label>
    <Input
      id="firstName"
      type="text"
      invalid={$errors.firstName}
      feedback={$errors.firstName}
      on:change={handleChange}
      bind:value={$form.firstName}
    />
  </FormGroup>

  <!-- Middle Name -->
  <FormGroup>
    <Label for="middleName">Middle Name</Label>
    <Input
      id="middleName"
      type="text"
      invalid={$errors.middleName}
      feedback={$errors.middleName}
      on:change={handleChange}
      bind:value={$form.middleName}
    />
  </FormGroup>

  <!-- Last Name -->
  <FormGroup>
    <Label for="lastName">Last Name</Label>
    <Input
      id="lastName"
      type="text"
      invalid={$errors.lastName}
      feedback={$errors.lastName}
      on:change={handleChange}
      bind:value={$form.lastName}
    />
  </FormGroup>

  <!-- Job Title -->
  <FormGroup>
    <Label for="jobTitle">Job Title</Label>
    <Input
      id="jobTitle"
      type="text"
      invalid={$errors.jobTitle}
      feedback={$errors.jobTitle}
      on:change={handleChange}
      bind:value={$form.jobTitle}
    />
  </FormGroup>

  <!-- Start Employment -->
  <FormGroup>
    <Label for="joinDate">Started Employment</Label>
    <DateField
      id="joinDate"
      invalid={$errors.joinDate}
      feedback={$errors.joinDate}
      on:change={() => handleChangeComponent("joinDate")}
      bind:date={$form.joinDate}
    />
  </FormGroup>

  <!-- End Employment -->
  <FormGroup>
    <Label for="leaveDate">Ended Employment</Label>
    <DateField
      id="leaveDate"
      invalid={$errors.leaveDate}
      feedback={$errors.leaveDate}
      on:change={() => handleChangeComponent("leaveDate")}
      bind:date={$form.leaveDate}
    />
  </FormGroup>
</form>
