<script>
  import { createEventDispatcher } from "svelte";
  import { Col, FormGroup, Input, Label, Row } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import { defaultLesson, LESSON_SCHEMA } from "./schemas";
  import DateField from "../../../formFields/DateField.svelte";
  import IntegerField from "../../../formFields/IntegerField.svelte";
  import ClassesField from "../../../formFields/ClassField.svelte";
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
    initialValues: defaultLesson(),
    validationSchema: LESSON_SCHEMA,
    onSubmit: (values) => dispatch("submit", values),
  });

  /**
   * The ID of the form, used for identifying the form in HTML.
   * @type {string}
   */
  export let id;

  /**
   * Function for handling a change to a wrapper input component.
   * Needed since `handleChange` can't find the corresponding DOM element...
   * @param {string} field The field to update.
   */
  function handleChangeComponent(field) {
    updateValidateField(field, $form[field]);
  }

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
  <!-- Date -->
  <FormGroup>
    <Label for="date">Date</Label>
    <DateField
      id="date"
      invalid={$errors.startDatetime}
      feedback={$errors.startDatetime}
      on:change={() => handleChangeComponent("startDatetime")}
      bind:date={$form.startDatetime}
    />
  </FormGroup>

  <Row>
    <!-- Start Time -->
    <Col>
      <FormGroup>
        <Label for="starttime">Start Time</Label>
        <Input
          id="starttime"
          type="time"
          invalid={$errors.starttime}
          feedback={$errors.starttime}
          on:change={handleChange}
          bind:value={$form.starttime}
        />
      </FormGroup>
    </Col>

    <!-- End Time -->
    <Col>
      <FormGroup>
        <Label for="endtime">End Time</Label>
        <Input
          id="endtime"
          type="time"
          invalid={$errors.endtime}
          feedback={$errors.endtime}
          on:change={handleChange}
          bind:value={$form.endtime}
        />
      </FormGroup>
    </Col>
  </Row>

  <!-- Class -->
  <FormGroup>
    <Label for="classFk">Class</Label>
    <ClassesField
      id="class"
      invalid={$errors.classFk}
      feedback={$errors.classFk}
      on:change={() => handleChangeComponent("classFk")}
      bind:classID={$form.classFk}
    />
  </FormGroup>

  <!-- Subject -->
  <FormGroup>
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
  </FormGroup>
</form>
