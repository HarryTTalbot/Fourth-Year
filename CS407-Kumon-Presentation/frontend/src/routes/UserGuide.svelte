<script>
  import { Container, Accordion, AccordionItem } from "sveltestrap";
  import { createEventDispatcher } from "svelte";
</script>

<Container>
  The application interface is split into the following five sections: <br /><br
  />

  <Accordion flush stayOpen>
    <AccordionItem header="Dashboard">
      <p>
        The dashboard or home page is the default page loaded up when someone
        logs in. This page contains some information and links to commonly used
        features of the application.
      </p>

      <hr />
      <p>It is split into four sections:</p>

      <h6>Right now</h6>

      <p>
        This shows information about the lesson which is happening at the moment
        (if there is one) and the next lesson. It also provides a link to take
        attendance for the current lesson.
      </p>

      <hr />
      <h6>Today's Lessons</h6>

      <p>This shows a list of all lessons taking place today.</p>

      <hr />
      <h6>Inventory</h6>

      <p>
        This displays the list of lendable item logs, anonymised using student and item IDs.
        To view more details, navigate to "Manage Lendable Items" under the "Inventory" drop down.
      </p>

      <hr />
      <h6>User Guide</h6>

      <p>
        This gives information on how to access the user guide of any page and a
        link to view the user guide of the application as a whole.
      </p>
    </AccordionItem>

    <AccordionItem header="Attendance">
      <h6>Today's Lessons</h6>

      <p>
        The "Today's Lessons" page contains a list of all the lessons present
        in the database that have been scheduled for today.
      </p>

      <p>
        Attendance can be taken for any lesson that is scheduled for today,
        regardless of time of day.
      </p>

      <p>
        Attendance can be taken for a chosen lesson using the supplied interface.
        The lesson can only be submitted to the database if it has had all students marked as
        one of the four options:
        <ul>
         <li>Present</li>
         <li>Late</li>
         <li>Authorised Absence</li>
         <li>Unauthorised Absence</li>
        </ul>
      <!-- </p> -->

      <hr />
      <h6>Past Lessons</h6>

      <p>
       Past attendance records can be viewed using the "Past Lessons" page.
       This allows the details for each lesson to be viewed, including when the
       attendance was first recorded, and when it was last modified.
      </p>

      <p>
        Attendance can be viewed and modified using the view attendance button after choosing a specific lesson.
      </p>

      <hr />
      <h6>Long Term Absences</h6>

      <p>
        The Long Term Absence Manager can be used to add, edit or remove long term absence records.
        Each record is associated with a student, and needs a reason associated with it alongside a date range.
      </p>

      <p>
        When a student is marked as having an authorised absence, they will
        default to the "authorised absence" option in any lesson attendances
        within the specific range.
      </p>
    </AccordionItem>

    <AccordionItem header="Inventory">
      <h6>Manage Worksheets</h6>

      <p>
        The worksheet manager allows worksheets to be added, edited and deleted.
        Each worksheet must be associated with a specific subject and level.
      </p>

      <p>
        Worksheets can be either "restocked" or "withdrawn", allowing loans to be
        input into the database.
        These loans must be associated with a specific staff member.
      </p>

      <hr />
      <h6>Manage Bulk Items</h6>

      <p>
        The bulk item manager can be used for managing any miscellaneous items that
        may be overseen by the Kumon centre.
        Items can be added, edited or deleted using the interface.
      </p>

      <p>
        Bulk items do not need to be associated with a specific subject.
      </p>

      <p>
        Bulk items can be either "restocked" or "withdrawn", allowing loans to be
        input into the database.
        These loans must be associated with a specific staff member.
      </p>

      <hr />
      <h6>Manage Lendable Items</h6>

      <p>
        The lendable items manager can be used to manage specific item loans.
        Items for this purpose can be added, edited and deleted using the interface.
      <p/>

      <p>
        When an item is loaned out, a log will be generated. An interface for managing loans
        is present on the alternative tab using these logs.
        When the item has been returned, that can be reflected in the page.
      </p>

    </AccordionItem>

    <AccordionItem header="Record Sheets">

      <p> The Record Sheet Generator allows you to add individuals or whole classes to a list of students, then create and save a PDF record sheet for the selection. </p>

    </AccordionItem>

    <AccordionItem header="Admin">
      <p>
        The admin interface is the part of the application dedicated to managing
        students, classes, staff, lessons and Kumon Center Details.
      </p>

      <hr />
      <h6>Manage Students</h6>
      <p>
        This page allows for student and contact information to be added, modified and removed.
      </p>

      <p>
        Contacts and students can also be linked using the interface, and GDPR
        data reports can be generated regarding students, including information
        regarding their attendance records.
      </p>

      <hr />
      <h6>Manage Classes</h6>

      <p>
        This page allows classes to be created, edited and deleted.
        This includes managing the students present within each class.
      </p>

      <p>
        Student details can be viewed within this page for students added to the class.
      </p>

      <p>
        Students can be added or removed from the class using the modal interface.
        Adding a student to a class will not automtically mark them present in any lessons.
      </p>

      <hr />
      <h6>Manage Staff</h6>

      <p>
        This page allows for staff to be added, modified and removed. This
        includes staff details and their KMS accounts. All staff have KMS
        accounts allowing them to login.
      </p>

      <p>
        Additional features of this page is creating and downloading data
        reports for a staff member.
      </p>

      <p>
        The administrator account can set the password for any staff account
        from here in the case where a staff member forgets their password.
      </p>

      <hr />
      <h6>Manage Lessons</h6>

      <p>
       Lessons are managed separately to classes, however they are linked.
       The interface allows classes to be created, edited and deleted from the database.
      </p>

      <p>
        Each lesson is a single instance, creating a new lesson will not introduce a recurring event.
      </p>

      <p>
        Lessons must be created with an associated class, subject and subject level.
      </p>


      <hr />
      <h6>Manage Center Details</h6>

      <p>
        The centre details manager can be used to change the address of the centre.
        These details are used when reports are generated, so should be kept up to
        date when necessary.
      </p>

      <p>
        The subjects taught by the centre can also be managed using this page.
        On the alternative tab, a list of subjects and their associated levels are listed.
        This can be added to with additional subjects/levels or trimmed by deleting them.
      </p>

      <hr />
      <h6>Maintenance</h6>

      <p>
        This page is split into two parts: Managing Importing and Exporting of
        data, and Managing Deleted Records.
      </p>

      <p>
        The Importing and Exporting page allows the user to import a K-SIS dump
        export or a KMS .kumon export file. In addition to this it allows them
        to export all data stored by the system to a KMS .kumon export file and
        view all previous imports.
      </p>

      <p>
        The deleted records page evolves around the data retention period for
        student and staff records. Whenever a student or staff record is
        deleted, the data will be kept for one year. This page will show all
        students and staff marked for deletion allowing them to be permanently
        deleted or restored.
      </p>
    </AccordionItem>

    <AccordionItem header="Other">
      <h6>Logging Out</h6>

      <p>
        In order to log out, you need to press "Account Details" in the top
        right hand corner of the screen. This will open a dropdown with a log
        out button.
      </p>

      <p>If this button is pressed, it will log you out.</p>

      <hr />
      <h6>Changing Password</h6>

      <p>
        In order to change your password you need to press "Account Details" in
        the top right hand corner of the screen. This will open a dropdown with
        a edit login details button.
      </p>

      <p>
        If this button is pressed, a pop-out will appear. This can be used to
        change the password.
      </p>

      <p>
        If you have forgotten your password, please see the "Forgot Password"
        section.
      </p>

      <hr />
      <h6>Forgot Password</h6>

      <p>
        If a user with a normal staff account has forgotten their password then
        the system administrator must log in. They can set the password for any
        staff account in the "Manage Staff" page of the "Admin" interface. Here
        you can find the staff member and press the yellow "Forgot Password"
        button in the information view.
      </p>

      <p>
        If the system administrator forgot their password, press the "here" link
        at the bottom of the login page. This will take you to a page where the
        recovery passcode can be used to reset the administrator's password.
      </p>
    </AccordionItem>
  </Accordion>
</Container>
