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
  header="User Guide - Long Term Absences Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of long term absences. This
  includes adding, editing and removing long term absences. <br /><br />

  Any student who has a long term absence marked for them will automatically be
  marked as authorised absence (A) for any lesson during the absence. <br /><br
  />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Viewing a Long Term Absence">
      In order to view the information stored for a specific long term absence
      you need to find them in the table. If they do not appear on the list
      shown you can do the following:<br />
      <ul>
        <li>Search based on the student's name using the filter box</li>
        <Input placeholder="Filter Text" type="text" />
        <li>
          Navigate through the pages of long term absences using the "Next" and
          "Previous" buttons located on the top right corner of the table
        </li>
        <Button color="primary">Next</Button>
        <Button color="primary">Previous</Button>
      </ul>

      <br />

      Once you have found the long term absence, you can click on their row in
      the table to make their information appear below.

      <br /><br />

      This information includes the details of the absence.
    </AccordionItem>

    <AccordionItem header="Adding a new Long Term Absence">
      In order to add a new long term absence you have to click on the add long
      term absence button (shown below). This is located on the right of the
      screen. <br /><br />

      <Button id="addLongTermHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addLongTermHelp" placement="top">
        Add a New Long Term Absence
      </Tooltip>

      <br /><br />

      This will open up a form allowing you to input the details of the new
      absence. Once the details have been added, the "Add Long Term Absence"
      button can be pressed. This will process the request and let you know if
      it was successful. <br /><br />

      There are some restrictions on the details which are to be stored (e.g.
      start and end dates). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>

    <AccordionItem header="Editing an existing Long Term Absence">
      In order to edit an existing absence you have to first view their details
      (see "Viewing a Long Term Absence" section). <br /><br />

      Next to the "Details" section there is an edit button: <br /><br />

      <Button color="primary" id="editLongTermHelp">
        <Icon name="pen" />
      </Button>
      <Tooltip target="editLongTermHelp" placement="top">
        Edit Long Term Absence Details
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where the details of the absence can be
      changed. Once the details have been updated, the "Save Changes" can be
      pressed. This will process the request and let you know if it was
      successful. <br /><br />

      There are some restrictions on the details which can be updated (e.g.
      start and end dates). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>

    <AccordionItem header="Deleting a Long Term Absence">
      In order to delete an existing absence you have to first view their
      details (see "Viewing a Long Term Absence" section). <br /><br />

      Next to the "Long Term Absence Details" title there is the delete long
      term absence button: <br /><br />

      <Button color="danger" id="deleteLongTermHelp">
        <Icon name="trash" />
      </Button>
      <Tooltip target="deleteLongTermHelp" placement="top">
        Delete Long Term Absence
      </Tooltip>

      <br /><br />

      Once pressed, it will ask for confirmation. If confirmation is given, the
      long term absence will be deleted.
    </AccordionItem>
  </Accordion>
</Offcanvas>
