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
  header="User Guide - Past Lessons"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of attendance from past lessons.
  This includes viewing and editing the attendance of previous lessons.
  <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Viewing a Lesson">
      In order to view the information on a lesson's attendance you need to find
      them in the table. If they do not appear on the list shown you can do the
      following:<br />
      <ul>
        <li>Search based on their class or subject using the filter box</li>
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

      This information includes the details of the lesson and the attendance
      recorded.
    </AccordionItem>

    <AccordionItem header="Modifying a Lesson's Attendance">
      In order to view or modify the attendance of a lesson, you need to first
      view the lesson (see "Viewing a Lesson" section). <br /><br />

      Once the lesson information appears, you simply press on the "View
      Attendance" button, which will open up the page to record attendance.
      <br />

      <Button color="primary">View Attendance</Button>

      <br /><br />

      On this page, any attendance record will be automatically loaded, and any
      changes can be saved.
    </AccordionItem>
  </Accordion>
</Offcanvas>
