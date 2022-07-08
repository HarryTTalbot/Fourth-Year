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
    required: "Required",
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
    min: "Input is too short (min ${min} characters)",
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
 * The schema used for validating record sheet forms.
 * @type {yup.ObjectSchema}
 * @constant
 */
export const RECORD_SHEET_SCHEMA = yup.object().shape({
 startDate : yup.date().required(),
 days : yup.number().required().integer().min(1).max(7),
 subject : yup.number().required(),
 subjectLevel : yup.number().required(),
 numSheets: yup.number().required(),
 completionTime: yup.number().optional().min(1)
});

// ------------------------------
// Default Values
// ------------------------------

/**
 * Gets the default record sheet values.
 */
export function defaultRecordSheet() {
  return {
    startDate : new Date(),
    subject: null,
    subjectLevel: null,
    days: null,
    numSheets: null,
    completionTime: null,
  };
}
