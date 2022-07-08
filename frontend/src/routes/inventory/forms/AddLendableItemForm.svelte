<script>
  import { createEventDispatcher } from "svelte";

  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import DateField from "../../../formFields/DateField.svelte";
  import IntegerField from "../../../formFields/IntegerField.svelte";

  import { createForm } from "svelte-forms-lib";
  import { defaultLendableItem, LENDABLEITEM_SCHEMA } from "./schemas";

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
    initialValues: defaultLendableItem(),
    validationSchema: LENDABLEITEM_SCHEMA,
    onSubmit: (values) => dispatch("submit", values),
  });

  /**
   * Function for handling a change to a wrapper input component.
   * Needed since `handleChange` can't find the corresponding DOM element...
   * @param {string} field The field to update.
   */
  function handleChangeComponent(field) {
    updateValidateField(field, $form[field]);
    console.log(field);
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
  <FormGroup>
    <Label for="name">Name</Label>
    <Input
      id="name"
      type="text"
      invalid={$errors.name}
      feedback={$errors.name}
      on:change={() => handleChangeComponent("name")}
      bind:value={$form.name}
    />
  </FormGroup>

  <FormGroup>
    <Label for="quantityAvailable">Quantity Available</Label>
    <Input
      id="quantityAvailable"
      invalid={$errors.quantityAvailable}
      feedback={$errors.quantityAvailable}
      on:change={() => handleChangeComponent("quantityAvailable")}
      bind:value={$form.quantityAvailable}
    />
  </FormGroup>
</form>
