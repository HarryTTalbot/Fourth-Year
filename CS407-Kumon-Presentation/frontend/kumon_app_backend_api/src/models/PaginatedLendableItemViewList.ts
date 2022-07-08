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
    LendableItemView,
    LendableItemViewFromJSON,
    LendableItemViewFromJSONTyped,
    LendableItemViewToJSON,
} from './LendableItemView';

/**
 * 
 * @export
 * @interface PaginatedLendableItemViewList
 */
export interface PaginatedLendableItemViewList {
    /**
     * 
     * @type {number}
     * @memberof PaginatedLendableItemViewList
     */
    count?: number;
    /**
     * 
     * @type {string}
     * @memberof PaginatedLendableItemViewList
     */
    next?: string | null;
    /**
     * 
     * @type {string}
     * @memberof PaginatedLendableItemViewList
     */
    previous?: string | null;
    /**
     * 
     * @type {Array<LendableItemView>}
     * @memberof PaginatedLendableItemViewList
     */
    results?: Array<LendableItemView>;
}

export function PaginatedLendableItemViewListFromJSON(json: any): PaginatedLendableItemViewList {
    return PaginatedLendableItemViewListFromJSONTyped(json, false);
}

export function PaginatedLendableItemViewListFromJSONTyped(json: any, ignoreDiscriminator: boolean): PaginatedLendableItemViewList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'count': !exists(json, 'count') ? undefined : json['count'],
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': !exists(json, 'results') ? undefined : ((json['results'] as Array<any>).map(LendableItemViewFromJSON)),
    };
}

export function PaginatedLendableItemViewListToJSON(value?: PaginatedLendableItemViewList | null): any {
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
        'results': value.results === undefined ? undefined : ((value.results as Array<any>).map(LendableItemViewToJSON)),
    };
}
