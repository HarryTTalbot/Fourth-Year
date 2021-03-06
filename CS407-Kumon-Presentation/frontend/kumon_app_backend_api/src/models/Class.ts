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
 * @interface Class
 */
export interface Class {
    /**
     * 
     * @type {number}
     * @memberof Class
     */
    readonly id: number;
    /**
     * 
     * @type {string}
     * @memberof Class
     */
    name: string;
    /**
     * 
     * @type {number}
     * @memberof Class
     */
    readonly size: number;
}

export function ClassFromJSON(json: any): Class {
    return ClassFromJSONTyped(json, false);
}

export function ClassFromJSONTyped(json: any, ignoreDiscriminator: boolean): Class {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'name': json['name'],
        'size': json['size'],
    };
}

export function ClassToJSON(value?: Class | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
    };
}

