<script>
  import { createEventDispatcher } from "svelte";

  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import DateField from "../../../formFields/DateField.svelte";
  import IntegerField from "../../../formFields/IntegerField.svelte";
  import SubjectsField from "../../../formFields/SubjectField.svelte";

  import { createForm } from "svelte-forms-lib";
  import { defaultWorksheet, WORKSHEET_SCHEMA } from "./schemas";

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
    initialValues: defaultWorksheet(),
    validationSchema: WORKSHEET_SCHEMA,
    onSubmit: (values) => dispatch("submit", values),
  });

  /**
   * Function for handling a change to a wrapper input component.
   * Needed since `handleChange` can't find the corresponding DOM element...
   * @param {string} field The field to update.
   */
  function handleChangeComponent(field) {
    updateValidateField(field, $form[field]);
  }

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
   * Function for resetting the values in the form.
   */
  export function reset() {
    handleReset();
  }
</script>

<form {id} {...$$restProps} on:submit={handleSubmit}>
  <Row>
    <Col>
      <Label for="subject">Subject</Label>
      <SubjectsField
        id="subject"
        idLevel="subject_level"
        invalidSubject={$errors.subject}
        invalidLevel={$errors.subjectLevel}
        feedbackSubject={$errors.subject}
        feedbackLevel={$errors.subjectLevel}
        on:change={() => handleChangeComponent("subject")}
        bind:subjectID={$form.subject}
        bind:levelID={$form.subjectLevel}
      />
    </Col>
  </Row>

  <Col>
    <Label for="set">Set</Label>
    <Input
      id="set"
      type="text"
      invalid={$errors.set}
      feedback={$errors.set}
      on:change={handleChange}
      bind:value={$form.set}
    />
  </Col>

  <FormGroup>
    <Label for="quantity">Quantity</Label>
    <Input
      id="quantity"
      type="number"
      invalid={$errors.quantity}
      feedback={$errors.quantity}
      on:change={() => handleChangeComponent("quantity")}
      bind:value={$form.quantity}
    />
  </FormGroup>
</form>
