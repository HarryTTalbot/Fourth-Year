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
 * @interface AddAdminAccountRequest
 */
export interface AddAdminAccountRequest {
    /**
     * 
     * @type {string}
     * @memberof AddAdminAccountRequest
     */
    firstName: string;
    /**
     * 
     * @type {string}
     * @memberof AddAdminAccountRequest
     */
    middleName?: string;
    /**
     * 
     * @type {string}
     * @memberof AddAdminAccountRequest
     */
    lastName: string;
    /**
     * 
     * @type {string}
     * @memberof AddAdminAccountRequest
     */
    jobTitle: string;
    /**
     * 
     * @type {string}
     * @memberof AddAdminAccountRequest
     */
    username: string;
    /**
     * 
     * @type {string}
     * @memberof AddAdminAccountRequest
     */
    password: string;
    /**
     * 
     * @type {string}
     * @memberof AddAdminAccountRequest
     */
    confirmPassword: string;
    /**
     * 
     * @type {string}
     * @memberof AddAdminAccountRequest
     */
    passcode: string;
    /**
     * 
     * @type {string}
     * @memberof AddAdminAccountRequest
     */
    confirmPasscode: string;
}

export function AddAdminAccountRequestFromJSON(json: any): AddAdminAccountRequest {
    return AddAdminAccountRequestFromJSONTyped(json, false);
}

export function AddAdminAccountRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): AddAdminAccountRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'firstName': json['first_name'],
        'middleName': !exists(json, 'middle_name') ? undefined : json['middle_name'],
        'lastName': json['last_name'],
        'jobTitle': json['job_title'],
        'username': json['username'],
        'password': json['password'],
        'confirmPassword': json['confirm_password'],
        'passcode': json['passcode'],
        'confirmPasscode': json['confirm_passcode'],
    };
}

export function AddAdminAccountRequestToJSON(value?: AddAdminAccountRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'first_name': value.firstName,
        'middle_name': value.middleName,
        'last_name': value.lastName,
        'job_title': value.jobTitle,
        'username': value.username,
        'password': value.password,
        'confirm_password': value.confirmPassword,
        'passcode': value.passcode,
        'confirm_passcode': value.confirmPasscode,
    };
}

