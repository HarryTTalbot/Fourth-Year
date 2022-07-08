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
    WorksheetLog,
    WorksheetLogFromJSON,
    WorksheetLogFromJSONTyped,
    WorksheetLogToJSON,
} from './WorksheetLog';

/**
 * 
 * @export
 * @interface PaginatedWorksheetLogList
 */
export interface PaginatedWorksheetLogList {
    /**
     * 
     * @type {number}
     * @memberof PaginatedWorksheetLogList
     */
    count?: number;
    /**
     * 
     * @type {string}
     * @memberof PaginatedWorksheetLogList
     */
    next?: string | null;
    /**
     * 
     * @type {string}
     * @memberof PaginatedWorksheetLogList
     */
    previous?: string | null;
    /**
     * 
     * @type {Array<WorksheetLog>}
     * @memberof PaginatedWorksheetLogList
     */
    results?: Array<WorksheetLog>;
}

export function PaginatedWorksheetLogListFromJSON(json: any): PaginatedWorksheetLogList {
    return PaginatedWorksheetLogListFromJSONTyped(json, false);
}

export function PaginatedWorksheetLogListFromJSONTyped(json: any, ignoreDiscriminator: boolean): PaginatedWorksheetLogList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'count': !exists(json, 'count') ? undefined : json['count'],
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': !exists(json, 'results') ? undefined : ((json['results'] as Array<any>).map(WorksheetLogFromJSON)),
    };
}

export function PaginatedWorksheetLogListToJSON(value?: PaginatedWorksheetLogList | null): any {
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
        'results': value.results === undefined ? undefined : ((value.results as Array<any>).map(WorksheetLogToJSON)),
    };
}
