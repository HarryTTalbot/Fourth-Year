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
    Lesson,
    LessonFromJSON,
    LessonFromJSONTyped,
    LessonToJSON,
} from './Lesson';

/**
 * 
 * @export
 * @interface PaginatedLessonList
 */
export interface PaginatedLessonList {
    /**
     * 
     * @type {number}
     * @memberof PaginatedLessonList
     */
    count?: number;
    /**
     * 
     * @type {string}
     * @memberof PaginatedLessonList
     */
    next?: string | null;
    /**
     * 
     * @type {string}
     * @memberof PaginatedLessonList
     */
    previous?: string | null;
    /**
     * 
     * @type {Array<Lesson>}
     * @memberof PaginatedLessonList
     */
    results?: Array<Lesson>;
}

export function PaginatedLessonListFromJSON(json: any): PaginatedLessonList {
    return PaginatedLessonListFromJSONTyped(json, false);
}

export function PaginatedLessonListFromJSONTyped(json: any, ignoreDiscriminator: boolean): PaginatedLessonList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'count': !exists(json, 'count') ? undefined : json['count'],
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': !exists(json, 'results') ? undefined : ((json['results'] as Array<any>).map(LessonFromJSON)),
    };
}

export function PaginatedLessonListToJSON(value?: PaginatedLessonList | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'count': value.count,
        'next': value.next,
        'previous': value.previous,
        'results': value.results === undefined ? undefined : ((value.results as Array<any>).map(LessonToJSON)),
    };
}

