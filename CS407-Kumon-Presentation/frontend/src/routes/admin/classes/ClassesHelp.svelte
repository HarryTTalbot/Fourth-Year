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
  header="User Guide - Class Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of classes. This includes adding,
  editing and removing classes as well as managing the students assigned to each
  class. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Viewing a class">
      In order to view the information stored for a specific class you need to
      find them in the table. If they do not appear on the list shown you can do
      the following:<br />
      <ul>
        <li>Search based on their class name using the filter box</li>
        <Input placeholder="Filter Text" type="text" />
        <li>
          Navigate through the pages of classes using the "Next" and "Previous"
          buttons located on the top right corner of the table
        </li>
        <Button color="primary">Next</Button>
        <Button color="primary">Previous</Button>
      </ul>

      <br />

      Once you have found the class, you can click on their row in the table to
      make their information appear below.

      <br /><br />

      This information includes the name and size of the class along with the
      student in the class. <br /><br />

      In order to view the personal details of an a student in the class, select
      the student from the dropdown in the "Students" section.
    </AccordionItem>

    <AccordionItem header="Adding a new class">
      In order to add a new class you have to click on the add class button
      (shown below). This is located on the right of the screen. <br /><br />

      <Button id="addClassHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addClassHelp" placement="top">Add a New Class</Tooltip>

      <br /><br />

      This will open up a form allowing you to input the name of the class. Once
      the details have been added, the "Add Class" button can be pressed. This
      will process the request and let you know if it was successful. <br /><br
      />

      There are some restrictions on the details which are to be stored (length
      of name). If an input is invalid, the box will be highlighted and a reason
      given below.
    </AccordionItem>

    <AccordionItem header="Editing an existing class">
      In order to edit an existing class you have to first view their details
      (see "Viewing a class" section). <br /><br />

      Next to the "Details" section there is an edit button: <br /><br />

      <Button color="primary" id="editClassHelp">
        <Icon name="pen" />
      </Button>
      <Tooltip target="editClassHelp" placement="top">
        Edit Class Details
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where the name of the class can be changed.
      Once the details have been updated, the "Save Changes" can be pressed.
      This will process the request and let you know if it was successful.
      <br /><br />

      There are some restrictions on the details which can be updated (length of
      name). If an input is invalid, the box will be highlighted and a reason
      given below.
    </AccordionItem>

    <AccordionItem header="Managing students in an existing class">
      In order to manage the students in an existing class you have to first
      view their details (see "Viewing a class" section). <br /><br />

      Next to the "Students" section there is an edit button: <br /><br />

      <Button color="primary" id="manageStudentsHelp">
        <Icon name="pen" />
      </Button>
      <Tooltip target="manageStudentsHelp" placement="top">
        Manage Students
      </Tooltip>

      <br /><br />

      Pressing this opens up a popup where students can be added and removed
      from the class. Every time a student is added or removed the interface
      will prompt whether the change was successful. <br /><br />

      To add or remove a student you select the checkbox next to their name and
      press the add or remove button located in between the two tables:
      <br /><br />

      <Button id="Add_To_Class_Help" color="success"
        ><Icon name="arrow-bar-left" /></Button
      >
      <Tooltip target="Add_To_Class_Help" placement="top">Add To Class</Tooltip>
      <Button id="Remove_From_Class_Help" color="danger"
        ><Icon name="arrow-bar-right" /></Button
      >
      <Tooltip target="Remove_From_Class_Help" placement="bottom">
        Remove From Class
      </Tooltip>

      <br /><br />

      Multiple students can be selected at a time. If a student you wish to add
      does not appear in the rightmost list, you can change the page or search
      for them based on their name using the filter box. <br /><br />

      Once you have finished, return to the previous page with the "Close"
      button in the bottom left.
    </AccordionItem>

    <AccordionItem header="Deleting a class">
      In order to delete an existing class you have to first view their details
      (see "Viewing a class" section). <br /><br />

      Next to the "Class Details" title there is the delete the class button:
      <br /><br />

      <Button color="danger" id="deleteClassHelp">
        <Icon name="trash" />
      </Button>
      <Tooltip target="deleteClassHelp" placement="top">Delete Class</Tooltip>

      <br /><br />

      Once pressed, it will ask for confirmation. If confirmation is given, the
      class will be deleted.
    </AccordionItem>
  </Accordion>
</Offcanvas>
