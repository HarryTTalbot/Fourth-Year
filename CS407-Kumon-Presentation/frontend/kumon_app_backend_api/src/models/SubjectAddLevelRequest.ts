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
 * @interface SubjectAddLevelRequest
 */
export interface SubjectAddLevelRequest {
    /**
     * 
     * @type {string}
     * @memberof SubjectAddLevelRequest
     */
    name: string;
}

export function SubjectAddLevelRequestFromJSON(json: any): SubjectAddLevelRequest {
    return SubjectAddLevelRequestFromJSONTyped(json, false);
}

export function SubjectAddLevelRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): SubjectAddLevelRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': json['name'],
    };
}

export function SubjectAddLevelRequestToJSON(value?: SubjectAddLevelRequest | null): any {
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
