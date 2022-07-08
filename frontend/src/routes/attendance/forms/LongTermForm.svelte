<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import DateField from "../../../formFields/DateField.svelte";
  import StudentField from "../../../formFields/StudentField.svelte";
  import { defaultLongTerm, LONG_TERM_SCHEMA } from "./schemas";

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
    initialValues: defaultLongTerm(),
    validationSchema: LONG_TERM_SCHEMA,
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
  <!-- Student -->
  <FormGroup>
    <Label for="student">Student</Label>
    <StudentField
      id="student"
      invalid={$errors.student}
      feedback={$errors.student}
      on:change={() => handleChangeComponent("student")}
      bind:student={$form.student}
    />
  </FormGroup>

  <!-- Start of Absence -->
  <FormGroup>
    <Label for="startDate">Start</Label>
    <DateField
      id="startDate"
      invalid={$errors.startDate}
      feedback={$errors.startDate}
      on:change={() => handleChangeComponent("startDate")}
      bind:date={$form.startDate}
    />
  </FormGroup>

  <!-- End of Absence -->
  <FormGroup>
    <Label for="endDate">End</Label>
    <DateField
      id="endDate"
      invalid={$errors.endDate}
      feedback={$errors.endDate}
      on:change={() => handleChangeComponent("endDate")}
      bind:date={$form.endDate}
    />
  </FormGroup>

  <!-- Reason -->
  <FormGroup>
    <Label for="reason">Reason</Label>
    <Input
      id="reason"
      type="select"
      invalid={$errors.reason}
      feedback={$errors.reason}
      on:change={handleChange}
      bind:value={$form.reason}
    >
      <option>Illness/Injury</option>
      <option>Personal Circumstances</option>
      <option>Bereavement</option>
      <option>Holiday</option>
      <option>Other</option>
    </Input>
  </FormGroup>

  {#if $form.reason == "Other"}
    <FormGroup>
      <Label for="otherDetail">Other - please specify reason</Label>
      <Input
        id="otherDetail"
        type="text"
        invalid={$errors.otherDetail}
        feedback={$errors.otherDetail}
        on:change={handleChange}
        bind:value={$form.otherDetail}
      />
    </FormGroup>
  {/if}
</form>
