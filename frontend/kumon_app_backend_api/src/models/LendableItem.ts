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
 * @interface LendableItem
 */
export interface LendableItem {
    /**
     * 
     * @type {number}
     * @memberof LendableItem
     */
    readonly id: number;
    /**
     * 
     * @type {string}
     * @memberof LendableItem
     */
    name: string;
    /**
     * 
     * @type {number}
     * @memberof LendableItem
     */
    quantityAvailable?: number;
    /**
     * 
     * @type {number}
     * @memberof LendableItem
     */
    readonly quantityLent: number;
}

export function LendableItemFromJSON(json: any): LendableItem {
    return LendableItemFromJSONTyped(json, false);
}

export function LendableItemFromJSONTyped(json: any, ignoreDiscriminator: boolean): LendableItem {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'name': json['name'],
        'quantityAvailable': !exists(json, 'quantity_available') ? undefined : json['quantity_available'],
        'quantityLent': json['quantity_lent'],
    };
}

export function LendableItemToJSON(value?: LendableItem | null): any {
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
