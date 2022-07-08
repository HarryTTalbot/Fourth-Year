<script>
  import { createEventDispatcher } from "svelte";
  import { FormGroup, Input, Label } from "sveltestrap";

  import { createForm } from "svelte-forms-lib";
  import { defaultClass, CLASS_SCHEMA } from "./schemas";

  const dispatch = createEventDispatcher();

  const {
    form,
    errors,
    handleChange,
    handleReset,
    handleSubmit,
    updateInitialValues,
  } = createForm({
    initialValues: defaultClass(),
    validationSchema: CLASS_SCHEMA,
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
   * Function for resetting the values in the form.
   */
  export function reset() {
    handleReset();
  }
</script>

<form {id} {...$$restProps} on:submit={handleSubmit}>
  <!-- Class Name -->
  <FormGroup>
    <Label for="name">Class Name</Label>
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
