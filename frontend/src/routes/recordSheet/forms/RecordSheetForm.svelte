<!--
@component
A reusable form component for student details.

Exported properties:
- `id`: The ID of this form.

Exported functions:
- `setDefaultValues(vals)`: Sets the default values displayed by this form.
- `reset()`: Resets the values displayed by this form.

Events:
- `submit(e)`: Raised when the form is submitted with validated data.
  - `e.detail`: Contains the validated values in this form.

Usage:

To use this component fully, you need to provide it with an ID, and also have a
backing variable to access the exported functions.

```html
<script>
  let myForm;

  // As this is bound to the component instance, we can do:
  // myForm.reset()
  // myForm.setDefaultValues({ ... })

  function handleSubmit(e) {
    // e.detail contains the validated values
  }
</script>
```

```tsx
<StudentForm id="my-form" bind:this={myForm} on:submit={handleSubmit} />
<button
  // Set the "form" attribute to the ID of the form above
  form="my-form" type="submit">
  Submit
</button>
```
-->
<script>
  import { createEventDispatcher } from "svelte";

  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import { defaultRecordSheet, RECORD_SHEET_SCHEMA } from "./schemas";
  import DateField from "../../../formFields/DateField.svelte";
  import IntegerField from "../../../formFields/IntegerField.svelte";
  import SubjectsField from "../../../formFields/SubjectField.svelte";



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
    initialValues: defaultRecordSheet(),
    validationSchema: RECORD_SHEET_SCHEMA,
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
    console.log("INSIDE OF FORM");
    console.log($form);
    console.log($form.starttime);
    console.log($form.endtme);
    updateInitialValues(values);
  }

  /**
   * Function for resetting the values in the form.
   */
  export function reset() {
    handleReset();
  }

  function datePlus(input, days) {
      let tempDate = new Date()
      tempDate.setDate(input.getDate() + parseInt(days));
      return tempDate;
  };

</script>

<form {id} {...$$restProps} on:submit={handleSubmit}>
  <Row>
    <Col>
      <Label for="date">Start Date</Label>
      <DateField
        id="date"
        invalid={$errors.startDate}
        feedback={$errors.startDate}
        on:change={() => handleChangeComponent("startDate")}
        bind:date={$form.startDate}
      />

      <Label for="days">Number of Days</Label>
      <IntegerField
        id="days"
        type="number"
        min={1}
        max={7}
        invalid={$errors.days}
        feedback={$errors.days}
        on:change={() => handleChangeComponent("days")}
        bind:value={$form.days}
      />
    </Col>

    <Col>
      <Label for="subject">Subject</Label>
      <SubjectsField
        id="subject"
        idLevel="subjectLevel"
        invalidSubject={$errors.subject}
        invalidLevel={$errors.subjectLevel}
        feedbackSubject={$errors.subject}
        feedbackLevel={$errors.subjectLevel}
        on:change={() => handleChangeComponent("subject")}
        bind:subjectID={$form.subject}
        bind:levelID={$form.subjectLevel}
      />
    </Col>
  </Row>
  <Row>
    <Col>
    <Label for="numSheets">Sheets Per Day</Label>
    <IntegerField
      id="numSheets"
      type="number"
      min={1}
      max={7}
      invalid={$errors.numSheets}
      feedback={$errors.numSheets}
      on:change={() => handleChangeComponent("numSheets")}
      bind:value={$form.numSheets}
    />

    </Col>
    <Col>

      <Label for="completionTime">Minutes to Complete</Label>
      <IntegerField
        id="completionTime"
        type="number"
        min={0}
        max={300}
        invalid={$errors.completionTime}
        feedback={$errors.completionTime}
        on:change={() => handleChangeComponent("completionTime")}
        bind:value={$form.completionTime}
      />
    </Col>
  </Row>
  <!-- <br>
  {#each {length: $form.days} as _, i}


    <Row>
    <Col xs="3">
    <Label for={'amount'+i}>{datePlus($form.startDate, i).toLocaleString('en-GB', {dateStyle: "short"})}</Label>
    </Col>
    <Col xs="3">
    <IntegerField
      id={'amount'+i}
      type="number"
      min={1}
      max={7}
      invalid={$errors.amount}
      feedback={$errors.amount}
      on:change={() => handleChangeComponent('amount')}
      bind:value={$form.amount}
    />
    </Col>
    </Row>
  {/each}
<br> -->

</form>
