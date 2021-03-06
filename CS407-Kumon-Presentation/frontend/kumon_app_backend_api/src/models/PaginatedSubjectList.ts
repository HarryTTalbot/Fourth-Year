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
    Subject,
    SubjectFromJSON,
    SubjectFromJSONTyped,
    SubjectToJSON,
} from './Subject';

/**
 * 
 * @export
 * @interface PaginatedSubjectList
 */
export interface PaginatedSubjectList {
    /**
     * 
     * @type {number}
     * @memberof PaginatedSubjectList
     */
    count?: number;
    /**
     * 
     * @type {string}
     * @memberof PaginatedSubjectList
     */
    next?: string | null;
    /**
     * 
     * @type {string}
     * @memberof PaginatedSubjectList
     */
    previous?: string | null;
    /**
     * 
     * @type {Array<Subject>}
     * @memberof PaginatedSubjectList
     */
    results?: Array<Subject>;
}

export function PaginatedSubjectListFromJSON(json: any): PaginatedSubjectList {
    return PaginatedSubjectListFromJSONTyped(json, false);
}

export function PaginatedSubjectListFromJSONTyped(json: any, ignoreDiscriminator: boolean): PaginatedSubjectList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'count': !exists(json, 'count') ? undefined : json['count'],
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': !exists(json, 'results') ? undefined : ((json['results'] as Array<any>).map(SubjectFromJSON)),
    };
}

export function PaginatedSubjectListToJSON(value?: PaginatedSubjectList | null): any {
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
        'results': value.results === undefined ? undefined : ((value.results as Array<any>).map(SubjectToJSON)),
    };
}

