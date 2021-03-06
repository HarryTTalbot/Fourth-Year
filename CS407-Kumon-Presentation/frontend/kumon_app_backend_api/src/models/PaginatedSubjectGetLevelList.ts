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
    SubjectGetLevel,
    SubjectGetLevelFromJSON,
    SubjectGetLevelFromJSONTyped,
    SubjectGetLevelToJSON,
} from './SubjectGetLevel';

/**
 * 
 * @export
 * @interface PaginatedSubjectGetLevelList
 */
export interface PaginatedSubjectGetLevelList {
    /**
     * 
     * @type {number}
     * @memberof PaginatedSubjectGetLevelList
     */
    count?: number;
    /**
     * 
     * @type {string}
     * @memberof PaginatedSubjectGetLevelList
     */
    next?: string | null;
    /**
     * 
     * @type {string}
     * @memberof PaginatedSubjectGetLevelList
     */
    previous?: string | null;
    /**
     * 
     * @type {Array<SubjectGetLevel>}
     * @memberof PaginatedSubjectGetLevelList
     */
    results?: Array<SubjectGetLevel>;
}

export function PaginatedSubjectGetLevelListFromJSON(json: any): PaginatedSubjectGetLevelList {
    return PaginatedSubjectGetLevelListFromJSONTyped(json, false);
}

export function PaginatedSubjectGetLevelListFromJSONTyped(json: any, ignoreDiscriminator: boolean): PaginatedSubjectGetLevelList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'count': !exists(json, 'count') ? undefined : json['count'],
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': !exists(json, 'results') ? undefined : ((json['results'] as Array<any>).map(SubjectGetLevelFromJSON)),
    };
}

export function PaginatedSubjectGetLevelListToJSON(value?: PaginatedSubjectGetLevelList | null): any {
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
        'results': value.results === undefined ? undefined : ((value.results as Array<any>).map(SubjectGetLevelToJSON)),
    };
}

