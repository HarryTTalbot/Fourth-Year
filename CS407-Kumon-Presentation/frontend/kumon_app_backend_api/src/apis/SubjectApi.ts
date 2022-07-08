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


import * as runtime from '../runtime';
import {
    PatchedSubjectRequest,
    PatchedSubjectRequestFromJSON,
    PatchedSubjectRequestToJSON,
    Subject,
    SubjectFromJSON,
    SubjectToJSON,
    SubjectAddLevelRequest,
    SubjectAddLevelRequestFromJSON,
    SubjectAddLevelRequestToJSON,
    SubjectGetLevel,
    SubjectGetLevelFromJSON,
    SubjectGetLevelToJSON,
    SubjectRemoveLevelRequest,
    SubjectRemoveLevelRequestFromJSON,
    SubjectRemoveLevelRequestToJSON,
    SubjectRequest,
    SubjectRequestFromJSON,
    SubjectRequestToJSON,
} from '../models';

export interface SubjectAddLevelCreateRequest {
    id: number;
    subjectAddLevelRequest: SubjectAddLevelRequest;
}

export interface SubjectCreateRequest {
    subjectRequest: SubjectRequest;
}

export interface SubjectDestroyRequest {
    id: number;
}

export interface SubjectGetLevelsListRequest {
    id: number;
    search?: string;
}

export interface SubjectListRequest {
    search?: string;
}

export interface SubjectPartialUpdateRequest {
    id: number;
    patchedSubjectRequest?: PatchedSubjectRequest;
}

export interface SubjectRemoveLevelCreateRequest {
    id: number;
    subjectRemoveLevelRequest: SubjectRemoveLevelRequest;
}

export interface SubjectRetrieveRequest {
    id: number;
}

export interface SubjectUpdateRequest {
    id: number;
    subjectRequest: SubjectRequest;
}

/**
 * 
 */
export class SubjectApi extends runtime.BaseAPI {

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectAddLevelCreateRaw(requestParameters: SubjectAddLevelCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling subjectAddLevelCreate.');
        }

        if (requestParameters.subjectAddLevelRequest === null || requestParameters.subjectAddLevelRequest === undefined) {
            throw new runtime.RequiredError('subjectAddLevelRequest','Required parameter requestParameters.subjectAddLevelRequest was null or undefined when calling subjectAddLevelCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/subject/{id}/add_level/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: SubjectAddLevelRequestToJSON(requestParameters.subjectAddLevelRequest),
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectAddLevelCreate(requestParameters: SubjectAddLevelCreateRequest, initOverrides?: RequestInit): Promise<void> {
        await this.subjectAddLevelCreateRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectCreateRaw(requestParameters: SubjectCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Subject>> {
        if (requestParameters.subjectRequest === null || requestParameters.subjectRequest === undefined) {
            throw new runtime.RequiredError('subjectRequest','Required parameter requestParameters.subjectRequest was null or undefined when calling subjectCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/subject/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: SubjectRequestToJSON(requestParameters.subjectRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => SubjectFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectCreate(requestParameters: SubjectCreateRequest, initOverrides?: RequestInit): Promise<Subject> {
        const response = await this.subjectCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectDestroyRaw(requestParameters: SubjectDestroyRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling subjectDestroy.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/subject/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectDestroy(requestParameters: SubjectDestroyRequest, initOverrides?: RequestInit): Promise<void> {
        await this.subjectDestroyRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectGetLevelsListRaw(requestParameters: SubjectGetLevelsListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<SubjectGetLevel>>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling subjectGetLevelsList.');
        }

        const queryParameters: any = {};

        if (requestParameters.search !== undefined) {
            queryParameters['search'] = requestParameters.search;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/subject/{id}/get_levels/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(SubjectGetLevelFromJSON));
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectGetLevelsList(requestParameters: SubjectGetLevelsListRequest, initOverrides?: RequestInit): Promise<Array<SubjectGetLevel>> {
        const response = await this.subjectGetLevelsListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectListRaw(requestParameters: SubjectListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<Subject>>> {
        const queryParameters: any = {};

        if (requestParameters.search !== undefined) {
            queryParameters['search'] = requestParameters.search;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/subject/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(SubjectFromJSON));
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectList(requestParameters: SubjectListRequest, initOverrides?: RequestInit): Promise<Array<Subject>> {
        const response = await this.subjectListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectPartialUpdateRaw(requestParameters: SubjectPartialUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Subject>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling subjectPartialUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/subject/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PATCH',
            headers: headerParameters,
            query: queryParameters,
            body: PatchedSubjectRequestToJSON(requestParameters.patchedSubjectRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => SubjectFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectPartialUpdate(requestParameters: SubjectPartialUpdateRequest, initOverrides?: RequestInit): Promise<Subject> {
        const response = await this.subjectPartialUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectRemoveLevelCreateRaw(requestParameters: SubjectRemoveLevelCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling subjectRemoveLevelCreate.');
        }

        if (requestParameters.subjectRemoveLevelRequest === null || requestParameters.subjectRemoveLevelRequest === undefined) {
            throw new runtime.RequiredError('subjectRemoveLevelRequest','Required parameter requestParameters.subjectRemoveLevelRequest was null or undefined when calling subjectRemoveLevelCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/subject/{id}/remove_level/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: SubjectRemoveLevelRequestToJSON(requestParameters.subjectRemoveLevelRequest),
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectRemoveLevelCreate(requestParameters: SubjectRemoveLevelCreateRequest, initOverrides?: RequestInit): Promise<void> {
        await this.subjectRemoveLevelCreateRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectRetrieveRaw(requestParameters: SubjectRetrieveRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Subject>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling subjectRetrieve.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/subject/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => SubjectFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectRetrieve(requestParameters: SubjectRetrieveRequest, initOverrides?: RequestInit): Promise<Subject> {
        const response = await this.subjectRetrieveRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectUpdateRaw(requestParameters: SubjectUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Subject>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling subjectUpdate.');
        }

        if (requestParameters.subjectRequest === null || requestParameters.subjectRequest === undefined) {
            throw new runtime.RequiredError('subjectRequest','Required parameter requestParameters.subjectRequest was null or undefined when calling subjectUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/subject/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PUT',
            headers: headerParameters,
            query: queryParameters,
            body: SubjectRequestToJSON(requestParameters.subjectRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => SubjectFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing subject and subject level information.
     */
    async subjectUpdate(requestParameters: SubjectUpdateRequest, initOverrides?: RequestInit): Promise<Subject> {
        const response = await this.subjectUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

}