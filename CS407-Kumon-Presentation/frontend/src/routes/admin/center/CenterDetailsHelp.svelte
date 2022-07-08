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
  header="User Guide - Center Details Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of the center details. <br /><br
  />

  In order to manage the subjects taught at the center, please navigate to the
  "Manage Subjects" tab on this page. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <!-- Specific Guides -->

  <Accordion flush stayOpen>
    <AccordionItem header="Editing the center details">
      In order to edit the center details you need to press the "Update Center
      Details" button:<br /><br />

      <Button id="editCenterHelp" color="primary">
        <Icon name="pen" />
      </Button>
      <Tooltip target="editCenterHelp" placement="top">
        Update Center Details
      </Tooltip>

      <br /><br />

      Pressing this opens up a form where the details can be changed. Once the
      details have been updated, the "Save Changes" can be pressed. This will
      process the request and let you know if it was successful. <br /><br />

      There are some restrictions on the details which can be updated (e.g.
      valid phone number). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>
  </Accordion>
</Offcanvas>
