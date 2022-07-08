<script>
  import Router from "svelte-spa-router";

  import Historical from "./attendance/historical/Historical.svelte";
  import Home from "./attendance/home/Home.svelte";
  import LessonAttendance from "./attendance/lessonAttendance/LessonAttendance.svelte";
  import LongTerm from "./attendance/longTerm/LongTerm.svelte";
  import MainNavbar from "../components/MainNavbar.svelte";
  import NotFound from "./NotFound.svelte";

  const prefix = "/attendance";
  const routes = {
    "/home": Home,
    "/historical": Historical,
    "/longTerm": LongTerm,
    "/lesson/:id" : LessonAttendance,
    "*": NotFound
  };
</script>

<main>
  <MainNavbar active="/attendance" />
  <Router {routes} {prefix} />
</main>

<style>
  main {
    height: 100vh;
  }
</style>
