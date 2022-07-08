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
  header="User Guide - Contact Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of contact details. This includes
  adding, editing and removing contact as well as managing their associated
  students. <br /><br />

  In order to manage the personal details of the associated students, please
  navigate to the "Manage Students" tab on this page. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Viewing a contact">
      In order to view the information stored for a specific contact you need to
      find them in the table. If they do not appear on the list shown you can do
      the following:<br />
      <ul>
        <li>
          Search based on their first name and last name using the filter box
        </li>
        <Input placeholder="Filter Text" type="text" />
        <li>
          Navigate through the pages of contact using the "Next" and "Previous"
          buttons located on the top right corner of the table
        </li>
        <Button color="primary">Next</Button>
        <Button color="primary">Previous</Button>
      </ul>

      <br />

      Once you have found the contact, you can click on their row in the table
      to make their information appear below. <br /><br />

      This information includes their personal details and associated students.<br
      /><br />

      In order to view the information of an associated student, select them
      from the drop down in the "Associated Students" section.
    </AccordionItem>

    <AccordionItem header="Adding a new contact">
      In order to add a new contact you have to click on the add contact button
      (shown below). This is located on the right of the screen. <br /><br />

      <Button id="addContactHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addContactHelp" placement="top">
        Add a New Contact
      </Tooltip>

      <br /><br />

      This will open up a form allowing you to input the contact details. Once
      the details have been added, the "Add" button can be pressed. This will
      process the request and let you know if it was successful. <br /><br />

      There are some restrictions on the details which are to be stored (e.g.
      valid phone numbers). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>

    <AccordionItem header="Editing a contact's details">
      In order to edit an existing contact you have to first view their details
      (see "Viewing a contact" section). <br /><br />

      Next to the "Details" section there is an edit button: <br /><br />

      <Button color="primary" id="editContactHelp">
        <Icon name="pen" />
      </Button>
      <Tooltip target="editContactHelp" placement="top">
        Edit Contact Details
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where the personal details of the contact
      can be changed. Once the details have been updated, the "Save Changes" can
      be pressed. This will process the request and let you know if it was
      successful. <br /><br />

      There are some restrictions on the details which can be updated (e.g.
      valid phone numbers). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>

    <AccordionItem header="Managing student relationships">
      In order to manage an existing contacts's associated students you have to
      first view their details (see "Viewing a contact" section). <br /><br />

      Next to the "Students" section there is an edit button: <br /><br />

      <Button color="primary" id="manageStudentsHelp">
        <Icon name="pen" />
      </Button>
      <Tooltip target="manageStudentsHelp" placement="top">
        Manage Associated Students
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where students can be added and removed.
      Every time a student is added or removed the interface will prompt whether
      the change was successful. <br /><br />

      There are some restrictions on the details which can be updated (e.g.
      valid phone numbers). If an input is invalid, the box will be highlighted
      and a reason given below. <br /><br />

      When adding a student you will have to search for them by entering their
      name into the search box.
    </AccordionItem>

    <AccordionItem header="Deleting a contact">
      In order to delete an existing contact you have to first view their
      details (see "Viewing a contact" section). <br /><br />

      Next to the contact's name there is the button to delete a contact:
      <br /><br />

      <Button color="danger" id="deleteContactHelp">
        <Icon name="trash" />
      </Button>
      <Tooltip target="deleteContactHelp" placement="top">
        Delete Contact
      </Tooltip>

      <br /><br />

      Once pressed, it will ask for confirmation. If confirmation is given, the
      contact will be deleted. Unlike with students, the personal details will
      not be kept for a set period of time. <br /><br />
    </AccordionItem>
  </Accordion>
</Offcanvas>
