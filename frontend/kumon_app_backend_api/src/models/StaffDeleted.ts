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
 * Serializer for listing deleted students.
 * @export
 * @interface StaffDeleted
 */
export interface StaffDeleted {
    /**
     * 
     * @type {number}
     * @memberof StaffDeleted
     */
    readonly id: number;
    /**
     * 
     * @type {string}
     * @memberof StaffDeleted
     */
    firstName: string;
    /**
     * 
     * @type {string}
     * @memberof StaffDeleted
     */
    middleName?: string;
    /**
     * 
     * @type {string}
     * @memberof StaffDeleted
     */
    lastName: string;
    /**
     * 
     * @type {string}
     * @memberof StaffDeleted
     */
    jobTitle: string;
    /**
     * 
     * @type {Date}
     * @memberof StaffDeleted
     */
    deletedAt?: Date | null;
    /**
     * 
     * @type {Date}
     * @memberof StaffDeleted
     */
    readonly permanentDeletionDate: Date;
}

export function StaffDeletedFromJSON(json: any): StaffDeleted {
    return StaffDeletedFromJSONTyped(json, false);
}

export function StaffDeletedFromJSONTyped(json: any, ignoreDiscriminator: boolean): StaffDeleted {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'firstName': json['first_name'],
        'middleName': !exists(json, 'middle_name') ? undefined : json['middle_name'],
        'lastName': json['last_name'],
        'jobTitle': json['job_title'],
        'deletedAt': !exists(json, 'deleted_at') ? undefined : (json['deleted_at'] === null ? null : new Date(json['deleted_at'])),
        'permanentDeletionDate': (new Date(json['permanent_deletion_date'])),
    };
}

export function StaffDeletedToJSON(value?: StaffDeleted | null): any {
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
        'deleted_at': value.deletedAt === undefined ? undefined : (value.deletedAt === null ? null : value.deletedAt.toISOString()),
    };
}

