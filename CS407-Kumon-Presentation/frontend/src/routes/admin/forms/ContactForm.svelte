<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";

  import { createForm } from "svelte-forms-lib";
  import { defaultContact, CONTACT_SCHEMA } from "./schemas";

  const dispatch = createEventDispatcher();

  const {
    form,
    errors,
    handleChange,
    handleReset,
    handleSubmit,
    updateInitialValues,
  } = createForm({
    initialValues: defaultContact(),
    validationSchema: CONTACT_SCHEMA,
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

  <FormGroup>
    <Label for="phoneHome">Home Phone Number</Label>
    <Input
      id="phoneHome"
      type="text"
      invalid={$errors.phoneHome}
      feedback={$errors.phoneHome}
      on:change={handleChange}
      bind:value={$form.phoneHome}
    />
  </FormGroup>

  <FormGroup>
    <Label for="phoneBusiness">Business Phone Number</Label>
    <Input
      id="phoneBusiness"
      type="text"
      invalid={$errors.phoneBusiness}
      feedback={$errors.phoneBusiness}
      on:change={handleChange}
      bind:value={$form.phoneBusiness}
    />
  </FormGroup>

  <FormGroup>
    <Label for="phoneMobile">Mobile Phone Number</Label>
    <Input
      id="phoneMobile"
      type="text"
      invalid={$errors.phoneMobile}
      feedback={$errors.phoneMobile}
      on:change={handleChange}
      bind:value={$form.phoneMobile}
    />
  </FormGroup>

  <FormGroup>
    <Label for="email">Email Address</Label>
    <Input
      id="email"
      type="text"
      invalid={$errors.email}
      feedback={$errors.email}
      on:change={handleChange}
      bind:value={$form.email}
    />
  </FormGroup>

  <!-- Address -->
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
