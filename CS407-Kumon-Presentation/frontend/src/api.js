import { Configuration } from "kumon_app_backend_api";
import { get } from "svelte/store";
import { authToken } from "./sessionStorage";

// Token for authentication
let token;

// Create a link to the session storage
authToken.subscribe((value) => {
  token = value;
});

/**
 * API configuration that needs to be used whenever we create a new API class instance.
 * This sets the base path to the origin server used by the browser.
 */
let API_CONFIG = new Configuration({
  basePath: window.location.origin,
  apiKey: token,
});

export default API_CONFIG;

// Function to get an up to date API configuration
export function getConfig() {
  return new Configuration({
    basePath: window.location.origin,
    apiKey: get(authToken),
  });
}
