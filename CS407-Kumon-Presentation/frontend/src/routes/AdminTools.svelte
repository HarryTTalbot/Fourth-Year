<script>
  import Router from "svelte-spa-router";

  import ClassManager from "./admin/classes/ClassManager.svelte";
  import MainNavbar from "../components/MainNavbar.svelte";
  import Maintenance from "./admin/Maintenance.svelte";
  import NotFound from "./NotFound.svelte";
  import StaffManager from "./admin/staff/StaffManager.svelte";
  import Students from "./admin/Students.svelte";
  import LessonManager from "./admin/lessons/LessonManager.svelte";
  import CenterSubjectManager from "./admin/CenterSubjectManager.svelte";

  const prefix = "/admin";
  const routes = {
    "/classes": ClassManager,
    "/students": Students,
    "/maintenance": Maintenance,
    "/staff": StaffManager,
    "/lessons": LessonManager,
    "/center": CenterSubjectManager,
    "*": NotFound,
  };
</script>

<main>
  <MainNavbar active="/admin" />
  <Router {routes} {prefix} />
</main>

<style>
  main {
    height: 100vh;
  }
</style>
