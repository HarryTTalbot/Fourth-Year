import AdminTools from "./routes/AdminTools.svelte";
import Attendance from "./routes/Attendance.svelte";
import Dashboard from "./routes/Dashboard.svelte";
import RecordSheetGenerator from "./routes/RecordSheetGenerator.svelte";
import Login from "./routes/authentication/Login.svelte";
import ResetAdminPassword from "./routes/authentication/ResetAdminPassword.svelte";
import Setup from "./routes/Setup.svelte";
import Inventory from "./routes/Inventory.svelte";

import NotFound from "./routes/NotFound.svelte";

// Routes of the interface
export default {
  "/": Login,
  "/welcome/*": Setup,
  "/admin/*": AdminTools,
  "/attendance/*": Attendance,
  "/dashboard": Dashboard,
  "/recordsheet": RecordSheetGenerator,
  "/forgotAdminPassword": ResetAdminPassword,
  "/inventory/*": Inventory,
  "*": NotFound, // NOTE: Catch-all route must be last
};
