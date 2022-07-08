import { writable } from "svelte/store";

// Get the value out of storage on load.
const stored = localStorage.authToken;

// Set the stored value or a sane default.
export const authToken = writable(stored || "");

// Anytime the store changes, update the local storage value.
authToken.subscribe((value) => (localStorage.authToken = value));
