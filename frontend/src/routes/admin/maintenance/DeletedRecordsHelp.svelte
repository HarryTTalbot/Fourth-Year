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
  header="User Guide - Deleted Records Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of deleted records. This includes
  restoring and permanently deletion staff anf students marked for deletion.
  <br /><br />

  In order to manage the imports and exports of data to or from the system,
  please navigate to the "Import/Export Data" tab. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <!-- Specific Guides -->

  <Accordion flush stayOpen>
    <AccordionItem header="Restoring a Student/Staff Record">
      In order to restore a student or staff record marked for deletion you have
      to first locate the record in the respective table. Once located, press
      the restore button in their row of the table:<br /><br />

      <Button id="restoreHelp" color="success">
        <Icon name="arrow-counterclockwise" />
      </Button>
      <Tooltip target="restoreHelp" placement="top">Restore</Tooltip>

      <br /><br />

      This will attempt to un-mark the student or staff record for deletion. A
      popup will appear detailing whether this process was successful.<br /><br
      />

      Once restored, the record will appear in the student or staff manager
      page.
    </AccordionItem>

    <AccordionItem header="Permanently deleting a Student/Staff Record">
      In order to permanently delete a student or staff record you have to first
      locate the record in the respective table. Once located, press the
      permanently delete button in their row of the table: <br /><br />

      <Button id="permanentlyDeleteHelp" color="danger">
        <Icon name="trash" />
      </Button>
      <Tooltip target="permanentlyDeleteHelp" placement="top">
        Permanently Delete
      </Tooltip>

      <br /><br />

      This will ask for confirmation. If given the request will be processed and
      a popup will appear detailing if it was successful. <br /><br />

      If the request was successful, the record will be deleted and cannot later
      be restored. <br /><br />

      A record will automatically be deleted on the "Permanent Deletion" date.
    </AccordionItem>
  </Accordion>
</Offcanvas>
