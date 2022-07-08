<script>
  import {
    Offcanvas,
    Icon,
    Tooltip,
    Button,
    Input,
    Accordion,
    AccordionItem,
    Row,
    Col,
  } from "sveltestrap";
  import StudentField from "../../../formFields/StudentField.svelte";
  export let open = false;
  const toggle = () => (open = !open);
</script>

<Offcanvas
  header="User Guide - Taking/Changing Attendance"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of attendance for a lesson. This
  includes marking students as present, late, authorised absent or unauthorised
  absent. In addition, a PDF of the lesson attendance can be created to allow it
  to be filled out by hand. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Marking a student's status">
      There are four options for a student to be marked as:
      <ul>
        <li>Present (P)</li>
        <li>Late (L)</li>
        <li>Authorised Absence (A)</li>
        <li>Unauthorised Absence (U)</li>
      </ul>

      <br />

      To mark an individual student as one of these, simply find their name in
      the list and select the checkbox in the approprate column (example shown
      below). Which column represents which attendance status is detailed in the
      headings.

      <br /><br />
      <input type="radio" id="bigger" />

      <br /><br />

      To mark multiple students as one of the attendance statuses, simply press
      one of the buttons above the attendance table (shown below). These will
      mark all students who have not already been given a status as the
      specified status. <br /><br />

      <Row>
        <Col id="AllPHelp" style="text-align:center; margin-right:10px;">
          <Button color="primary">
            P <Icon name="check2" />
            <Tooltip target="AllPHelp" placement="top">Present</Tooltip>
          </Button>
        </Col>
        <Col id="AllLHelp" style="text-align:center; margin-right:10px;">
          <Button color="primary">
            L <Icon name="clock" />
            <Tooltip target="AllLHelp" placement="top">Late</Tooltip>
          </Button>
        </Col>
        <Col id="AllAHelp" style="text-align:center; margin-right:10px;">
          <Button color="primary">
            A <Icon name="calendar-check" />
            <Tooltip target="AllAHelp" placement="top">
              Authorised Absence
            </Tooltip>
          </Button>
        </Col>
        <Col id="AllUHelp" style="text-align:center">
          <Button color="primary">
            U <Icon name="x-lg" />
            <Tooltip target="AllUHelp" placement="top">
              Unauthorised Absence
            </Tooltip>
          </Button>
        </Col>
      </Row>

      <br /> <br />

      Note that any changes will not be saved until the submit button has been
      pressed.
    </AccordionItem>

    <AccordionItem header="Downloading a sheet to fill out">
      A pdf can be generated which contains a list of all the students in the
      lesson to take attendance with. <br /><br />

      In order to do this, you need to press the download button. This is
      located on the right of the screen. <br /><br />

      <Button id="DownloadAttendanceHelp" color="primary">
        <Icon name="download" />
      </Button>
      <Tooltip target="DownloadAttendanceHelp" placement="top">
        Download PDF of Attendance Sheet
      </Tooltip>

      <br /><br />

      This will automatically generate this pdf and download it.
    </AccordionItem>

    <AccordionItem header="Adding a Student to the Register">
      In order to add a new student to the attendance record for the lesson you
      need to use the add student component. <br /><br />

      First, you search for a student using the search student component. Here
      you can search by their name. <br /><br />

      <StudentField />

      <br /><br />

      Once a student has been selected, you can press the add button next to the
      search box. This will add the student to the register and mark them
      automatically as present. <br /><br />

      <Button id="AddStudentHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="AddStudentHelp" placement="top">
        Add Student To Register
      </Tooltip>

      <br /><br />

      A student who is already in the lesson's attendance record cannot be added
      again. In this eventuality, a popup window will open explaining the error.
    </AccordionItem>

    <AccordionItem header="Saving Attendance Records">
      In order to save modifications made to the attendance record you need to
      press the "Submit" button: <br /><br />

      <Button color="primary">Submit</Button>

      <br /><br />

      Once pressed, it will process the request and open a popup detailing
      whether it was successful. Please note that in order for a register to be
      saved, every student on it must have an attendance option selected.
    </AccordionItem>
  </Accordion>
</Offcanvas>

<style>
  input#bigger {
    transform: scale(1.5);
  }
</style>
