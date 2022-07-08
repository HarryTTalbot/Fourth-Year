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
  header="User Guide - Bulk Item Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of bulk item details. This
  includes adding, editing and removing bulk items. <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Editing a bulk item">
      In order to view additional information stored for a specific bulk item or
      edit its details, you will first need to find it in the table. If it does
      not appear on the list shown you can do the following:<br />
      <ul>
        <li>Search using the filter box</li>
        <Input placeholder="Filter Text" type="text" />
        <li>
          Navigate through the pages of bulk items using the "Next" and
          "Previous" buttons located on the top right corner of the table
        </li>
        <Button color="primary">Next</Button>
        <Button color="primary">Previous</Button>
      </ul>

      <br />

      Once you have found the bulk item, you can click on its row in the table,
      opening a modal allowing you to edit any associated details.
    </AccordionItem>

    <AccordionItem header="Adding a new bulk item">
      In order to add a new bulk item you have to click on the add bulk item
      button (shown below). This is located on the right of the screen. <br
      /><br />

      <Button id="addBulk ItemHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addBulk ItemHelp" placement="top">
        Add a New Bulk Item
      </Tooltip>

      <br /><br />

      This will open up a form allowing you to input the bulk item details. Once
      the details have been added, the "Add" button can be pressed. This will
      process the request and let you know if it was successful. <br /><br />

      There are some restrictions on the details which are to be stored (e.g.
      valid phone numbers). If an input is invalid, the box will be highlighted
      and a reason given below.
    </AccordionItem>

    <AccordionItem header="Withdrawing / Restocking Inventory">
      In order to update the databse with information regarding items being
      either removed from storage or restocked, first find the bulk item as
      described above. Once the bulk item has been found, use the "order" button
      to open a form allowing the type of order and number of items that have
      been restocked/withdrawn.
    </AccordionItem>

    <AccordionItem header="Deleting a bulk item">
      Next to the bulk item's name there are two buttons. One of these is the
      button to delete a bulk item: <br /><br />

      <Button color="danger" id="deleteBulk ItemHelp">
        <Icon name="trash" />
      </Button>
      <Tooltip target="deleteBulk ItemHelp" placement="top">
        Delete Bulk Item
      </Tooltip>

      <br /><br />

      Once pressed, it will ask for confirmation. If confirmation is given, the
      bulk item will be deleted.
    </AccordionItem>
  </Accordion>
</Offcanvas>
