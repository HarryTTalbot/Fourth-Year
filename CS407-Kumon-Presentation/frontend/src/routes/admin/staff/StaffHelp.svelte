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
  header="User Guide - Staff Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of staff details. This includes
  adding, editing and removing staff members as well as generating data reports.
  <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Viewing a staff member">
      In order to view the information stored for a specific staff member you
      need to find them in the table. If they do not appear on the list shown
      you can do the following:<br />
      <ul>
        <li>
          Search based on their first name and last name using the filter box
        </li>
        <Input placeholder="Filter Text" type="text" />
        <li>
          Navigate through the pages of staff members using the "Next" and
          "Previous" buttons located on the top right corner of the table
        </li>
        <Button color="primary">Next</Button>
        <Button color="primary">Previous</Button>
      </ul>

      <br />

      Once you have found the staff member, you can click on their row in the
      table to make their information appear below.

      <br /><br />

      This information includes their personal details.
    </AccordionItem>

    <AccordionItem header="Adding a new staff member">
      In order to add a new staff member you have to be logged in as the
      administrator. Then click on the add staff button (shown below). This is
      located on the right of the screen. <br /><br />

      <Button id="addStaffHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addStaffHelp" placement="top">
        Add a New Staff Member
      </Tooltip>

      <br /><br />

      This will open up a form allowing you to input the staff member details.
      Once the details have been added, the "Add" button can be pressed. This
      will open a new form to set the login details for the staff member. Once
      that form is complete the system will process the request and let you know
      if it was successful. <br /><br />

      There are some restrictions on the details which are to be stored (e.g.
      name length). If an input is invalid, the box will be highlighted and a
      reason given below.
    </AccordionItem>

    <AccordionItem header="Editing a staff member's details">
      In order to edit an existing staff member you have to first view their
      details (see "Viewing a staff member" section). <br /><br />

      Next to the "Details" section there is an edit button: <br /><br />

      <Button color="primary" id="editStaffHelp">
        <Icon name="pen" />
      </Button>
      <Tooltip target="editStaffHelp" placement="top">
        Edit Staff Member Details
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where the personal details of the staff
      member can be changed. Once the details have been updated, the "Save
      Changes" can be pressed. This will process the request and let you know if
      it was successful. <br /><br />

      There are some restrictions on the details which can be updated (e.g. name
      length). If an input is invalid, the box will be highlighted and a reason
      given below.
    </AccordionItem>

    <AccordionItem header="Resetting Password">
      In the eventuality that a staff member forgets their password, the
      administrator can override it to a new password. <br /> <br />

      In order to do this you have to first view their details (see "Viewing a
      staff member" section). <br /><br />

      Next to the staff member's name there are three buttons. The right most is
      the reset password button: <br /><br />

      <Button color="warning" id="forgotPasswordHelp">
        <Icon name="question-square" />
      </Button>
      <Tooltip target="forgotPasswordHelp" placement="top">
        Forgot Password
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where a new password can be set. One
      "Overwrite Password" is pressed the interface will prompt whether the
      change was successful. <br /><br />

      There are some restrictions on the new password (e.g. password length). If
      an input is invalid, the box will be highlighted and a reason given below.
    </AccordionItem>

    <AccordionItem header="Generating a PDF data report">
      In order to generate a PDF report on an existing staff member you have to
      first view their details (see "Viewing a staff member" section). <br /><br
      />

      Next to the staff member's name there are three buttons. One of these is
      the button to generate the report: <br /><br />

      <Button color="info" id="downloadStaffHelp">
        <Icon name="download" />
      </Button>
      <Tooltip target="downloadStaffHelp" placement="top">
        Download Staff Data Report
      </Tooltip>

      <br /><br />

      Once pressed, the report will be generated and automatically downloaded.
      <br /><br />

      This report contains all the information stored by the system for the
      staff member in question.
    </AccordionItem>

    <AccordionItem header="Deleting a student">
      In order to delete an existing staff member you have to first view their
      details (see "Viewing a staff member" section). <br /><br />

      Next to the staff member's name there are three buttons. One of these is
      the button to delete a student: <br /><br />

      <Button color="danger" id="deleteStaffHelp">
        <Icon name="trash" />
      </Button>
      <Tooltip target="deleteStaffHelp" placement="top">
        Delete Staff Member
      </Tooltip>

      <br /><br />

      Once pressed, it will ask for confirmation. If confirmation is given, the
      staff member will be marked for deletion. <br /><br />

      This does not delete the staff member from the system, as for GDPR their
      information is kept for a set period of time. To manage when they are
      permanently deleted you can visit the "Deleted Records" tab in the
      "Maintenance" admin page.
    </AccordionItem>
  </Accordion>
</Offcanvas>
