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
  header="User Guide - Student Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of student details. This includes
  adding, editing and removing students as well as generating data reports and
  managing their associated contacts. <br /><br />

  In order to manage the personal details of the associated contacts, please
  navigate to the "Manage Contacts" tab on this page. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Viewing a student">
      In order to view the information stored for a specific student you need to
      find them in the table. If they do not appear on the list shown you can do
      the following:<br />
      <ul>
        <li>
          Search based on their first name and last name using the filter box
        </li>
        <Input placeholder="Filter Text" type="text" />
        <li>
          Navigate through the pages of students using the "Next" and "Previous"
          buttons located on the top right corner of the table
        </li>
        <Button color="primary">Next</Button>
        <Button color="primary">Previous</Button>
      </ul>

      <br />

      Once you have found the student, you can click on their row in the table
      to make their information appear below.

      <br /><br />

      This information includes their personal details, associated contacts and
      the classes they are in. <br /><br />

      In order to view the personal details of an associated contact select them
      from the dropdown in the "Contacts" section.
    </AccordionItem>

    <AccordionItem header="Adding a new student">
      In order to add a new student you have to click on the add student button
      (shown below). This is located on the right of the screen. <br /><br />

      <Button id="addStudentHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addStudentHelp" placement="top">
        Add a New Student
      </Tooltip>

      <br /><br />

      This will open up a form allowing you to input the student details. Once
      the details have been added, the "Add" button can be pressed. This will
      process the request and let you know if it was successful. <br /><br />

      There are some restrictions on the details which are to be stored (e.g.
      valid phone numbers). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>

    <AccordionItem header="Editing a student details">
      In order to edit an existing student you have to first view their details
      (see "Viewing a student" section). <br /><br />

      Next to the "Details" section there is an edit button: <br /><br />

      <Button color="primary" id="editStudentHelp">
        <Icon name="pen" />
      </Button>
      <Tooltip target="editStudentHelp" placement="top">
        Edit Student Details
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where the personal details of the student
      can be changed. Once the details have been updated, the "Save Changes" can
      be pressed. This will process the request and let you know if it was
      successful. <br /><br />

      There are some restrictions on the details which can be updated (e.g.
      valid phone numbers). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>

    <AccordionItem header="Managing student contacts">
      In order to manage an existing student's contacts you have to first view
      their details (see "Viewing a student" section). <br /><br />

      Next to the "Contacts" section there is an edit button: <br /><br />

      <Button color="primary" id="manageContactsHelp">
        <Icon name="pen" />
      </Button>
      <Tooltip target="manageContactsHelp" placement="top">
        Manage Student Contacts
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where contacts can be added and removed.
      Every time a contact is added or removed the interface will prompt whether
      the change was successful. <br /><br />

      There are some restrictions on the details which can be updated (e.g.
      valid phone numbers). If an input is invalid, the box will be highlighted
      and a reason given below. <br /><br />

      When adding a contact you will have to search for them by entering their
      name into the search box.
    </AccordionItem>

    <AccordionItem header="Generating a PDF data report">
      In order to generate a PDF report on an existing student you have to first
      view their details (see "Viewing a student" section). <br /><br />

      Next to the student's name there are two buttons. One of these is the
      button to generate the report: <br /><br />

      <Button color="info" id="downloadStudentHelp">
        <Icon name="download" />
      </Button>
      <Tooltip target="downloadStudentHelp" placement="top">
        Download Student Data Report
      </Tooltip>

      <br /><br />

      Once pressed, the report will be generated and automatically downloaded.
      <br /><br />

      This report contains all the information stored by the system for the
      student in question.
    </AccordionItem>

    <AccordionItem header="Deleting a student">
      In order to delete an existing student you have to first view their
      details (see "Viewing a student" section). <br /><br />

      Next to the student's name there are two buttons. One of these is the
      button to delete a student: <br /><br />

      <Button color="danger" id="deleteStudentHelp">
        <Icon name="trash" />
      </Button>
      <Tooltip target="deleteStudentHelp" placement="top">
        Delete Student
      </Tooltip>

      <br /><br />

      Once pressed, it will ask for confirmation. If confirmation is given, the
      student will be marked for deletion. <br /><br />

      This does not delete the student from the system, as for GDPR their
      information is kept for a set period of time. To manage when they are
      permanently deleted you can visit the "Deleted Records" tab in the
      "Maintenance" admin page.
    </AccordionItem>
  </Accordion>
</Offcanvas>
