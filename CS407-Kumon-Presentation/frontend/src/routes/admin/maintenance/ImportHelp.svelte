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

  This page allows the importing and exporting of data from the system. This
  includes both K-SIS exports as well as our own .kumon exports. <br /><br />

  If you wish to manage students and staff marked for deletion, navigate to the
  "Deleted Records" tab. <br /><br />

  Please press on the sections below to view their respective user guides:
  <br /><br />

  <!-- Specific Guides -->

  <Accordion flush stayOpen>
    <AccordionItem header="Importing Data">
      There are two kinds of files which can be imported by the system:<br />
      <ul>
        <li>The excel export file produced by K-SIS</li>
        <li>The .kumon database backup file produced by this system</li>
      </ul>

      <br />

      In order to import one of these file types you must fill out the form
      under the "Import Data" section. Ensure the import type is correct. Once
      the "Import" button is pressed, the system will import the data and prompt
      if it was successful.<br /><br />

      If the import was successful it will appear in the list at the bottom of
      the page.<br /><br />

      Importing data will simply add to the data already in the system, at most
      overwriting data where e.g. K-SIS IDs are the same.
    </AccordionItem>

    <AccordionItem header="Exporting Data">
      In order to export all data you need to press the "Export All Data"
      button. <br /><br />

      <Button color="primary">Export All Data</Button>

      <br /><br />

      This will generate a .kumon database backup file which will be
      automatically downloaded. <br /><br />

      This file can later be used as an import.
    </AccordionItem>

    <AccordionItem header="Downloading a Previous Import">
      At the bottom of the screen there is a list of all previous successful
      imports with some of their key information. Next to each import there is a
      button to allow it to be downloaded: <br /><br />

      <Button id="downloadImportHelp" color="primary">
        <Icon name="download" />
      </Button>
      <Tooltip target="downloadImportHelp" placement="top">Download</Tooltip>

      <br /><br />

      Pressing this will automatically download the file used in the import.
    </AccordionItem>
  </Accordion>
</Offcanvas>
