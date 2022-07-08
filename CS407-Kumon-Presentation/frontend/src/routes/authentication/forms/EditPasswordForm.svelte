<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import { defaultEditPassword, EDIT_PASSWORD_SCHEMA } from "./schemas";

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
    initialValues: defaultEditPassword(),
    validationSchema: EDIT_PASSWORD_SCHEMA,
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
   * @param oldPasswordError
   * @param newPasswordError
   * @param confirmNewPasswordError
   */
  export function setErrors(
    oldPasswordError,
    newPasswordError,
    confirmNewPasswordError
  ) {
    $errors.oldPassword = oldPasswordError;
    $errors.newPassword = newPasswordError;
    $errors.confirmNewPassword = confirmNewPasswordError;
  }
</script>

<form {id} {...$$restProps} on:submit={handleSubmit}>
  <!-- old password -->
  <FormGroup>
    <Label for="oldPassword">Old Password</Label>
    <Input
      id="oldPassword"
      type="password"
      invalid={$errors.oldPassword}
      feedback={$errors.oldPassword}
      on:change={handleChange}
      bind:value={$form.oldPassword}
    />
  </FormGroup>

  <!-- new password -->
  <FormGroup>
    <Label for="newPassword">New Password</Label>
    <Input
      id="newPassword"
      type="password"
      invalid={$errors.newPassword}
      feedback={$errors.newPassword}
      on:change={handleChange}
      bind:value={$form.newPassword}
    />
  </FormGroup>

  <!-- confirm password -->
  <FormGroup>
    <Label for="confirmNewPassword">Confirm New Password</Label>
    <Input
      id="confirmNewPassword"
      type="password"
      invalid={$errors.confirmNewPassword}
      feedback={$errors.confirmNewPassword}
      on:change={handleChange}
      bind:value={$form.confirmNewPassword}
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
