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
 * @interface SubjectRequest
 */
export interface SubjectRequest {
    /**
     * 
     * @type {string}
     * @memberof SubjectRequest
     */
    name: string;
}

export function SubjectRequestFromJSON(json: any): SubjectRequest {
    return SubjectRequestFromJSONTyped(json, false);
}

export function SubjectRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): SubjectRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': json['name'],
    };
}

export function SubjectRequestToJSON(value?: SubjectRequest | null): any {
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
