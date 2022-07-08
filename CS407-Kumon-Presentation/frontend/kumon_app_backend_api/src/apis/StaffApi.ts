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
    PaginatedStaffList,
    PaginatedStaffListFromJSON,
    PaginatedStaffListToJSON,
    PatchedStaffRequest,
    PatchedStaffRequestFromJSON,
    PatchedStaffRequestToJSON,
    Staff,
    StaffFromJSON,
    StaffToJSON,
    StaffCreate,
    StaffCreateFromJSON,
    StaffCreateToJSON,
    StaffCreateRequest,
    StaffCreateRequestFromJSON,
    StaffCreateRequestToJSON,
    StaffRequest,
    StaffRequestFromJSON,
    StaffRequestToJSON,
    StudentDeleted,
    StudentDeletedFromJSON,
    StudentDeletedToJSON,
} from '../models';

export interface StaffCreateOperationRequest {
    staffCreateRequest: StaffCreateRequest;
}

export interface StaffDestroyRequest {
    id: number;
}

export interface StaffGdprDeleteDestroyRequest {
    id: number;
}

export interface StaffGdprRestoreCreateRequest {
    id: number;
}

export interface StaffGetDataRetrieveRequest {
    id: number;
}

export interface StaffListRequest {
    page?: number;
    search?: string;
}

export interface StaffListDeletedListRequest {
    search?: string;
}

export interface StaffPartialUpdateRequest {
    id: number;
    patchedStaffRequest?: PatchedStaffRequest;
}

export interface StaffRetrieveRequest {
    id: number;
}

export interface StaffUpdateRequest {
    id: number;
    staffRequest: StaffRequest;
}

/**
 * 
 */
export class StaffApi extends runtime.BaseAPI {

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffCreateRaw(requestParameters: StaffCreateOperationRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<StaffCreate>> {
        if (requestParameters.staffCreateRequest === null || requestParameters.staffCreateRequest === undefined) {
            throw new runtime.RequiredError('staffCreateRequest','Required parameter requestParameters.staffCreateRequest was null or undefined when calling staffCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: StaffCreateRequestToJSON(requestParameters.staffCreateRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => StaffCreateFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffCreate(requestParameters: StaffCreateOperationRequest, initOverrides?: RequestInit): Promise<StaffCreate> {
        const response = await this.staffCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffDestroyRaw(requestParameters: StaffDestroyRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling staffDestroy.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffDestroy(requestParameters: StaffDestroyRequest, initOverrides?: RequestInit): Promise<void> {
        await this.staffDestroyRaw(requestParameters, initOverrides);
    }

    /**
     * Deletes records in a GDPR-compliant manner
     */
    async staffGdprDeleteDestroyRaw(requestParameters: StaffGdprDeleteDestroyRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling staffGdprDeleteDestroy.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/{id}/gdpr_delete/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Deletes records in a GDPR-compliant manner
     */
    async staffGdprDeleteDestroy(requestParameters: StaffGdprDeleteDestroyRequest, initOverrides?: RequestInit): Promise<void> {
        await this.staffGdprDeleteDestroyRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffGdprRestoreCreateRaw(requestParameters: StaffGdprRestoreCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling staffGdprRestoreCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/{id}/gdpr_restore/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffGdprRestoreCreate(requestParameters: StaffGdprRestoreCreateRequest, initOverrides?: RequestInit): Promise<void> {
        await this.staffGdprRestoreCreateRaw(requestParameters, initOverrides);
    }

    /**
     * Returns a summary of all of the data stored about a staff member in PDF format
     */
    async staffGetDataRetrieveRaw(requestParameters: StaffGetDataRetrieveRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Blob>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling staffGetDataRetrieve.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/{id}/get_data/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.BlobApiResponse(response);
    }

    /**
     * Returns a summary of all of the data stored about a staff member in PDF format
     */
    async staffGetDataRetrieve(requestParameters: StaffGetDataRetrieveRequest, initOverrides?: RequestInit): Promise<Blob> {
        const response = await this.staffGetDataRetrieveRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffListRaw(requestParameters: StaffListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<PaginatedStaffList>> {
        const queryParameters: any = {};

        if (requestParameters.page !== undefined) {
            queryParameters['page'] = requestParameters.page;
        }

        if (requestParameters.search !== undefined) {
            queryParameters['search'] = requestParameters.search;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => PaginatedStaffListFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffList(requestParameters: StaffListRequest, initOverrides?: RequestInit): Promise<PaginatedStaffList> {
        const response = await this.staffListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffListDeletedListRaw(requestParameters: StaffListDeletedListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<StudentDeleted>>> {
        const queryParameters: any = {};

        if (requestParameters.search !== undefined) {
            queryParameters['search'] = requestParameters.search;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/list_deleted/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(StudentDeletedFromJSON));
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffListDeletedList(requestParameters: StaffListDeletedListRequest, initOverrides?: RequestInit): Promise<Array<StudentDeleted>> {
        const response = await this.staffListDeletedListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffPartialUpdateRaw(requestParameters: StaffPartialUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Staff>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling staffPartialUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PATCH',
            headers: headerParameters,
            query: queryParameters,
            body: PatchedStaffRequestToJSON(requestParameters.patchedStaffRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => StaffFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffPartialUpdate(requestParameters: StaffPartialUpdateRequest, initOverrides?: RequestInit): Promise<Staff> {
        const response = await this.staffPartialUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffRetrieveRaw(requestParameters: StaffRetrieveRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Staff>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling staffRetrieve.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => StaffFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffRetrieve(requestParameters: StaffRetrieveRequest, initOverrides?: RequestInit): Promise<Staff> {
        const response = await this.staffRetrieveRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffUpdateRaw(requestParameters: StaffUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Staff>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling staffUpdate.');
        }

        if (requestParameters.staffRequest === null || requestParameters.staffRequest === undefined) {
            throw new runtime.RequiredError('staffRequest','Required parameter requestParameters.staffRequest was null or undefined when calling staffUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/staff/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PUT',
            headers: headerParameters,
            query: queryParameters,
            body: StaffRequestToJSON(requestParameters.staffRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => StaffFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing staff information.
     */
    async staffUpdate(requestParameters: StaffUpdateRequest, initOverrides?: RequestInit): Promise<Staff> {
        const response = await this.staffUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

}