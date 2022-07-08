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
  header="User Guide - Lesson Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of lessons. This includes adding,
  editing and removing lessons. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Viewing a lesson">
      In order to view the information stored for a specific lesson you need to
      find them in the table. If they do not appear on the list shown you can do
      the following:<br />
      <ul>
        <li>Search based on their class and subject using the filter box</li>
        <Input placeholder="Filter Text" type="text" />
        <li>
          Navigate through the pages of lessons using the "Next" and "Previous"
          buttons located on the top right corner of the table
        </li>
        <Button color="primary">Next</Button>
        <Button color="primary">Previous</Button>
      </ul>

      <br />

      Once you have found the lesson, you can click on their row in the table to
      make their information appear below.

      <br /><br />

      This information includes the details of the lesson.
    </AccordionItem>

    <AccordionItem header="Adding a new lesson">
      In order to add a new lesson you have to click on the add lesson button
      (shown below). This is located on the right of the screen. <br /><br />

      <Button id="addLessonHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addLessonHelp" placement="top">Add a New Lesson</Tooltip>

      <br /><br />

      This will open up a form allowing you to input the details of the new
      lesson. Once the details have been added, the "Add Lesson" button can be
      pressed. This will process the request and let you know if it was
      successful. <br /><br />

      There are some restrictions on the details which are to be stored (e.g.
      start and end times). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>

    <AccordionItem header="Editing an existing lesson">
      In order to edit an existing lesson you have to first view their details
      (see "Viewing a lesson" section). <br /><br />

      Next to the "Details" section there is an edit button: <br /><br />

      <Button color="primary" id="editLessonHelp">
        <Icon name="pen" />
      </Button>
      <Tooltip target="editLessonHelp" placement="top">
        Edit Lesson Details
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where the details of the lesson can be
      changed. Once the details have been updated, the "Save Changes" can be
      pressed. This will process the request and let you know if it was
      successful. <br /><br />

      There are some restrictions on the details which can be updated (e.g.
      start and end times). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>

    <AccordionItem header="Deleting a lesson">
      In order to delete an existing lesson you have to first view their details
      (see "Viewing a lesson" section). <br /><br />

      Next to the "Lesson Details" title there is the delete lesson button:
      <br /><br />

      <Button color="danger" id="deleteLessonHelp">
        <Icon name="trash" />
      </Button>
      <Tooltip target="deleteLessonHelp" placement="top">Delete Lesson</Tooltip>

      <br /><br />

      Once pressed, it will ask for confirmation. If confirmation is given, the
      lesson will be deleted.
    </AccordionItem>
  </Accordion>
</Offcanvas>
