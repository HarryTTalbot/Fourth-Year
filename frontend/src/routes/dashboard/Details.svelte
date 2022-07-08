<script>
  import { Container } from "sveltestrap";

  import API_CONFIG from "../../api";
  import { StudentsApi, StaffApi, ClassesApi } from "kumon_app_backend_api";

  // Link to backend api
  let studentApi = new StudentsApi(API_CONFIG);
  let staffApi = new StaffApi(API_CONFIG);
  let classesApi = new ClassesApi(API_CONFIG);

  // Number of objects in the database
  let no_students = 0;
  let no_classes = 0;
  let no_staff = 0;

  async function getDetails() {
    // Query the backend api
    try {
      let response = await studentApi.studentsList({});
      no_students = response.count;

      response = await classesApi.classesList({});
      no_classes = response.count;

      response = await staffApi.staffList({});
      no_staff = response.count;
    } catch (e) {}
  }
</script>

<main>
  <Container class="p-3">
    {#await getDetails()}
      <p>Retrieving Information...</p>
    {:then}
      <h2>Students</h2>

      <p>{no_students} students records in database</p>

      <h2>Classes</h2>

      <p>{no_classes} classes records in database</p>

      <h2>Staff</h2>

      <p>{no_staff} staff records in database</p>
    {/await}
  </Container>
</main>

<style>
  main {
    border-style: solid;
    border-width: 2px;
    border-color: gray;
    border-radius: 5px;
    width: 100%;
  }
</style>
