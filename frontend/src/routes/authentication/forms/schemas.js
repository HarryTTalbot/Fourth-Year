/**
 * @module schemas
 * Contains validation schemas for various forms used in the application.
 * These are created using [Yup](https://github.com/jquense/yup).
 */

import * as yup from "yup";

// ------------------------------
// Yup Configuration
// ------------------------------

// Different default messages
yup.setLocale({
  mixed: {
    required: "Required field",
    notType: "Value is not a valid ${type}",
  },
  number: {
    integer: "Value should be an integer",
    min: "Value should be at least ${min}",
    max: "Value should be at most ${max}",
    positive: "Value should be positive",
  },
  string: {
    email: "Invalid email provided",
    max: "Input is too long (max ${max} characters)",
  },
});

// ------------------------------
// Schemas
// ------------------------------

/**
 * The default max length used by the database models.
 * @type {number}
 * @constant
 */
const MAX_LENGTH = 50;

export const LOGIN_SCHEMA = yup.object().shape({
  username: yup.string().required().max(MAX_LENGTH),
  password: yup.string().required().max(MAX_LENGTH),
});

export const EDIT_PASSWORD_SCHEMA = yup.object().shape({
  oldPassword: yup.string().required().max(MAX_LENGTH),
  newPassword: yup
    .string()
    .required()
    .min(8)
    .max(MAX_LENGTH)
    .test(
      "password-strength",
      "Password must contain upper and lower case letters and at least one special character",
      function (value) {
        let regEx = new RegExp("(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])");
        return regEx.test(value);
      }
    ),
  confirmNewPassword: yup
    .string()
    .required()
    .min(8)
    .max(MAX_LENGTH)
    .test("same-as-password", "Must be the same as new password", function (
      value
    ) {
      return this.parent.newPassword == value;
    }),
});

export const FORGET_PASSWORD_SCHEMA = yup.object().shape({
  newPassword: yup
    .string()
    .required()
    .min(8)
    .max(MAX_LENGTH)
    .test(
      "password-strength",
      "Password must contain upper and lower case letters and at least one special character",
      function (value) {
        let regEx = new RegExp("(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])");
        return regEx.test(value);
      }
    ),
  confirmNewPassword: yup
    .string()
    .required()
    .max(MAX_LENGTH)
    .test("same-as-password", "Must be the same as new password", function (
      value
    ) {
      return this.parent.newPassword == value;
    }),
});

export const ADMIN_FORGET_PASSWORD_SCHEMA = yup.object().shape({
  passcode: yup.string().required().max(MAX_LENGTH),
  newPassword: yup
    .string()
    .required()
    .min(8)
    .max(MAX_LENGTH)
    .test(
      "password-strength",
      "Password must contain upper and lower case letters and at least one special character",
      function (value) {
        let regEx = new RegExp("(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])");
        return regEx.test(value);
      }
    ),
  confirmNewPassword: yup
    .string()
    .required()
    .max(MAX_LENGTH)
    .test("same-as-password", "Must be the same as new password", function (
      value
    ) {
      return this.parent.newPassword == value;
    }),
});

export const NEW_ACCOUNT_SCHEMA = yup.object().shape({
  username: yup
    .string()
    .required()
    .min(5)
    .max(MAX_LENGTH)
    .test(
      "username-characters",
      "Username must only contain letters and numbers",
      function (value) {
        return value.match(/^[a-zA-Z0-9]+$/);
      }
    ),
  password: yup
    .string()
    .required()
    .min(8)
    .max(MAX_LENGTH)
    .test(
      "password-strength",
      "Password must contain upper and lower case letters and at least one special character",
      function (value) {
        let regEx = new RegExp("(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])");
        return regEx.test(value);
      }
    ),
  confirmPassword: yup
    .string()
    .required()
    .max(MAX_LENGTH)
    .test("same-as-password", "Must be the same as new password", function (
      value
    ) {
      return this.parent.newPassword == value;
    }),
});

// ------------------------------
// Default Values
// ------------------------------

export function defaultLogin() {
  return {
    username: "",
    password: "",
  };
}

export function defaultEditPassword() {
  return {
    oldPassword: "",
    newPassword: "",
    confirmNewPassword: "",
  };
}

export function defaultForgetPassword() {
  return {
    newPassword: "",
    confirmNewPassword: "",
  };
}

export function defaultAdminForgetPassword() {
  return {
    passcode: "",
    newPassword: "",
    confirmNewPassword: "",
  };
}

export function defaultNewAccount() {
  return {
    username: "",
    password: "",
    confirmPassword: "",
  };
}
