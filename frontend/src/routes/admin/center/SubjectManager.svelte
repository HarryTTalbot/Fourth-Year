<script>
  import { onMount } from "svelte";
  import { fade } from "svelte/transition";
  import { Modals, closeModal, openModal } from "svelte-modals";
  import {
    Button,
    Container,
    Table,
    Input,
    Label,
    Row,
    Col,
    Icon,
    Tooltip,
  } from "sveltestrap";
  import { tick } from "svelte";

  import API_CONFIG, { getConfig } from "../../../api";
  import { SubjectApi } from "kumon_app_backend_api";

  import SubjectForm from "../forms/SubjectForm.svelte";

  import InfoModal from "../../../modals/InfoModal.svelte";
  import {
    default as ConfirmationModal,
    BUTTONS,
  } from "../../../modals/ConfirmationModal.svelte";
  import AddSubjectModal from "./modals/AddSubjectModal.svelte";
  import SubjectHelp from "./SubjectHelp.svelte";

  // Link to backend api
  let subjectApi = new SubjectApi(API_CONFIG);

  // Variables needed in the page
  let subjectList = []; // List of subject currently on display
  let levelList = []; // List of levels for the current subject
  let subjectForm; // Backing element for the subject form
  let currentID; // The current subject member being viewed
  let view = false; // Whether the view subject form is open
  let newLevel = ""; // Name of a new level being added
  let openHelp = false; // Whether the useguide is open

  /**
   * Whether we are refreshing the list of imports.
   * @type {boolean}
   */
  let isRefreshing = false;

  // Function to refresh the list of subject
  async function refreshSubjects() {
    try {
      // Get the most up to date authentication
      subjectApi = new SubjectApi(getConfig());
      isRefreshing = true;

      // Query the Backend with the page and search filter
      let response = await subjectApi.subjectList({});

      // Fill the subjects list
      subjectList = [];
      for (let i = 0; i < response.length; i++) {
        let subject = response[i];

        // Get the subject levels of the current subject
        let response2 = await subjectApi.subjectGetLevelsList({
          id: subject.id,
        });

        // Add those to the subject
        subject.levels = response2;
        subject.levelsDisplay = "";

        // Define how the levels are to be shown
        for (let j = 0; j < response2.length; j++) {
          subject.levelsDisplay += response2[j].name;
          if (j + 1 != response2.length) {
            subject.levelsDisplay += ", ";
          }
        }

        // Add the subject to the list
        subjectList.push(subject);
      }
      isRefreshing = false;
    } catch (e) {}
  }

  // Function to close all views (create new subject and view subject)
  async function closeView() {
    // Set whether create subject and view subject are open
    view = false;
    newLevel = "";

    // Refresh the list of subject
    await refreshSubjects();

    // Reset the selected subject
    currentID = null;
  }

  // Function to open the details of a subject member
  async function handleViewSubject(id) {
    // If the subject is currently being viewed, the view gets closed
    if (currentID === id) {
      currentID = null;
      await closeView();
      return;
    }

    // Set the create subject to be hidden and view subject to be open
    view = true;
    currentID = id;

    // Wait for the form component to be loaded in
    await tick();

    // Find the subject member and set them as the subject object to be shown
    subjectList.forEach(function (item, index) {
      if (item.id == currentID) {
        subjectForm.setDefaultValues(item);

        levelList = item.levels;
      }
    });
  }

  // Function to open the create new subject form
  async function openCreateForm() {
    openModal(AddSubjectModal, {
      onSubjectAdd: async () => {
        // Refresh the staff list
        await refreshSubjects();
      },
    });
  }

  // Function to update a subject member's details
  async function handleUpdateSubject(evt) {
    try {
      // Query the backend to update the details
      await subjectApi.subjectUpdate({
        id: evt.detail.id,
        subjectRequest: evt.detail,
      });

      // Open a modal to say the operation was successfull
      openModal(InfoModal, {
        title: "Update Subject",
        message: "Successfully updated the subject!",
      });

      // Hide the subject details view
      await closeView();

      // Refresh the subject list
      await refreshSubjects();
    } catch (e) {
      // Open a modal to tell them the update was unsuccessful
      openModal(InfoModal, {
        title: "Update Subject",
        message: "Unable to update subject!",
      });
    }
  }

  // Function to remove a subject member
  async function handleDeleteSubject() {
    // Query the backend to get the subject details (as they are in the database)
    let subject = await subjectApi.subjectRetrieve({ id: currentID });

    // Formulate a confirmation message to the user
    let subjectMessage = subject.name;

    let confirmationMessage =
      "Are you sure you want to delete this subject?\n\n" + subjectMessage;

    // Open a confirmation modal to ask the user to confirm the deletion
    openModal(ConfirmationModal, {
      title: "Delete Subject",
      message: confirmationMessage,
      buttons: BUTTONS.yesNo,
      onConfirm: () => {
        // If the user confirms the deletion
        try {
          // Query the backend to remove the subject member (uses Promise API)
          subjectApi.subjectDestroy({ id: subject.id }).then((_) => {
            // Update the subject list to remove the subject member
            subjectList = subjectList.filter(
              (subject2) => subject2.id !== currentID
            );

            // Set whether create subject and view subject are open
            view = false;

            // Reset the selected subject
            currentID = null;

            // Open a modal to inform the user that the subject member has been removed
            openModal(
              InfoModal,
              {
                title: "Delete Subject",
                message: `Deleted subject ${subjectMessage}.`,
              },
              { replace: true }
            );
          });
        } catch (e) {
          // Open a modal to inform the user that the deletion has been unsuccessful
          openModal(
            InfoModal,
            {
              title: "Delete Subject",
              message: `Could not mark ${subjectMessage}  for deletion!`,
            },
            { replace: true }
          );
        }
      },
    });
  }

  // Fuction to remove a subject level
  async function deleteLevel(level) {
    try {
      isRefreshing = true;

      // Query the backend to remove the level
      await subjectApi.subjectRemoveLevelCreate({
        id: currentID,
        subjectRemoveLevelRequest: { id: level.id },
      });

      // Remove the level from the list on the frontend
      levelList = levelList.filter((level2) => level2.id !== level.id);

      // Refetch the subject levels from the backend to display
      for (let i = 0; i < subjectList.length; i++) {
        if (subjectList[i].id == currentID) {
          levelList = await subjectApi.subjectGetLevelsList({ id: currentID });

          subjectList[i].levelsDisplay = "";

          for (let j = 0; j < levelList.length; j++) {
            subjectList[i].levelsDisplay += levelList[j].name;
            if (j + 1 != levelList.length) {
              subjectList[i].levelsDisplay += ", ";
            }
          }

          // Reset the values of the subject form
          subjectForm.setDefaultValues(subjectList[i]);
        }
      }
      isRefreshing = false;
    } catch (e) {
      // On an error, open an info modal to inform the user of the issue
      openModal(
        InfoModal,
        {
          title: "Delete Subject Level",
          message: `Could not delete the level ${level.name}!`,
        },
        { replace: true }
      );
    }
  }

  // Function to add a new subject level
  async function addLevel() {
    try {
      isRefreshing = true;

      // Send a request to the backend
      await subjectApi.subjectAddLevelCreate({
        id: currentID,
        subjectAddLevelRequest: { name: newLevel },
      });

      // Update the levels in the frontend and how they are displayed
      for (let i = 0; i < subjectList.length; i++) {
        if (subjectList[i].id == currentID) {
          levelList = await subjectApi.subjectGetLevelsList({ id: currentID });

          subjectList[i].levelsDisplay = "";

          for (let j = 0; j < levelList.length; j++) {
            subjectList[i].levelsDisplay += levelList[j].name;
            if (j + 1 != levelList.length) {
              subjectList[i].levelsDisplay += ", ";
            }
          }

          // Update the default values of the subject form
          subjectForm.setDefaultValues(subjectList[i]);
        }
      }

      // Set the new level form to blank
      newLevel = "";

      isRefreshing = false;
    } catch (e) {
      // On an error, open up a modal informing the user
      openModal(
        InfoModal,
        {
          title: "Create Subject Level",
          message: `Could not add ${newLevel}!`,
        },
        { replace: true }
      );
    }
  }

  /**
   * Refreshes classes when the page is loaded.
   */
  onMount(async () => {
    await refreshSubjects();
  });
</script>

<!-- Content of the page -->
<Container class="p-3">
  <Row>
    <Col>
      <h1>Subject Manager</h1>
    </Col>

    <Col>
      <Button
        id="helpSubject"
        color="dark"
        style="float: right;"
        on:click={() => (openHelp = !openHelp)}
      >
        <Icon name="question-square" />
      </Button>
      <Tooltip target="helpSubject" placement="top">
        User Guide for Subject Manager
      </Tooltip>
    </Col>
  </Row>
  <Row>
    <Col>
      <h2>Subject List</h2>
    </Col>

    <Col>
      <Button
        id="addSubject"
        color="success"
        style="float: right;"
        on:click={() => openCreateForm()}
      >
        <Icon name="plus-square" />
      </Button>
      <Tooltip target="addSubject" placement="top">Add a New Subject</Tooltip>
    </Col>
  </Row>

  <Table class="mainTable">
    <!-- Subject Table Headings -->
    <thead>
      <tr>
        <th>Subject</th>
        <th>Levels</th>
      </tr>
    </thead>

    {#if isRefreshing}
      <!-- Whilst waiting for backend response -->
      <tfoot class="info">
        <tr>
          <td colspan="6">Retrieving list of subjects...</td>
        </tr>
      </tfoot>
    {:else if subjectList.length === 0}
      <!-- If no subject are returned -->
      <tfoot class="info">
        <tr>
          <td colspan="6">No subject data found</td>
        </tr>
      </tfoot>
    {:else}
      <!-- If subjects are returned -->
      <tbody>
        {#each subjectList as subject}
          <tr
            class:selected={currentID === subject.id}
            on:click={() => handleViewSubject(subject.id)}
          >
            <td>{subject.name}</td>
            <td>{subject.levelsDisplay}</td>
          </tr>
        {/each}
      </tbody>
    {/if}
  </Table>

  <!-- View subject Details -->
  {#if view == true}
    <Row>
      <Col xs="auto">
        <h2>Subject Details</h2>
      </Col>

      <Col>
        <Button
          id="removeSubject"
          color="danger"
          on:click={() => handleDeleteSubject()}
        >
          <Icon name="trash" />
        </Button>
        <Tooltip target="removeSubject" placement="top">
          Remove the Subject
        </Tooltip>
      </Col>
    </Row>

    <SubjectForm
      id="edit-subject-form"
      class="w-50"
      bind:this={subjectForm}
      on:submit={handleUpdateSubject}
      visible={false}
    />
    <Button
      id="editSubject"
      form="edit-subject-form"
      color="primary"
      type="submit"
    >
      <Icon name="pen" />
    </Button>
    <Tooltip target="editSubject" placement="top">Update Subject Name</Tooltip>
    <Button
      id="cancelSubject"
      form="edit-subject-form"
      color="secondary"
      outline
      on:click={closeView}
    >
      <Icon name="x-square" />
    </Button>
    <Tooltip target="cancelSubject" placement="top">
      Close Subject Details
    </Tooltip>
    <Table>
      <!-- Subject Table Headings -->
      <thead>
        <tr>
          <th>Level Name</th>
        </tr>
      </thead>
      <tbody>
        {#each levelList as level}
          <tr>
            <td>
              {level.name}
            </td>
            <td>
              <Button
                id="removeSubjectLevel{level.id}"
                color="danger"
                on:click={() => deleteLevel(level)}
              >
                <Icon name="trash" />
              </Button>
              <Tooltip target="removeSubjectLevel{level.id}" placement="top">
                Remove the Subject Level - {level.name}
              </Tooltip>
            </td>
          </tr>
        {/each}
        <tr>
          <td>
            <Input id="newLevelName" type="text" bind:value={newLevel} />
          </td>
          <td>
            <Button
              id="addSubjectLevel"
              color="success"
              on:click={() => addLevel()}
            >
              <Icon name="plus-square" />
            </Button>
            <Tooltip target="addSubjectLevel" placement="top">
              Add a New Subject Level
            </Tooltip>
          </td>
        </tr>
      </tbody>
    </Table>
  {/if}

  <SubjectHelp bind:open={openHelp} />
</Container>

<style>
  /* Centre any footers displaying information */
  tfoot.info > tr > td {
    text-align: center;
  }
  .selected {
    background-color: #6c757d;
    color: white;
  }
  Table.mainTable tbody tr:hover {
    background-color: #6c757d;
    color: white;
  }
</style>
