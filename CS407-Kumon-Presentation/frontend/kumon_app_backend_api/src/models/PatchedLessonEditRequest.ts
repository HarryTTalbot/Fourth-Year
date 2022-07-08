/* tslint:disable */
/* eslint-disable */
/**
 * Kumon App - Backend API
 * Backend API for the Kumon Centre Management app.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface PatchedLessonEditRequest
 */
export interface PatchedLessonEditRequest {
    /**
     * 
     * @type {Date}
     * @memberof PatchedLessonEditRequest
     */
    startDatetime?: Date;
    /**
     * 
     * @type {Date}
     * @memberof PatchedLessonEditRequest
     */
    endDatetime?: Date;
    /**
     * 
     * @type {number}
     * @memberof PatchedLessonEditRequest
     */
    classFk?: number;
    /**
     * 
     * @type {number}
     * @memberof PatchedLessonEditRequest
     */
    subjectLevel?: number;
}

export function PatchedLessonEditRequestFromJSON(json: any): PatchedLessonEditRequest {
    return PatchedLessonEditRequestFromJSONTyped(json, false);
}

export function PatchedLessonEditRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): PatchedLessonEditRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'startDatetime': !exists(json, 'start_datetime') ? undefined : (new Date(json['start_datetime'])),
        'endDatetime': !exists(json, 'end_datetime') ? undefined : (new Date(json['end_datetime'])),
        'classFk': !exists(json, 'class_fk') ? undefined : json['class_fk'],
        'subjectLevel': !exists(json, 'subject_level') ? undefined : json['subject_level'],
    };
}

export function PatchedLessonEditRequestToJSON(value?: PatchedLessonEditRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'start_datetime': value.startDatetime === undefined ? undefined : (value.startDatetime.toISOString()),
        'end_datetime': value.endDatetime === undefined ? undefined : (value.endDatetime.toISOString()),
        'class_fk': value.classFk,
        'subject_level': value.subjectLevel,
    };
}
