<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import { defaultLogin, LOGIN_SCHEMA } from "./schemas";

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
    initialValues: defaultLogin(),
    validationSchema: LOGIN_SCHEMA,
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

  /**
   * Updates the error messages to display.
   * @param usernameError
   * @param passwordError
   */
  export function setErrors(usernameError, passwordError) {
    $errors.username = usernameError;
    $errors.password = passwordError;
  }
</script>

<form {id} {...$$restProps} on:submit={handleSubmit}>
  <!-- username -->
  <FormGroup>
    <Label for="username">Username</Label>
    <Input
      id="username"
      type="text"
      invalid={$errors.username}
      feedback={$errors.username}
      on:change={handleChange}
      bind:value={$form.username}
    />
  </FormGroup>

  <!-- password -->
  <FormGroup>
    <Label for="password">Password</Label>
    <Input
      id="password"
      type="password"
      invalid={$errors.password}
      feedback={$errors.password}
      on:change={handleChange}
      bind:value={$form.password}
    />
  </FormGroup>
</form>

<style>
  form {
    margin-left: auto;
    margin-right: auto;
    width: 100%;
    text-align: left;
  }
</style>
