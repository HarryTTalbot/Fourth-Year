<script>
  import { Container, Row, Col } from "sveltestrap";

  import MainNavbar from "../components/MainNavbar.svelte";

  import AttendanceComponent from "./dashboard/Attendance.svelte";
  import InventoryComponent from "./dashboard/Inventory.svelte";
  import HelpComponent from "./dashboard/Help.svelte";
  import CalendarComponent from "./dashboard/Calendar.svelte";

  import API_CONFIG from "../api";
  import { AuthenticationApi } from "kumon_app_backend_api";

  // Link to backend API
  let authApi = new AuthenticationApi(API_CONFIG);

  // Logged in user
  let staff = null;

  // Function to get the current logged in user
  async function get_user() {
    staff = await authApi.authenticationGetLoggedInStaffRetrieve({});
  }
</script>

<main>
  <!-- Navigation Bar -->
  <MainNavbar active="/dashboard" />

  <!-- Welcome Message -->
  <Container class="p-3">
    {#await get_user()}
      <p>Loading data...</p>
    {:then}
      <h1>Welcome {staff.firstName} {staff.lastName}!</h1>
    {:catch}
      <h1>Welcome!</h1>
    {/await}
  </Container>

  <!-- Modules in 2x2 configuration -->
  <div class="outer" style="height:80%">
    <Row class="h-50">
      <Col>
        <AttendanceComponent />
      </Col>

      <Col>
        <CalendarComponent />
      </Col>
    </Row>
    <br />
    <Row>
      <Col>
        <InventoryComponent />
      </Col>

      <Col>
        <HelpComponent />
      </Col>
    </Row>
  </div>
</main>

<style>
  main {
    height: 100vh;
  }

  div.outer {
    margin-left: 5%;
    margin-right: 5%;
  }
</style>
