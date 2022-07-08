<script>
  import { createEventDispatcher } from "svelte";

  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import DateField from "../../../formFields/DateField.svelte";
  import IntegerField from "../../../formFields/IntegerField.svelte";

  import { createForm } from "svelte-forms-lib";
  import { defaultStudent, STUDENT_SCHEMA } from "./schemas";

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
    initialValues: defaultStudent(),
    validationSchema: STUDENT_SCHEMA,
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
  <!-- Student Details -->
  <FormGroup>
    <Label for="kSisId">K-SIS ID</Label>
    <IntegerField
      id="kSisId"
      type="number"
      invalid={$errors.kSisId}
      feedback={$errors.kSisId}
      on:change={() => handleChangeComponent("kSisId")}
      bind:value={$form.kSisId}
    />
  </FormGroup>

  <!-- Student Name -->
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
    <Label for="dateOfBirth">Date of Birth</Label>
    <DateField
      id="dateOfBirth"
      invalid={$errors.dateOfBirth}
      feedback={$errors.dateOfBirth}
      on:change={() => handleChangeComponent("dateOfBirth")}
      bind:date={$form.dateOfBirth}
    />
  </FormGroup>

  <!-- Join/Leave Date -->
  <Row class="mb-3">
    <Col>
      <Label for="joinDate">Join Date</Label>
      <DateField
        id="joinDate"
        invalid={$errors.joinDate}
        feedback={$errors.joinDate}
        on:change={() => handleChangeComponent("joinDate")}
        bind:date={$form.joinDate}
      />
    </Col>

    <Col>
      <Label for="leaveDate">Leave Date</Label>
      <DateField
        id="leaveDate"
        invalid={$errors.leaveDate}
        feedback={$errors.leaveDate}
        on:change={() => handleChangeComponent("leaveDate")}
        bind:date={$form.leaveDate}
      />
    </Col>
  </Row>

  <FormGroup>
    <Label for="phoneNumber">Phone Number</Label>
    <Input
      id="phoneNumber"
      type="text"
      invalid={$errors.phoneNumber}
      feedback={$errors.phoneNumber}
      on:change={handleChange}
      bind:value={$form.phoneNumber}
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

  <FormGroup>
    <Label for="school">School</Label>
    <Input
      id="school"
      type="text"
      invalid={$errors.school}
      feedback={$errors.school}
      on:change={handleChange}
      bind:value={$form.school}
    />
  </FormGroup>

  <FormGroup>
    <Label for="grade">Grade</Label>
    <Input
      id="grade"
      type="text"
      invalid={$errors.grade}
      feedback={$errors.grade}
      on:change={handleChange}
      bind:value={$form.grade}
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
