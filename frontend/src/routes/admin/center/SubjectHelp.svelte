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

  export let open = false;
  const toggle = () => (open = !open);
</script>

<Offcanvas
  header="User Guide - Subject Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of subjects. This includes adding,
  editing and removing subjects. <br /><br />

  In order to manage the details of the Center, please navigate to the "Manage
  Center Details" tab. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <!-- Specific Guides -->
  <Accordion flush stayOpen>
    <AccordionItem header="Adding a new subject">
      In order to add a new subject you have to click on the add subject button
      (shown below). This is located on the right of the screen. <br /><br />

      <Button id="addSubjectHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addSubjectHelp" placement="top">
        Add a New Subject
      </Tooltip>

      <br /><br />

      This will open up a form allowing you to input the subject details. Once
      the details have been added, the "Add" button can be pressed. This will
      process the request and let you know if it was successful. <br /><br />

      There are some restrictions on the details which are to be stored (e.g.
      length of name). If an input is invalid, the box will be highlighted and a
      reason given below. <br /><br />

      There are no automatic levels added to a subject, so these will have to be
      added before the subject can be referenced.
    </AccordionItem>

    <AccordionItem header="Editing a subject">
      In order to edit an existing subject you have to first select it in the
      table. This will make details about the subject appear. <br /><br />

      The subject name can be edited through the text box and when complete,
      press the "Update Subject Name" button: <br /><br />

      <Button id="editSubjectHelp" color="primary">
        <Icon name="pen" />
      </Button>
      <Tooltip target="editSubjectHelp" placement="top">
        Update Subject Name
      </Tooltip>

      <br /><br />

      This will process the request and let you know if it was successful.
      <br /><br />

      There are some restrictions on the details which can be updated (e.g.
      length of name). If an input is invalid, the box will be highlighted and a
      reason given below.
    </AccordionItem>

    <AccordionItem header="Add a new subject level">
      In order to add a new subject level to an existing subject you have to
      first select the subject in the table. This will make details about the
      subject appear. <br /><br />

      At the bottom of the table of existing subject levels is a section to add
      a new subject level: <br /><br />

      <td>
        <Input type="text" />
      </td>
      <td>
        <Button id="addSubjectLevelHelp" color="success">
          <Icon name="plus-square" />
        </Button>
        <Tooltip target="addSubjectLevelHelp" placement="top">
          Add a New Subject Level
        </Tooltip>
      </td>

      <br /><br />

      Here you can add the name of the subject level to be created and when
      complete, press the add button. The interface will prompt whether the
      change was successful. <br /><br />

      There are some restrictions on the details which can be updated (e.g.
      length of name). If an input is invalid, the box will be highlighted and a
      reason given below. <br /><br />
    </AccordionItem>

    <AccordionItem header="Remove an existing subject level">
      In order to remove a subject level from an existing subject you have to
      first select the subject in the table. This will make details about the
      subject appear. <br /><br />

      Next to each subject level in the table, there is a "Remove subject level"
      button: <br /><br />

      <Button id="removeSubjectLevelHelp" color="danger">
        <Icon name="trash" />
      </Button>
      <Tooltip target="removeSubjectLevelHelp" placement="top">
        Remove the Subject Level
      </Tooltip>

      <br /><br />

      Once pressed, it will confirm if the deletion was successful. <br /><br />
    </AccordionItem>
  </Accordion>
</Offcanvas>
