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
    StudentGetContacts,
    StudentGetContactsFromJSON,
    StudentGetContactsFromJSONTyped,
    StudentGetContactsToJSON,
} from './StudentGetContacts';

/**
 * 
 * @export
 * @interface PaginatedStudentGetContactsList
 */
export interface PaginatedStudentGetContactsList {
    /**
     * 
     * @type {number}
     * @memberof PaginatedStudentGetContactsList
     */
    count?: number;
    /**
     * 
     * @type {string}
     * @memberof PaginatedStudentGetContactsList
     */
    next?: string | null;
    /**
     * 
     * @type {string}
     * @memberof PaginatedStudentGetContactsList
     */
    previous?: string | null;
    /**
     * 
     * @type {Array<StudentGetContacts>}
     * @memberof PaginatedStudentGetContactsList
     */
    results?: Array<StudentGetContacts>;
}

export function PaginatedStudentGetContactsListFromJSON(json: any): PaginatedStudentGetContactsList {
    return PaginatedStudentGetContactsListFromJSONTyped(json, false);
}

export function PaginatedStudentGetContactsListFromJSONTyped(json: any, ignoreDiscriminator: boolean): PaginatedStudentGetContactsList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'count': !exists(json, 'count') ? undefined : json['count'],
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': !exists(json, 'results') ? undefined : ((json['results'] as Array<any>).map(StudentGetContactsFromJSON)),
    };
}

export function PaginatedStudentGetContactsListToJSON(value?: PaginatedStudentGetContactsList | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'count': value.count,
        'next': value.next,
        'previous': value.previous,
        'results': value.results === undefined ? undefined : ((value.results as Array<any>).map(StudentGetContactsToJSON)),
    };
}

