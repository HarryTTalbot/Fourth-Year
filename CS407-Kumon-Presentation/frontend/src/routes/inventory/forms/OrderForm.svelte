<script>
  import { createEventDispatcher } from "svelte";

  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import DateField from "../../../formFields/DateField.svelte";
  import IntegerField from "../../../formFields/IntegerField.svelte";
  import StaffField from "../../../formFields/StaffField.svelte";

  import { createForm } from "svelte-forms-lib";
  import { defaultWorksheetLog, WORKSHEETLOG_SCHEMA } from "./schemas";

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
    initialValues: defaultWorksheetLog(),
    validationSchema: WORKSHEETLOG_SCHEMA,
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
  <Col>
    <Label for="type">Type</Label>
    <Input
      id="type"
      type="select"
      invalid={$errors.type}
      feedback={$errors.type}
      on:change={() => handleChangeComponent("type")}
      bind:value={$form.type}
    >
      <option>Withdrawal</option>
      <option>Restock</option>
    </Input>
  </Col>

  <Col>
    <Label for="staffId">Staff Name</Label>
    <StaffField
      id="staffId"
      invalid={$errors.staffId}
      feedback={$errors.staffId}
      on:change={() => handleChangeComponent("staffId")}
      bind:staff={$form.staffId}
    />
  </Col>

  <FormGroup>
    <Label for="quantity">Quantity</Label>
    <Input
      id="quantity"
      invalid={$errors.quantity}
      feedback={$errors.quantity}
      on:change={() => handleChangeComponent("quantity")}
      bind:value={$form.quantity}
    />
  </FormGroup>
</form>
