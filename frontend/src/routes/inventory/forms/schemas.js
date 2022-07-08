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
    max: "Field is too long (max ${max} characters)",
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
export const WORKSHEET_SCHEMA = yup.object().shape({
  subject: yup.number().required(),
  subjectLevel: yup.string().required(),
  set: yup.string(),
  quantity: yup.number(),
});

export const WORKSHEETLOG_SCHEMA = yup.object().shape({
  staffId: yup.number().required(),
  type: yup.string().required(), //Dropdown, both options are strings
  quantity: yup.number(),
});

/**
 * The schema used for validating address forms.
 * @type {yup.ObjectSchema}
 * @constant
 */
export const BULKITEM_SCHEMA = yup.object().shape({
  name: yup.string(),
  quantity: yup.number(),
});

export const LENDABLEITEM_SCHEMA = yup.object().shape({
  name: yup.string(),
  quantityAvailable: yup.number(),
});

export const ITEMLOANLOG_SCHEMA = yup.object().shape({
  studentId: yup.number().required(),
  quantity: yup.number(),
});

/**
 * Gets the default long term absence values.
 */
export function defaultWorksheet() {
  return {
    subject: null,
    subject_level: null,
    set: "",
    quantity: null,
  };
}

export function defaultWorksheetLog() {
  return {
    id: null,
    staffId: null,
    type: "Withdrawal",
    quantity: 0,
  };
}

export function defaultItemLoanLog() {
  return {
    studentId: null,
    quantity: 0,
  };
}

export function defaultBulkItem() {
  return {
    name: "",
    quantity: null,
  };
}

export function defaultLendableItem() {
  return {
    name: "",
    quantityAvailable: 0,
  };
}
