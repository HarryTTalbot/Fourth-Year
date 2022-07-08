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
 * 
 * @export
 * @interface PatchedLendableItemRequest
 */
export interface PatchedLendableItemRequest {
    /**
     * 
     * @type {string}
     * @memberof PatchedLendableItemRequest
     */
    name?: string;
    /**
     * 
     * @type {number}
     * @memberof PatchedLendableItemRequest
     */
    quantityAvailable?: number;
}

export function PatchedLendableItemRequestFromJSON(json: any): PatchedLendableItemRequest {
    return PatchedLendableItemRequestFromJSONTyped(json, false);
}

export function PatchedLendableItemRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): PatchedLendableItemRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': !exists(json, 'name') ? undefined : json['name'],
        'quantityAvailable': !exists(json, 'quantity_available') ? undefined : json['quantity_available'],
    };
}

export function PatchedLendableItemRequestToJSON(value?: PatchedLendableItemRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
        'quantity_available': value.quantityAvailable,
    };
}
