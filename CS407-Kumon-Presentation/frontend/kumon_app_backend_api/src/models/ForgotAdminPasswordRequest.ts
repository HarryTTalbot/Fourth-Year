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
 * Serializer for setting a new admin password.
 * @export
 * @interface ForgotAdminPasswordRequest
 */
export interface ForgotAdminPasswordRequest {
    /**
     * 
     * @type {string}
     * @memberof ForgotAdminPasswordRequest
     */
    passcode: string;
    /**
     * 
     * @type {string}
     * @memberof ForgotAdminPasswordRequest
     */
    newPassword: string;
    /**
     * 
     * @type {string}
     * @memberof ForgotAdminPasswordRequest
     */
    confirmNewPassword: string;
}

export function ForgotAdminPasswordRequestFromJSON(json: any): ForgotAdminPasswordRequest {
    return ForgotAdminPasswordRequestFromJSONTyped(json, false);
}

export function ForgotAdminPasswordRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): ForgotAdminPasswordRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'passcode': json['passcode'],
        'newPassword': json['new_password'],
        'confirmNewPassword': json['confirm_new_password'],
    };
}

export function ForgotAdminPasswordRequestToJSON(value?: ForgotAdminPasswordRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'passcode': value.passcode,
        'new_password': value.newPassword,
        'confirm_new_password': value.confirmNewPassword,
    };
}

