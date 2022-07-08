<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import { defaultSubject, SUBJECT_SCHEMA } from "./schemas";
  import DateField from "../../../formFields/DateField.svelte";
  import IntegerField from "../../../formFields/IntegerField.svelte";
  import ClassesField from "../../../formFields/ClassField.svelte";
  import SubjectsField from "../../../formFields/SubjectField.svelte";

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
    initialValues: defaultSubject(),
    validationSchema: SUBJECT_SCHEMA,
    onSubmit: (values) => dispatch("submit", values),
  });

  /**
   * The ID of the form, used for identifying the form in HTML.
   * @type {string}
   */
  export let id;

  /**
   * Function for handling a change to a wrapper input component.
   * Needed since `handleChange` can't find the corresponding DOM element...
   * @param {string} field The field to update.
   */
  function handleChangeComponent(field) {
    updateValidateField(field, $form[field]);
  }

  /**
   * Updates the default values to display.
   * @param values
   */
  export function setDefaultValues(values) {
    updateInitialValues(values);
  }

  /**
   * Function for resetting the values in the form.
   */
  export function reset() {
    handleReset();
  }
</script>

<form {id} {...$$restProps} on:submit={handleSubmit}>
  <!-- End Time -->
  <FormGroup>
    <Label for="name">Subject Name</Label>
    <Input
      id="name"
      type="text"
      invalid={$errors.name}
      feedback={$errors.name}
      on:change={handleChange}
      bind:value={$form.name}
    />
  </FormGroup>
</form>
