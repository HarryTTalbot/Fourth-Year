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
  header="User Guide - Today's Lessons"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the taking of attendance for today's lessons. <br /><br />

  In order to create a new lesson or modify the details of a lesson, please go
  to the "Manage Lessons" page in the "Admin" section of the application.
  <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Take attendance for a Lesson">
      In order to take attendance for a lesson you need to find the lesson in
      the table. Then press the "Take Attendance" button: <br /><br />

      <Button color="primary">Take Attendance</Button>

      <br /><br />

      This will open up a page which allows for the attendance of the lesson to
      be recorded or modified.
    </AccordionItem>
  </Accordion>
</Offcanvas>
