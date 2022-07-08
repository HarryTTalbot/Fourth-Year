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
  header="User Guide - Item Manager"
  scroll
  isOpen={open}
  {toggle}
  backdrop={true}
  style="width: 25%"
>
  <!-- Page Description -->

  This page allows the viewing and management of lendable item and loan details.
  This includes adding, editing and removing items, loaning those items and
  confirming a return. <br /><br />

  <Accordion flush stayOpen>
    <AccordionItem header="Editing an item">
      In order to view additional information stored for a specific item or edit
      its details, you will first need to find it in the table. If it does not
      appear on the list shown you can do the following:<br />
      <ul>
        <li>Search using the filter box</li>
        <Input placeholder="Filter Text" type="text" />
        <li>
          Navigate through the pages of itmes using the "Next" and "Previous"
          buttons located on the top right corner of the table
        </li>
        <Button color="primary">Next</Button>
        <Button color="primary">Previous</Button>
      </ul>

      <br />

      Once you have found the item, you can click on its row in the table,
      opening a modal allowing you to edit any associated details.
    </AccordionItem>

    <AccordionItem header="Adding a new item">
      In order to add a new item you have to click on the add item button (shown
      below). This is located on the right of the screen. <br /><br />

      <Button id="addItemHelp" color="success">
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addItemHelp" placement="top">Add a New Item</Tooltip>

      <br /><br />

      This will open up a form allowing you to input the item details. Once the
      details have been added, the "Add" button can be pressed. This will
      process the request and let you know if it was successful.
    </AccordionItem>

    <AccordionItem header="Creating a new Loan">
      "Lendable Items" are not restocked and withdrawn. Instead, items are leant
      out to specific students. This can be carried out by using the "Lend Out"
      button for the appropriate item. <br /><br />

      <Button color="primary" id="lendItemHelp">Lend out</Button>
      <Tooltip target="lendItemHelp" placement="top">
        Lend out this item
      </Tooltip>

      Choose a student to associate this item with using the search input box,
      then fill in the form and submit. A corresponding loan will appear on the
      alternative tab.
    </AccordionItem>

    <AccordionItem header="Deleting a item">
      Next to the item's name there are two buttons. One of these is the button
      to delete a item: <br /><br />

      <Button color="danger" id="deleteItemHelp">
        <Icon name="trash" />
      </Button>
      <Tooltip target="deleteItemHelp" placement="top">Delete Item</Tooltip>

      <br /><br />

      Once pressed, it will ask for confirmation. If confirmation is given, the
      item will be deleted.
    </AccordionItem>

    <AccordionItem header="Returning an item">
      On the alternative tab, a list of all item loan logs will be displayed. To
      notfiy the database a loaned item has been returned, find the appropriate
      log and use the "return" button as shown below: <br /><br />

      <Button color="warning" id="itemReturn">Return</Button>
      <Tooltip target="itemReturn" placement="top">Return this item</Tooltip>

      <br /><br />

      Once pressed, the loan will be marked as completed, and will no longer be
      present in the list view.
    </AccordionItem>
  </Accordion>
</Offcanvas>
