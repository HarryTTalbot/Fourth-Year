<script>
  import { closeModal, openModal } from "svelte-modals";
  import {
    Button,
    Table,
    Input,
    Modal,
    ModalBody,
    ModalFooter,
    Icon,
    Tooltip,
  } from "sveltestrap";

  import StudentField from "../../../../formFields/StudentField.svelte";

  import InfoModal from "../../../../modals/InfoModal.svelte";

  import API_CONFIG from "../../../../api";
  import { ContactsApi, StudentsApi } from "kumon_app_backend_api";

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * The ID of the student currently being edited.
   * @type {number}
   */
  export let id;

  /**
   * The details of the contact currently being edited.
   * @type {details} matches the student API endpoint
   */
  let contactDetails;

  /**
   * List of students associated with the chosen contact
   */
  let students = [];

  /**
   * The ID of the contact being selected.
   * @type {number}
   */
  let newStudent;

  let studentError;
  let studentComp;

  /**
   * The type of relationship being created.
   * @type {string} defaults to "Mother" to allow immediate submission
   */
  let newRelationship = "Mother";

  /**
   * The contacts API instance in use.
   * @type {ContactsApi}
   */
  let contactsApi = new ContactsApi(API_CONFIG);

  /**
   * The students API instance in use.
   * @type {StudentsApi}
   */
  let studentsApi = new StudentsApi(API_CONFIG);

  /**
   * Loads the student's current details into this form.
   * @param {number} id The ID of the student.
   */
  async function loadContactDetails(id) {
    try {
      contactDetails = await contactsApi.contactsRetrieve({ id: id });
      // Get the list of contacts associated with the chosen student
      students = await contactsApi.contactsGetStudentsList({ id: id });
    } catch (e) {
      openModal(InfoModal, {
        title: "Manage Student Contacts",
        message: `Could not load details for student ${id}!`,
      });
    }
  }

  async function deleteStudent(student_id) {
    try {
      await studentsApi.studentsRemoveContactsCreate({
        id: student_id,
        studentRemoveContactsRequest: [{ contactId: id }],
      });
      await loadContactDetails(id);
    } catch (e) {
      openModal(InfoModal, {
        title: "Manage Student Contacts",
        message: `Could not remove the contact!`,
      });
    }
  }

  async function addStudent() {
    try {
      // verifies if the contact has already been linked to the student
      for (let i = 0; i < students.length; i++) {
        if (students[i].studentId.id == newStudent) {
          openModal(InfoModal, {
            title: "Manage Contact Students",
            message: `Cannot add a duplicate student`,
          });
          return;
        }
      }

      await studentsApi.studentsAddContactsCreate({
        id: newStudent,
        studentAddContactsRequest: [
          { contactId: id, relationship: newRelationship },
        ],
      });

      await loadContactDetails(id);

      newStudent = null;
      studentComp.handleClear();
    } catch (e) {
      openModal(InfoModal, {
        title: "Manage Contact Students",
        message: `Could not add the student!`,
      });
    }
  }

  // Subscription which automatically re-fills the form when the ID is changed
  // Needed since svelte-modals re-uses the component instances
  $: loadContactDetails(id);
</script>

{#if isOpen && contactDetails != undefined}
  <Modal
    centered
    size="lg"
    {isOpen}
    header={`Manage Students for ${contactDetails.lastName}, ${contactDetails.firstName}`}
  >
    <ModalBody>
      <Table>
        <thead>
          <tr>
            <th style="width: 60%">Student Name</th>
            <th style="width: 30%">Relationship</th>
            <th style="width: 10%" />
          </tr>
        </thead>
        <tbody>
          {#each students as student}
            <tr>
              <td>
                {student.studentId.lastName}, {student.studentId.firstName}
              </td>
              <td>
                {student.relationship}
              </td>
              <td>
                <Button
                  id={"deleteStudentLink" + student.studentId.id}
                  color="danger"
                  on:click={() => deleteStudent(student.studentId.id)}
                >
                  <Icon name="trash" />
                </Button>
                <Tooltip
                  target={"deleteStudentLink" + student.studentId.id}
                  placement="top"
                >
                  Remove {student.studentId.lastName}, {student.studentId
                    .firstName} as a Student
                </Tooltip>
              </td>
            </tr>
          {/each}
          <tr>
            <td>
              <StudentField
                id="student"
                invalid={studentError}
                feedback={studentError}
                bind:student={newStudent}
                bind:this={studentComp}
              />
            </td>
            <td>
              <Input
                id="relationship"
                type="select"
                bind:value={newRelationship}
              >
                <option selected="selected">Mother</option>
                <option>Father</option>
                <option>Uncle</option>
                <option>Aunt</option>
                <option>Guardian</option>
                <option>Other</option>
              </Input>
            </td>
            <td>
              <Button
                id="addStudentLink"
                color="success"
                on:click={() => addStudent()}
              >
                <Icon name="plus-square" />
              </Button>
              <Tooltip target="addStudentLink" placement="top">
                Add Student
              </Tooltip>
            </td>
          </tr>
        </tbody>
      </Table>
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" outline on:click={closeModal}>Back</Button>
    </ModalFooter>
  </Modal>
{/if}
