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

/**
 * 
 * @export
 * @enum {string}
 */
export enum TypeEnum {
    KSis = 'k_sis',
    Dumps = 'dumps'
}

export function TypeEnumFromJSON(json: any): TypeEnum {
    return TypeEnumFromJSONTyped(json, false);
}

export function TypeEnumFromJSONTyped(json: any, ignoreDiscriminator: boolean): TypeEnum {
    return json as TypeEnum;
}

export function TypeEnumToJSON(value?: TypeEnum | null): any {
    return value as any;
}

