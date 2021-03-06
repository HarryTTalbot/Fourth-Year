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
 * Serializer for adding or removing contacts from a student.
 * @export
 * @interface PatchedStudentAddRemoveContactsRequest
 */
export interface PatchedStudentAddRemoveContactsRequest {
    /**
     * 
     * @type {Array<number>}
     * @memberof PatchedStudentAddRemoveContactsRequest
     */
    ids?: Array<number>;
}

export function PatchedStudentAddRemoveContactsRequestFromJSON(json: any): PatchedStudentAddRemoveContactsRequest {
    return PatchedStudentAddRemoveContactsRequestFromJSONTyped(json, false);
}

export function PatchedStudentAddRemoveContactsRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): PatchedStudentAddRemoveContactsRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'ids': !exists(json, 'ids') ? undefined : json['ids'],
    };
}

export function PatchedStudentAddRemoveContactsRequestToJSON(value?: PatchedStudentAddRemoveContactsRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'ids': value.ids,
    };
}

