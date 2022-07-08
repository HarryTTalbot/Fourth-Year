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
    WorksheetView,
    WorksheetViewFromJSON,
    WorksheetViewFromJSONTyped,
    WorksheetViewToJSON,
} from './WorksheetView';

/**
 * 
 * @export
 * @interface PaginatedWorksheetViewList
 */
export interface PaginatedWorksheetViewList {
    /**
     * 
     * @type {number}
     * @memberof PaginatedWorksheetViewList
     */
    count?: number;
    /**
     * 
     * @type {string}
     * @memberof PaginatedWorksheetViewList
     */
    next?: string | null;
    /**
     * 
     * @type {string}
     * @memberof PaginatedWorksheetViewList
     */
    previous?: string | null;
    /**
     * 
     * @type {Array<WorksheetView>}
     * @memberof PaginatedWorksheetViewList
     */
    results?: Array<WorksheetView>;
}

export function PaginatedWorksheetViewListFromJSON(json: any): PaginatedWorksheetViewList {
    return PaginatedWorksheetViewListFromJSONTyped(json, false);
}

export function PaginatedWorksheetViewListFromJSONTyped(json: any, ignoreDiscriminator: boolean): PaginatedWorksheetViewList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'count': !exists(json, 'count') ? undefined : json['count'],
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': !exists(json, 'results') ? undefined : ((json['results'] as Array<any>).map(WorksheetViewFromJSON)),
    };
}

export function PaginatedWorksheetViewListToJSON(value?: PaginatedWorksheetViewList | null): any {
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
        'results': value.results === undefined ? undefined : ((value.results as Array<any>).map(WorksheetViewToJSON)),
    };
}
