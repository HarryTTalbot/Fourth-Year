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
    Staff,
    StaffFromJSON,
    StaffFromJSONTyped,
    StaffToJSON,
} from './Staff';

/**
 * 
 * @export
 * @interface PaginatedStaffList
 */
export interface PaginatedStaffList {
    /**
     * 
     * @type {number}
     * @memberof PaginatedStaffList
     */
    count?: number;
    /**
     * 
     * @type {string}
     * @memberof PaginatedStaffList
     */
    next?: string | null;
    /**
     * 
     * @type {string}
     * @memberof PaginatedStaffList
     */
    previous?: string | null;
    /**
     * 
     * @type {Array<Staff>}
     * @memberof PaginatedStaffList
     */
    results?: Array<Staff>;
}

export function PaginatedStaffListFromJSON(json: any): PaginatedStaffList {
    return PaginatedStaffListFromJSONTyped(json, false);
}

export function PaginatedStaffListFromJSONTyped(json: any, ignoreDiscriminator: boolean): PaginatedStaffList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'count': !exists(json, 'count') ? undefined : json['count'],
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': !exists(json, 'results') ? undefined : ((json['results'] as Array<any>).map(StaffFromJSON)),
    };
}

export function PaginatedStaffListToJSON(value?: PaginatedStaffList | null): any {
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
        'results': value.results === undefined ? undefined : ((value.results as Array<any>).map(StaffToJSON)),
    };
}

