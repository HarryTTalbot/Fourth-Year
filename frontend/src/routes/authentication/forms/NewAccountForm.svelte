<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import { defaultNewAccount, NEW_ACCOUNT_SCHEMA } from "./schemas";

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
    initialValues: defaultNewAccount(),
    validationSchema: NEW_ACCOUNT_SCHEMA,
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
   * @param confirmPasswordError
   */
  export function setErrors(
    usernameError,
    passwordError,
    confirmPasswordError
  ) {
    $errors.username = usernameError;
    $errors.password = passwordError;
    $errors.confirmPassword = confirmPasswordError;
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

  <!-- confirm password -->
  <FormGroup>
    <Label for="confirmPassword">Confirm Password</Label>
    <Input
      id="confirmPassword"
      type="password"
      invalid={$errors.confirmPassword}
      feedback={$errors.confirmPassword}
      on:change={handleChange}
      bind:value={$form.confirmPassword}
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
