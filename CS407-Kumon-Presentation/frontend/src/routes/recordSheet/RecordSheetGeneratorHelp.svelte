<script>
  import {
    Offcanvas,
    Icon,
    Tooltip,
    Button,
    Input,
    Accordion,
    AccordionItem,
  } from "sveltestrap";

  import StudentField from "../../formFields/StudentField.svelte";
  import ClassesField from "../../formFields/ClassField.svelte";

  export let open = false;
  const toggle = () => (open = !open);
</script>

<Offcanvas
  header="User Guide - Record Sheet Generator"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows record sheets to be created for one or more students over a
  period of up to a week. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Adding students to the list">
      Search boxes like the ones shown below are present on the page. Start
      typing the name of a student or class into the respective boxes, then
      click on the correct one when it appears.

      <br /><br />

      <StudentField />

      <br /><br />

      <ClassesField />

      <br /><br />

      A table at the top of the page will show all the students that have been
      selected <br /><br />
    </AccordionItem>

    <AccordionItem header="Generating a record sheet">
      In order to generate a record sheet, there must be at least one student
      selected. <br /><br />

      Below the student and class search boxes there are several fields. Fill
      these out with the desired options and then generate the record sheet with
      the Submit button like the one shown below: <br /><br />

      <Button color="primary">Submit</Button>

      <br /><br />

      Pressing this generates a PDF and downloads it, saving it to your
      computer. You can open and view it using your browser or your computer's
      file manager <br /><br />
    </AccordionItem>

    <AccordionItem header="Removing a student from the list">
      If you have added a student to the list by accident, you can remove them
      by clicking the <Icon name="trash" /> button next to their name. <br /><br
      />

      <!-- Next to the "Lesson Details" title there is the delete lesson button: <br/><br/> -->

      <Button id="removeStudentHelp" color="danger">
        <Icon name="trash" />
      </Button>
      <Tooltip target="removeStudentHelp" placement="top">Remove</Tooltip>

      <br /><br />

      This only affects the list of students the record sheet is being generated
      for; the student is still in the database
    </AccordionItem>
  </Accordion>
</Offcanvas>
