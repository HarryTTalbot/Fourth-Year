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

/**
 * The schema used for validating address forms.
 * @type {yup.ObjectSchema}
 * @constant
 */
export const ADDRESS_SCHEMA = yup.object().shape({
  lineOne: yup.string().required().max(MAX_LENGTH),
  lineTwo: yup.string().max(MAX_LENGTH),
  lineThree: yup.string().max(MAX_LENGTH),
  cityTown: yup.string().required().max(MAX_LENGTH),
  provinceDistrict: yup.string().max(MAX_LENGTH),
  postCode: yup.string().required().max(MAX_LENGTH),
  country: yup.string().required().max(MAX_LENGTH),
});

export const ADMIN_ACCOUNT_SCHEMA = yup.object().shape({
  firstName: yup.string().required().max(MAX_LENGTH),
  middleName: yup.string().max(MAX_LENGTH),
  lastName: yup.string().required().max(MAX_LENGTH),
  jobTitle: yup.string().required().max(MAX_LENGTH),
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
    .min(8)
    .max(MAX_LENGTH)
    .test("same-as-password", "Must be the same as new password", function (
      value
    ) {
      return this.parent.password == value;
    }),
  passcode: yup
    .string()
    .required()
    .min(12)
    .max(MAX_LENGTH)
    .test(
      "passcode-strength",
      "Passcode must contain upper and lower case letters and at least one special character",
      function (value) {
        let regEx = new RegExp("(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])");
        return regEx.test(value);
      }
    )
    .test(
      "different-to-password",
      "Passcode must be different to password",
      function (value) {
        return this.parent.password != value;
      }
    ),
  confirmPasscode: yup
    .string()
    .required()
    .min(8)
    .max(MAX_LENGTH)
    .test("same-as-password", "Must be the same as new password", function (
      value
    ) {
      return this.parent.passcode == value;
    }),
});

export const CENTER_DETAILS_SCHEMA = yup.object().shape({
  name: yup.string().required().max(MAX_LENGTH),
  phoneNumber: yup
    .string()
    .required()
    .max(20)
    .min(7)
    .test(
      "is-valid-characters",
      "Can only contain numbers and +, (, ) characters",
      function (value) {
        return value.match(/^[0-9+() ]+$/);
      }
    ),
  address: ADDRESS_SCHEMA,
});

// ------------------------------
// Default Values
// ------------------------------

export function defaultAdminAccount() {
  return {
    firstName: "",
    middleName: "",
    lastName: "",
    jobTitle: "",
    username: "",
    password: "",
    confirmPassword: "",
    passcode: "",
    confirmPasscode: "",
  };
}

export function defaultCenterDetails() {
  return {
    name: "",
    phoneNumber: "",
    address: defaultAddress(),
  };
}

export function defaultAddress() {
  return {
    lineOne: "",
    lineTwo: "",
    lineThree: "",
    cityTown: "",
    provinceDistrict: "",
    postCode: "",
    country: "",
  };
}
