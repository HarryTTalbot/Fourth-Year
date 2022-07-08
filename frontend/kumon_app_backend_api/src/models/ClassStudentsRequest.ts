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
 * Serializer for managing class students.
 * @export
 * @interface ClassStudentsRequest
 */
export interface ClassStudentsRequest {
    /**
     * 
     * @type {number}
     * @memberof ClassStudentsRequest
     */
    studentId: number;
}

export function ClassStudentsRequestFromJSON(json: any): ClassStudentsRequest {
    return ClassStudentsRequestFromJSONTyped(json, false);
}

export function ClassStudentsRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): ClassStudentsRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'studentId': json['student_id'],
    };
}

export function ClassStudentsRequestToJSON(value?: ClassStudentsRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'student_id': value.studentId,
    };
}
