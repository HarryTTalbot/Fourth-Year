<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import { defaultAdminAccount, ADMIN_ACCOUNT_SCHEMA } from "./schemas";

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
    initialValues: defaultAdminAccount(),
    validationSchema: ADMIN_ACCOUNT_SCHEMA,
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
  <h3>Staff Details</h3>
  <!-- Staff Name -->
  <Row class="mb-3">
    <Col>
      <Label for="firstName">First Name</Label>
      <Input
        id="firstName"
        type="text"
        invalid={$errors.firstName}
        feedback={$errors.firstName}
        on:change={handleChange}
        bind:value={$form.firstName}
      />
    </Col>

    <Col>
      <Label for="middleName">Middle Name</Label>
      <Input
        id="middleName"
        type="text"
        invalid={$errors.middleName}
        feedback={$errors.middleName}
        on:change={handleChange}
        bind:value={$form.middleName}
      />
    </Col>

    <Col>
      <Label for="lastName">Last Name</Label>
      <Input
        id="lastName"
        type="text"
        invalid={$errors.lastName}
        feedback={$errors.lastName}
        on:change={handleChange}
        bind:value={$form.lastName}
      />
    </Col>
  </Row>

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

  <h3>Login Details</h3>
  <!-- Username -->
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

  <!-- Password -->
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

  <!-- Confirm Password -->
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

  <h3>Account Recovery Details</h3>
  <!-- Passcode -->
  <FormGroup>
    <Label for="passcode">Passcode</Label>
    <Input
      id="passcode"
      type="text"
      invalid={$errors.passcode}
      feedback={$errors.passcode}
      on:change={handleChange}
      bind:value={$form.passcode}
    />
  </FormGroup>

  <!-- Confirm Passcode -->
  <FormGroup>
    <Label for="confirmPasscode">Confirm Passcode</Label>
    <Input
      id="confirmPasscode"
      type="text"
      invalid={$errors.confirmPasscode}
      feedback={$errors.confirmPasscode}
      on:change={handleChange}
      bind:value={$form.confirmPasscode}
    />
  </FormGroup>
</form>
