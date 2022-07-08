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
export const LONG_TERM_SCHEMA = yup.object().shape({
  student: yup.number().typeError("Student is required").integer().required("Student is required"),
  startDate: yup.date(),
  endDate: yup.date().test(
      'is-after-start',
      'Must be after start date',
      function(value){
        return this.parent.startDate < value;
      }),
  reason: yup.string().required(),
  otherDetail: yup.string().test(
      'is-not-empty-when-other',
      'You must specify a reason',
      function(value){
        if ( this.parent.reason == "Other" && (value == "" || value == null || value == undefined) ) {
          return false
        }
        return true;
      }),
});

/**
 * Gets the default long term absence values.
 */
export function defaultLongTerm() {
  return {
    student: null,
    startDate: null,
    endDate: null,
    reason: "Holiday",
    otherDetail: ""
  };
}
