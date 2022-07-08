<script>
  import { onMount } from "svelte";
  import { openModal, closeModal } from "svelte-modals";
  import {
    Button,
    Container,
    Table,
    Collapse,
    FormGroup,
    Label,
    Input,
    Row,
    Col,
    Tooltip,
    Icon,
    Modal,
    ModalBody,
    ModalFooter,
  } from "sveltestrap";

  import API_CONFIG from "../../../../api";
  import { ClassesApi } from "kumon_app_backend_api";
  import InfoModal from "../../../../modals/InfoModal.svelte";
  import {
    PageFilter,
    default as PaginationFilteringBar,
  } from "../../../../components/PaginationFilteringBar.svelte";

  let classApi = new ClassesApi(API_CONFIG);
  let classes = [];

  let studentsInClass = [];
  let studentsNotInClass = [];

  let chosenClass = null; // Stores the value selected in the dropdown
  let focused = false;

  let idsToAdd = []; // List of ids of Students to add to a class
  let idsToRemove = [];

  export let onEdit = async () => {};

  /**
   * Whether we are refreshing the list of imports.
   * @type {boolean}
   */
  let isRefreshing = false;

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let isOpen;

  /**
   * Whether the modal is open or not.
   * @type {boolean}
   */
  export let classID;

  let pageFilterNotInClass = new PageFilter();

  /**
   * Refreshes the list of students.
   * @param {number} cid The ID of the class we're refreshing the lists for.
   */
  export async function refreshStudents() {
    isRefreshing = true;

    try {
      // Query the backend for a list of students in the selected class, and a list of students not in that class. Store the two lists as variables.
      let inClass = await classApi.classesGetStudentsList({ id: classID });
      let notInClass = await classApi.classesGetStudentsNotInClassList({
        id: classID,
        page: pageFilterNotInClass.page,
        search: pageFilterNotInClass.filter,
      });

      studentsInClass = inClass;

      studentsNotInClass = notInClass.results;

      // Update list with pagination and filtering
      pageFilterNotInClass.pageUpdate(notInClass);
      pageFilterNotInClass.filter += " ";
      pageFilterNotInClass.filter = pageFilterNotInClass.filter.substring(
        0,
        pageFilterNotInClass.filter.length - 1
      );
    } catch (e) {}

    isRefreshing = false;
  }

  /**
   * Handler for editing a class.
   * @param {number} cid The ID of the class we've selected in the dropdown
   */
  async function handleClassSelect() {
    if (classID === null) return;
    try {
      let response = await classApi.classesRetrieve({ id: classID });
      chosenClass = response.name;
    } catch (e) {}
    isOpen = true; // Open <Collapse> tag (Containing the two tables and buttons)
    refreshStudents(classID);
  }

  /**
   * Handler for adding a student to a class.
   * @param {number} cid The ID of the class we're adding the student to.
   */
  async function handleAddToClass() {
    try {
      let idsToBeUsed = [];

      for (let i = 0; i < idsToAdd.length; i++) {
        idsToBeUsed.push({ studentId: idsToAdd[i] });
      }

      await classApi.classesAddStudents({
        id: classID,
        classStudentsRequest: idsToBeUsed,
      });

      let addSuccessMsg =
        idsToAdd.length > 1
          ? "Successfully added " +
            idsToAdd.length +
            " students to class " +
            classID +
            "!"
          : "Successfully added a student to Class " + classID + "!";

      idsToAdd = [];

      refreshStudents();
    } catch (e) {
      // TODO: More descriptive error? Some of this could be handled in client-side validation
      await handleClose();
      openModal(InfoModal, {
        title: "Add Student to Class",
        message: "Unable to add student(s) to class!",
      });
    }
  }

  /**
   * Handler for removing a student from a class.
   * @param {number} cid The ID of the class we're removing the student from.
   */
  async function handleRemoveFromClass() {
    try {
      let idsToBeUsed = [];

      for (let i = 0; i < idsToRemove.length; i++) {
        idsToBeUsed.push({ studentId: idsToRemove[i] });
      }

      await classApi.classesRemoveStudents({
        id: classID,
        classStudentsRequest: idsToBeUsed,
      });

      let rmvSuccessMsg =
        idsToRemove.length > 1
          ? "Successfully removed " +
            idsToRemove.length +
            " students from class " +
            classID +
            "!"
          : "Successfully removed a student from Class " + classID + "!";

      idsToRemove = [];

      refreshStudents();
    } catch (e) {
      await handleClose();
      openModal(InfoModal, {
        title: "Remove Student(s) from Class",
        message: "Unable to remove student(s) from class!",
      });
    }
  }

  async function handleClose() {
    await onEdit();
    closeModal();
  }

  $: handleClassSelect(classID);
</script>

{#if isOpen}
  <Modal centered {isOpen} header={`Manage Students in Class`} fullscreen>
    <ModalBody>
      <div style="padding-left:2%; padding-right:2%;">
        <Row>
          <Col>
            <!--
          This first table contains members of the class that was selected in the dropdown.
          It is displayed on the left of the page.
          -->
            <h3>Students in {chosenClass}</h3>
            <Table>
              <thead>
                <tr>
                  <th />
                  <th>K-SIS ID</th>
                  <th>First Name</th>
                  <th>Last Name</th>
                </tr>
              </thead>

              {#if isRefreshing}
                <tfoot class="info">
                  <tr>
                    <td colspan="4">Retrieving list of students...</td>
                  </tr>
                </tfoot>
              {:else if studentsInClass.length === 0}
                <tfoot class="info">
                  <tr>
                    <td colspan="4">No student data found</td>
                  </tr>
                </tfoot>
              {:else}
                <tbody>
                  <!-- Load students into the table -->
                  {#each studentsInClass as student}
                    <tr>
                      <td>
                        <!-- When a checkbox is checked, its value — the student id — is added to the bound list "idsToRemove" -->
                        <input
                          type="checkbox"
                          bind:group={idsToRemove}
                          value={student.id}
                        />
                      </td>
                      {#if student.kSisId}
                        <td>{student.kSisId}</td>
                      {:else}
                        <td>N/A</td>
                      {/if}
                      <td>{student.firstName}</td>
                      <td>{student.lastName}</td>
                    </tr>
                  {/each}
                </tbody>
              {/if}
            </Table>
          </Col>

          <!--
        This column sits between the two tables and holds the two buttons used to move students between classes
        -->
          <Col xs="auto">
            <Row>
              <!-- Each button is disabled until the list it passes to its on:click function has at least one element -->
              <Button
                id="Add_To_Class"
                size="lg"
                color="success"
                disabled={!idsToAdd.length}
                on:click={() => handleAddToClass(chosenClass, idsToAdd)}
                ><Icon name="arrow-bar-left" /></Button
              >
            </Row>
            <Tooltip target="Add_To_Class" placement="top">
              Add To Class {chosenClass}
            </Tooltip>
            <Row>
              <Button
                id="Remove_From_Class"
                size="lg"
                color="danger"
                disabled={!idsToRemove.length}
                on:click={() => handleRemoveFromClass(chosenClass, idsToRemove)}
                ><Icon name="arrow-bar-right" /></Button
              >
            </Row>
            <Tooltip target="Remove_From_Class" placement="bottom">
              Remove From Class {chosenClass}
            </Tooltip>
          </Col>

          <!--
        This second table contains all other students who are not members of the selected class.
        It is displayed on the right of the page.
        -->
          <Col>
            <h3>Other students</h3>
            <PaginationFilteringBar
              refresh={() => refreshStudents(classID)}
              pageFilter={pageFilterNotInClass}
            />
            <Table>
              <thead>
                <tr>
                  <th />
                  <th>K-SIS ID</th>
                  <th>First Name</th>
                  <th>Last Name</th>
                </tr>
              </thead>

              {#if isRefreshing}
                <tfoot class="info">
                  <tr>
                    <td colspan="4">Retrieving list of students...</td>
                  </tr>
                </tfoot>
              {:else if studentsNotInClass.length === 0}
                <tfoot class="info">
                  <tr>
                    <td colspan="4">No student data found</td>
                  </tr>
                </tfoot>
              {:else}
                <tbody>
                  {#each studentsNotInClass as student}
                    <tr>
                      <td>
                        <input
                          type="checkbox"
                          bind:group={idsToAdd}
                          value={student.id}
                        />
                      </td>
                      {#if student.kSisId}
                        <td>{student.kSisId}</td>
                      {:else}
                        <td>N/A</td>
                      {/if}
                      <td>{student.firstName}</td>
                      <td>{student.lastName}</td>
                    </tr>
                  {/each}
                </tbody>
              {/if}
            </Table>
          </Col>
        </Row>
      </div>
    </ModalBody>
    <ModalFooter>
      <Button color="secondary" size="lg" outline on:click={handleClose}
        >Close</Button
      >
    </ModalFooter>
  </Modal>
{/if}
