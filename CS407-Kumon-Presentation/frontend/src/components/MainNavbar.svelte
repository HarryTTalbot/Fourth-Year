<script>
  import { link, push } from "svelte-spa-router";
  import { authToken } from "../sessionStorage";
  import {
    Image,
    Button,
    ButtonDropdown,
    DropdownItem,
    DropdownMenu,
    DropdownToggle,
  } from "sveltestrap";
  import { fade } from "svelte/transition";
  import { tick } from "svelte";
  import EditPassword from "../routes/authentication/EditPassword.svelte";
  import { Modals, closeModal, openModal } from "svelte-modals";

  export let active = "/dashboard";

  // Links in the website
  const links = [
    {
      href: "/dashboard",
      name: "Home",
    },
    {
      href: "/attendance",
      name: "Attendance",
      sublinks: [
        { href: "/attendance/home", name: "Today's Lessons" },
        { href: "/attendance/historical", name: "Past Lessons" },
        { href: "/attendance/longTerm", name: "Long Term Absences" },
      ],
    },
    {
      href: "/inventory",
      // href: "/inventory/",
      name: "Inventory",
      sublinks: [
        { href: "/inventory/worksheets", name: "Worksheets" },
        { href: "/inventory/bulkitems", name: "Bulk Items" },
        { href: "/inventory/lendableitems", name: "Lendable Items" },
      ]
    },
    {
      href: "/recordsheet",
      name: "Record Sheet Generator",
    },
    {
      href: "/admin",
      name: "Admin",
      sublinks: [
        { href: "/admin/students", name: "Manage Students" },
        { href: "/admin/classes", name: "Manage Classes" },
        { href: "/admin/staff", name: "Manage Staff" },
        { href: "/admin/lessons", name: "Manage Lessons" },
        { href: "/admin/center", name: "Manage Center Details" },
        { href: "/admin/maintenance", name: "Maintenance" },
      ],
    },
  ];

  // Function to log the user out
  function logout() {
    $authToken = "";
    location.reload();
  }

  // Function to open the form to edit the password
  function openEditPassword() {
    openModal(EditPassword);
  }
</script>

<!-- Navigation bar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <!-- Logo and Application Name -->

    <a class="navbar-brand" href="/dashboard" use:link>
    <Image src="static/KMS_K.png" style="width:35px;height:35px;" />
      Kumon Management System
    </a>

    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarSupportedContent"
    >
      <span class="navbar-toggler-icon" />
    </button>

    <!-- Navigation bar -->
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        {#each links as lnk}
          {#if lnk.sublinks}
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                class:active={lnk.href === active}
                role="button"
                data-bs-toggle="dropdown"
                href={"#"}
              >
                {lnk.name}
              </a>

              <ul class="dropdown-menu">
                {#each lnk.sublinks as sublnk}
                  <li>
                    <a class="dropdown-item" href={sublnk.href} use:link>
                      {sublnk.name}
                    </a>
                  </li>
                {/each}
              </ul>
            </li>
          {:else}
            <li class="nav-item">
              <a
                class="nav-link"
                class:active={lnk.href === active}
                href={lnk.href}
                use:link
              >
                {lnk.name}
              </a>
            </li>
          {/if}
        {/each}
      </ul>

      <!-- Account details corner of navigation bar -->
      <div class="d-flex" style="padding-right:20px">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              role="button"
              data-bs-toggle="dropdown"
              style="color:#f0ad4e"
              href={"#"}
            >
              Account Details
            </a>

            <ul class="dropdown-menu">
              <li>
                <DropdownItem on:click={() => openEditPassword()}
                  >Edit Login Details</DropdownItem
                >
              </li>
              <li>
                <DropdownItem on:click={() => logout()}>Logout</DropdownItem>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </div>
</nav>
