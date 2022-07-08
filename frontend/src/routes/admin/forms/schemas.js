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
 * The maximum length used for phone number strings.
 * @type {number}
 * @constant
 */
const MAX_PHONE_LENGTH = 17;

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

/**
 * The schema used for validating class forms.
 * @type {yup.ObjectSchema}
 * @constant
 */
export const CLASS_SCHEMA = yup.object().shape({
  name: yup.string().required().max(MAX_LENGTH),
});

/**
 * The schema used for validating contact detail forms.
 * @type {yup.ObjectSchema}
 * @constant
 */
export const CONTACT_SCHEMA = yup.object().shape({
  firstName: yup.string().required().max(MAX_LENGTH),
  middleName: yup.string().optional().max(MAX_LENGTH),
  lastName: yup.string().required().max(MAX_LENGTH),
  phoneHome: yup.string().optional().max(20).min(7).test(
      'is-valid-characters',
      'Can only contain numbers and +, (, ) characters',
      function(value){
        return value.match(/^[0-9+() ]+$/);
      }),
  phoneBusiness: yup.string().optional().max(20).min(7).test(
      'is-valid-characters',
      'Can only contain numbers and +, (, ) characters',
      function(value){
        return value.match(/^[0-9+() ]+$/);
      }),
  phoneMobile: yup.string().required().max(20).min(7).test(
      'is-valid-characters',
      'Can only contain numbers and +, (, ) characters',
      function(value){
        return value.match(/^[0-9+() ]+$/);
      }),
  email: yup.string().required().email(),

  address: ADDRESS_SCHEMA,
});

/**
 * The schema used for validating student forms.
 * @type {yup.ObjectSchema}
 * @constant
 */
export const STUDENT_SCHEMA = yup.object().shape({
  kSisId: yup.number().nullable().integer().positive(),
  firstName: yup.string().required().max(MAX_LENGTH),
  middleName: yup.string().optional().max(MAX_LENGTH),
  lastName: yup.string().required().max(MAX_LENGTH),
  dateOfBirth: yup.date().required().test(
      'is-before-today',
      'Cannot be in the future',
      function(value){
        return new Date() > value;
      }),
  joinDate: yup.date().nullable().test(
      'is-after-birth',
      'Must be after date of birth',
      function(value){
        return value == null || this.parent.dateOfBirth < value;
      }),
  leaveDate: yup.date().nullable().test(
      'is-after-join',
      'Must be after join date',
      function(value){
        return value == null || this.parent.joinDate < value;
      }),
  phoneNumber: yup.string().required().max(20).min(7).test(
      'is-valid-characters',
      'Can only contain numbers and +, (, ) characters',
      function(value){
        return value.match(/^[0-9+() ]+$/);
      }),
  school: yup.string().required().max(MAX_LENGTH),
  grade: yup.string().required().oneOf(['K', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']),
  email: yup.string().required().email(),

  address: ADDRESS_SCHEMA,
});

/**
 * The schema used for validating staff forms.
 * @type {yup.ObjectSchema}
 * @constant
 */
 export const STAFF_SCHEMA = yup.object().shape({
  firstName : yup.string().required().max(MAX_LENGTH),
  middleName : yup.string().max(MAX_LENGTH),
  lastName : yup.string().required().max(MAX_LENGTH),
  jobTitle : yup.string().required().max(MAX_LENGTH),
  joinDate : yup.date().required(),
  leaveDate : yup.date().nullable().test(
      'is-after-join',
      'Must be after start of Employment',
      function(value){
        return value == null || this.parent.joinDate < value;
      }),
});

/**
 * The schema used for validating lesson forms.
 * @type {yup.ObjectSchema}
 * @constant
 */
 export const LESSON_SCHEMA = yup.object().shape({
  startDatetime : yup.date().required(),
  starttime : yup.string().required(),
  endtime : yup.string().required().test(
      'is-after-start',
      'Must be after start time',
      function(value){
        return this.parent.starttime < value;
      }),
  classFk : yup.string().required(),
  subject : yup.number().required(),
  subjectLevel : yup.number().required(),
});

/**
 * The schema used for validating subject forms.
 * @type {yup.ObjectSchema}
 * @constant
 */
 export const SUBJECT_SCHEMA = yup.object().shape({
  name : yup.string().required().max(MAX_LENGTH),
});

// ------------------------------
// Default Values
// ------------------------------

/**
 * Gets the default address values.
 */
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

/**
 * Gets the default class values.
 */
export function defaultClass() {
  return {
    name: "",
  };
}

/**
 * Gets the default contact values.
 */
export function defaultContact() {
  return {
    firstName: "",
    middleName: "",
    lastName: "",
    phoneHome: "",
    phoneBusiness: "",
    phoneMobile: "",
    email: "",

    address: defaultAddress(),
  };
}

/**
 * Gets the default student values.
 */
export function defaultStudent() {
  return {
    kSisId: null,
    firstName: "",
    middleName: "",
    lastName: "",
    dateOfBirth: null,
    joinDate: null,
    leaveDate: null,
    phoneNumber: "",
    school: "",
    grade: null,

    address: defaultAddress(),
  };
}

/**
 * Gets the default staff values.
 */
export function defaultStaff() {
  return {
    firstName: "",
    middleName: "",
    lastName: "",
    jobTitle: "",
    joinDate: null,
    leaveDate: null
  };
}

/**
 * Gets the default staff values.
 */
export function defaultLesson() {
  return {
    startDateTime: new Date(),
    startTime: "",
    endTime: "",
    classFk: "",
    subject: null,
    subjectLevel: null,
  };
}

/**
 * Gets the default subject values.
 */
export function defaultSubject() {
  return {
    name : ""
  };
}
