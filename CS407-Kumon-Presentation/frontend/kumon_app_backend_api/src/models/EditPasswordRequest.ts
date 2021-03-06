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
 * Serializer for editing your password.
 * @export
 * @interface EditPasswordRequest
 */
export interface EditPasswordRequest {
    /**
     * 
     * @type {string}
     * @memberof EditPasswordRequest
     */
    oldPassword: string;
    /**
     * 
     * @type {string}
     * @memberof EditPasswordRequest
     */
    newPassword: string;
    /**
     * 
     * @type {string}
     * @memberof EditPasswordRequest
     */
    confirmNewPassword: string;
}

export function EditPasswordRequestFromJSON(json: any): EditPasswordRequest {
    return EditPasswordRequestFromJSONTyped(json, false);
}

export function EditPasswordRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): EditPasswordRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'oldPassword': json['old_password'],
        'newPassword': json['new_password'],
        'confirmNewPassword': json['confirm_new_password'],
    };
}

export function EditPasswordRequestToJSON(value?: EditPasswordRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'old_password': value.oldPassword,
        'new_password': value.newPassword,
        'confirm_new_password': value.confirmNewPassword,
    };
}

