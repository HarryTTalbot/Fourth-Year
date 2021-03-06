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
    ContactGetStudents,
    ContactGetStudentsFromJSON,
    ContactGetStudentsFromJSONTyped,
    ContactGetStudentsToJSON,
} from './ContactGetStudents';

/**
 * 
 * @export
 * @interface PaginatedContactGetStudentsList
 */
export interface PaginatedContactGetStudentsList {
    /**
     * 
     * @type {number}
     * @memberof PaginatedContactGetStudentsList
     */
    count?: number;
    /**
     * 
     * @type {string}
     * @memberof PaginatedContactGetStudentsList
     */
    next?: string | null;
    /**
     * 
     * @type {string}
     * @memberof PaginatedContactGetStudentsList
     */
    previous?: string | null;
    /**
     * 
     * @type {Array<ContactGetStudents>}
     * @memberof PaginatedContactGetStudentsList
     */
    results?: Array<ContactGetStudents>;
}

export function PaginatedContactGetStudentsListFromJSON(json: any): PaginatedContactGetStudentsList {
    return PaginatedContactGetStudentsListFromJSONTyped(json, false);
}

export function PaginatedContactGetStudentsListFromJSONTyped(json: any, ignoreDiscriminator: boolean): PaginatedContactGetStudentsList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'count': !exists(json, 'count') ? undefined : json['count'],
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': !exists(json, 'results') ? undefined : ((json['results'] as Array<any>).map(ContactGetStudentsFromJSON)),
    };
}

export function PaginatedContactGetStudentsListToJSON(value?: PaginatedContactGetStudentsList | null): any {
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
        'results': value.results === undefined ? undefined : ((value.results as Array<any>).map(ContactGetStudentsToJSON)),
    };
}

