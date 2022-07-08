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
    AddressRequest,
    AddressRequestFromJSON,
    AddressRequestFromJSONTyped,
    AddressRequestToJSON,
} from './AddressRequest';

/**
 * Serializer for contact details.
 * @export
 * @interface PatchedContactRequest
 */
export interface PatchedContactRequest {
    /**
     * 
     * @type {string}
     * @memberof PatchedContactRequest
     */
    firstName?: string;
    /**
     * 
     * @type {string}
     * @memberof PatchedContactRequest
     */
    middleName?: string;
    /**
     * 
     * @type {string}
     * @memberof PatchedContactRequest
     */
    lastName?: string;
    /**
     * 
     * @type {string}
     * @memberof PatchedContactRequest
     */
    phoneHome?: string;
    /**
     * 
     * @type {string}
     * @memberof PatchedContactRequest
     */
    phoneBusiness?: string;
    /**
     * 
     * @type {string}
     * @memberof PatchedContactRequest
     */
    phoneMobile?: string;
    /**
     * 
     * @type {string}
     * @memberof PatchedContactRequest
     */
    email?: string;
    /**
     * 
     * @type {AddressRequest}
     * @memberof PatchedContactRequest
     */
    address?: AddressRequest;
}

export function PatchedContactRequestFromJSON(json: any): PatchedContactRequest {
    return PatchedContactRequestFromJSONTyped(json, false);
}

export function PatchedContactRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): PatchedContactRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'firstName': !exists(json, 'first_name') ? undefined : json['first_name'],
        'middleName': !exists(json, 'middle_name') ? undefined : json['middle_name'],
        'lastName': !exists(json, 'last_name') ? undefined : json['last_name'],
        'phoneHome': !exists(json, 'phone_home') ? undefined : json['phone_home'],
        'phoneBusiness': !exists(json, 'phone_business') ? undefined : json['phone_business'],
        'phoneMobile': !exists(json, 'phone_mobile') ? undefined : json['phone_mobile'],
        'email': !exists(json, 'email') ? undefined : json['email'],
        'address': !exists(json, 'address') ? undefined : AddressRequestFromJSON(json['address']),
    };
}

export function PatchedContactRequestToJSON(value?: PatchedContactRequest | null): any {
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
        'phone_home': value.phoneHome,
        'phone_business': value.phoneBusiness,
        'phone_mobile': value.phoneMobile,
        'email': value.email,
        'address': AddressRequestToJSON(value.address),
    };
}
