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
    Student,
    StudentFromJSON,
    StudentFromJSONTyped,
    StudentToJSON,
} from './Student';

/**
 * 
 * @export
 * @interface LongTermAbsenceView
 */
export interface LongTermAbsenceView {
    /**
     * 
     * @type {number}
     * @memberof LongTermAbsenceView
     */
    readonly id: number;
    /**
     * 
     * @type {Student}
     * @memberof LongTermAbsenceView
     */
    student: Student;
    /**
     * 
     * @type {Date}
     * @memberof LongTermAbsenceView
     */
    startDate: Date;
    /**
     * 
     * @type {Date}
     * @memberof LongTermAbsenceView
     */
    endDate: Date;
    /**
     * 
     * @type {string}
     * @memberof LongTermAbsenceView
     */
    reason: string;
}

export function LongTermAbsenceViewFromJSON(json: any): LongTermAbsenceView {
    return LongTermAbsenceViewFromJSONTyped(json, false);
}

export function LongTermAbsenceViewFromJSONTyped(json: any, ignoreDiscriminator: boolean): LongTermAbsenceView {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'student': StudentFromJSON(json['student']),
        'startDate': (new Date(json['start_date'])),
        'endDate': (new Date(json['end_date'])),
        'reason': json['reason'],
    };
}

export function LongTermAbsenceViewToJSON(value?: LongTermAbsenceView | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'student': StudentToJSON(value.student),
        'start_date': (value.startDate.toISOString().substr(0,10)),
        'end_date': (value.endDate.toISOString().substr(0,10)),
        'reason': value.reason,
    };
}

