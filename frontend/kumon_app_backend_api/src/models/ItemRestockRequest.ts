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
 * @interface ItemRestockRequest
 */
export interface ItemRestockRequest {
    /**
     * 
     * @type {number}
     * @memberof ItemRestockRequest
     */
    staffId: number;
    /**
     * 
     * @type {number}
     * @memberof ItemRestockRequest
     */
    quantity: number;
}

export function ItemRestockRequestFromJSON(json: any): ItemRestockRequest {
    return ItemRestockRequestFromJSONTyped(json, false);
}

export function ItemRestockRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): ItemRestockRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'staffId': json['staff_id'],
        'quantity': json['quantity'],
    };
}

export function ItemRestockRequestToJSON(value?: ItemRestockRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'staff_id': value.staffId,
        'quantity': value.quantity,
    };
}
