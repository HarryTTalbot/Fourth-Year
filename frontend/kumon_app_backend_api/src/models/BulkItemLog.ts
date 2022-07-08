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
    Type3beEnum,
    Type3beEnumFromJSON,
    Type3beEnumFromJSONTyped,
    Type3beEnumToJSON,
} from './Type3beEnum';

/**
 * 
 * @export
 * @interface BulkItemLog
 */
export interface BulkItemLog {
    /**
     * 
     * @type {number}
     * @memberof BulkItemLog
     */
    staffId?: number | null;
    /**
     * 
     * @type {Type3beEnum}
     * @memberof BulkItemLog
     */
    type: Type3beEnum;
    /**
     * 
     * @type {number}
     * @memberof BulkItemLog
     */
    quantity: number;
    /**
     * 
     * @type {Date}
     * @memberof BulkItemLog
     */
    readonly createdAt: Date;
}

export function BulkItemLogFromJSON(json: any): BulkItemLog {
    return BulkItemLogFromJSONTyped(json, false);
}

export function BulkItemLogFromJSONTyped(json: any, ignoreDiscriminator: boolean): BulkItemLog {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'staffId': !exists(json, 'staff_id') ? undefined : json['staff_id'],
        'type': Type3beEnumFromJSON(json['type']),
        'quantity': json['quantity'],
        'createdAt': (new Date(json['created_at'])),
    };
}

export function BulkItemLogToJSON(value?: BulkItemLog | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'staff_id': value.staffId,
        'type': Type3beEnumToJSON(value.type),
        'quantity': value.quantity,
    };
}
