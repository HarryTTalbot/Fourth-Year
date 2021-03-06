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
import {
    StudentListRequest,
    StudentListRequestFromJSON,
    StudentListRequestFromJSONTyped,
    StudentListRequestToJSON,
} from './StudentListRequest';

/**
 * 
 * @export
 * @interface PatchedLongTermAbsenceRequest
 */
export interface PatchedLongTermAbsenceRequest {
    /**
     * 
     * @type {StudentListRequest}
     * @memberof PatchedLongTermAbsenceRequest
     */
    student?: StudentListRequest;
    /**
     * 
     * @type {Date}
     * @memberof PatchedLongTermAbsenceRequest
     */
    startDate?: Date;
    /**
     * 
     * @type {Date}
     * @memberof PatchedLongTermAbsenceRequest
     */
    endDate?: Date;
    /**
     * 
     * @type {string}
     * @memberof PatchedLongTermAbsenceRequest
     */
    reason?: string;
}

export function PatchedLongTermAbsenceRequestFromJSON(json: any): PatchedLongTermAbsenceRequest {
    return PatchedLongTermAbsenceRequestFromJSONTyped(json, false);
}

export function PatchedLongTermAbsenceRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): PatchedLongTermAbsenceRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'student': !exists(json, 'student') ? undefined : StudentListRequestFromJSON(json['student']),
        'startDate': !exists(json, 'startDate') ? undefined : (new Date(json['startDate'])),
        'endDate': !exists(json, 'endDate') ? undefined : (new Date(json['endDate'])),
        'reason': !exists(json, 'reason') ? undefined : json['reason'],
    };
}

export function PatchedLongTermAbsenceRequestToJSON(value?: PatchedLongTermAbsenceRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'student': StudentListRequestToJSON(value.student),
        'startDate': value.startDate === undefined ? undefined : (value.startDate.toISOString().substr(0,10)),
        'endDate': value.endDate === undefined ? undefined : (value.endDate.toISOString().substr(0,10)),
        'reason': value.reason,
    };
}

