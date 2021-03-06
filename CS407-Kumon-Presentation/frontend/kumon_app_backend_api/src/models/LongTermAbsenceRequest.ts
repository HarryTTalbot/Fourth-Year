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
 * @interface LongTermAbsenceRequest
 */
export interface LongTermAbsenceRequest {
    /**
     * 
     * @type {StudentListRequest}
     * @memberof LongTermAbsenceRequest
     */
    student: StudentListRequest;
    /**
     * 
     * @type {Date}
     * @memberof LongTermAbsenceRequest
     */
    startDate: Date;
    /**
     * 
     * @type {Date}
     * @memberof LongTermAbsenceRequest
     */
    endDate: Date;
    /**
     * 
     * @type {string}
     * @memberof LongTermAbsenceRequest
     */
    reason: string;
}

export function LongTermAbsenceRequestFromJSON(json: any): LongTermAbsenceRequest {
    return LongTermAbsenceRequestFromJSONTyped(json, false);
}

export function LongTermAbsenceRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): LongTermAbsenceRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'student': StudentListRequestFromJSON(json['student']),
        'startDate': (new Date(json['startDate'])),
        'endDate': (new Date(json['endDate'])),
        'reason': json['reason'],
    };
}

export function LongTermAbsenceRequestToJSON(value?: LongTermAbsenceRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'student': StudentListRequestToJSON(value.student),
        'startDate': (value.startDate.toISOString().substr(0,10)),
        'endDate': (value.endDate.toISOString().substr(0,10)),
        'reason': value.reason,
    };
}

