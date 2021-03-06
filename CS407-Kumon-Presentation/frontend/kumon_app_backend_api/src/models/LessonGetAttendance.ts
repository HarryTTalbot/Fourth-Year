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
    StatusEnum,
    StatusEnumFromJSON,
    StatusEnumFromJSONTyped,
    StatusEnumToJSON,
} from './StatusEnum';
import {
    StudentList,
    StudentListFromJSON,
    StudentListFromJSONTyped,
    StudentListToJSON,
} from './StudentList';

/**
 * 
 * @export
 * @interface LessonGetAttendance
 */
export interface LessonGetAttendance {
    /**
     * 
     * @type {StudentList}
     * @memberof LessonGetAttendance
     */
    student: StudentList;
    /**
     * 
     * @type {StatusEnum}
     * @memberof LessonGetAttendance
     */
    status: StatusEnum;
    /**
     * 
     * @type {Date}
     * @memberof LessonGetAttendance
     */
    readonly lastModifiedAt: Date;
}

export function LessonGetAttendanceFromJSON(json: any): LessonGetAttendance {
    return LessonGetAttendanceFromJSONTyped(json, false);
}

export function LessonGetAttendanceFromJSONTyped(json: any, ignoreDiscriminator: boolean): LessonGetAttendance {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'student': StudentListFromJSON(json['student']),
        'status': StatusEnumFromJSON(json['status']),
        'lastModifiedAt': (new Date(json['last_modified_at'])),
    };
}

export function LessonGetAttendanceToJSON(value?: LessonGetAttendance | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'student': StudentListToJSON(value.student),
        'status': StatusEnumToJSON(value.status),
    };
}

