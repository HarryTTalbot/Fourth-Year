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
 * @interface Subject
 */
export interface Subject {
    /**
     * 
     * @type {number}
     * @memberof Subject
     */
    readonly id: number;
    /**
     * 
     * @type {string}
     * @memberof Subject
     */
    name: string;
}

export function SubjectFromJSON(json: any): Subject {
    return SubjectFromJSONTyped(json, false);
}

export function SubjectFromJSONTyped(json: any, ignoreDiscriminator: boolean): Subject {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'name': json['name'],
    };
}

export function SubjectToJSON(value?: Subject | null): any {
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

