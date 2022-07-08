<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import { defaultCenterDetails, CENTER_DETAILS_SCHEMA } from "./schemas";

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
    initialValues: defaultCenterDetails(),
    validationSchema: CENTER_DETAILS_SCHEMA,
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
  <h2>Center Details</h2>
  <!-- Center Name -->
  <FormGroup>
    <Label for="name">Center Name</Label>
    <Input
      id="name"
      type="text"
      invalid={$errors.name}
      feedback={$errors.name}
      on:change={handleChange}
      bind:value={$form.name}
    />
  </FormGroup>

  <!-- Center Phone Number -->
  <FormGroup>
    <Label for="phoneNumber">Center Phone Number</Label>
    <Input
      id="phoneNumber"
      type="text"
      invalid={$errors.phoneNumber}
      feedback={$errors.phoneNumber}
      on:change={handleChange}
      bind:value={$form.phoneNumber}
    />
  </FormGroup>

  <h2>Center Address</h2>
  <!-- Address - line one -->
  <FormGroup>
    <Label for="address.lineOne">Address Line 1</Label>
    <Input
      id="address.lineOne"
      type="text"
      invalid={$errors.address.lineOne}
      feedback={$errors.address.lineOne}
      on:change={handleChange}
      bind:value={$form.address.lineOne}
    />
  </FormGroup>

  <!-- Address - line two -->
  <FormGroup>
    <Label for="address.lineTwo">Address Line 2</Label>
    <Input
      id="address.lineTwo"
      type="text"
      invalid={$errors.address.lineTwo}
      feedback={$errors.address.lineTwo}
      on:change={handleChange}
      bind:value={$form.address.lineTwo}
    />
  </FormGroup>

  <!-- Address - line three -->
  <FormGroup>
    <Label for="address.lineThree">Address Line 3</Label>
    <Input
      id="address.lineThree"
      type="text"
      invalid={$errors.address.lineThree}
      feedback={$errors.address.lineThree}
      on:change={handleChange}
      bind:value={$form.address.lineThree}
    />
  </FormGroup>

  <!-- Address - city town -->
  <Row>
    <Col>
      <FormGroup>
        <Label for="address.cityTown">City/Town</Label>
        <Input
          id="address.cityTown"
          type="text"
          invalid={$errors.address.cityTown}
          feedback={$errors.address.cityTown}
          on:change={handleChange}
          bind:value={$form.address.cityTown}
        />
      </FormGroup>
    </Col>

    <!-- Address - province district -->
    <Col>
      <FormGroup>
        <Label for="address.provinceDistrict">County</Label>
        <Input
          id="address.provinceDistrict"
          type="text"
          invalid={$errors.address.provinceDistrict}
          feedback={$errors.address.provinceDistrict}
          on:change={handleChange}
          bind:value={$form.address.provinceDistrict}
        />
      </FormGroup>
    </Col>
  </Row>

  <!-- Address - post code -->
  <FormGroup>
    <Label for="address.postCode">Post Code</Label>
    <Input
      id="address.postCode"
      invalid={$errors.address.postCode}
      feedback={$errors.address.postCode}
      on:change={handleChange}
      bind:value={$form.address.postCode}
    />
  </FormGroup>

  <!-- Address - country -->
  <FormGroup>
    <Label for="address.country">Country</Label>
    <Input
      id="address.country"
      invalid={$errors.address.country}
      feedback={$errors.address.country}
      on:change={handleChange}
      bind:value={$form.address.country}
    />
  </FormGroup>
</form>
