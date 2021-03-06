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
    ItemRestockRequest,
    ItemRestockRequestFromJSON,
    ItemRestockRequestToJSON,
    ItemWithdrawRequest,
    ItemWithdrawRequestFromJSON,
    ItemWithdrawRequestToJSON,
    PaginatedWorksheetLogList,
    PaginatedWorksheetLogListFromJSON,
    PaginatedWorksheetLogListToJSON,
    PaginatedWorksheetViewList,
    PaginatedWorksheetViewListFromJSON,
    PaginatedWorksheetViewListToJSON,
    PatchedWorksheetEditRequest,
    PatchedWorksheetEditRequestFromJSON,
    PatchedWorksheetEditRequestToJSON,
    WorksheetEdit,
    WorksheetEditFromJSON,
    WorksheetEditToJSON,
    WorksheetEditRequest,
    WorksheetEditRequestFromJSON,
    WorksheetEditRequestToJSON,
    WorksheetView,
    WorksheetViewFromJSON,
    WorksheetViewToJSON,
} from '../models';

export interface WorksheetCreateRequest {
    worksheetEditRequest: WorksheetEditRequest;
}

export interface WorksheetDestroyRequest {
    id: number;
}

export interface WorksheetHistoryListRequest {
    id: number;
    page?: number;
}

export interface WorksheetListRequest {
    page?: number;
}

export interface WorksheetPartialUpdateRequest {
    id: number;
    patchedWorksheetEditRequest?: PatchedWorksheetEditRequest;
}

export interface WorksheetRestockCreateRequest {
    id: number;
    itemRestockRequest: ItemRestockRequest;
}

export interface WorksheetRetrieveRequest {
    id: number;
}

export interface WorksheetUpdateRequest {
    id: number;
    worksheetEditRequest: WorksheetEditRequest;
}

export interface WorksheetWithdrawCreateRequest {
    id: number;
    itemWithdrawRequest: ItemWithdrawRequest;
}

/**
 * 
 */
export class WorksheetApi extends runtime.BaseAPI {

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetCreateRaw(requestParameters: WorksheetCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<WorksheetEdit>> {
        if (requestParameters.worksheetEditRequest === null || requestParameters.worksheetEditRequest === undefined) {
            throw new runtime.RequiredError('worksheetEditRequest','Required parameter requestParameters.worksheetEditRequest was null or undefined when calling worksheetCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: WorksheetEditRequestToJSON(requestParameters.worksheetEditRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => WorksheetEditFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetCreate(requestParameters: WorksheetCreateRequest, initOverrides?: RequestInit): Promise<WorksheetEdit> {
        const response = await this.worksheetCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetDestroyRaw(requestParameters: WorksheetDestroyRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling worksheetDestroy.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetDestroy(requestParameters: WorksheetDestroyRequest, initOverrides?: RequestInit): Promise<void> {
        await this.worksheetDestroyRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetHistoryListRaw(requestParameters: WorksheetHistoryListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<PaginatedWorksheetLogList>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling worksheetHistoryList.');
        }

        const queryParameters: any = {};

        if (requestParameters.page !== undefined) {
            queryParameters['page'] = requestParameters.page;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/{id}/history/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => PaginatedWorksheetLogListFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetHistoryList(requestParameters: WorksheetHistoryListRequest, initOverrides?: RequestInit): Promise<PaginatedWorksheetLogList> {
        const response = await this.worksheetHistoryListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetListRaw(requestParameters: WorksheetListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<PaginatedWorksheetViewList>> {
        const queryParameters: any = {};

        if (requestParameters.page !== undefined) {
            queryParameters['page'] = requestParameters.page;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => PaginatedWorksheetViewListFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetList(requestParameters: WorksheetListRequest, initOverrides?: RequestInit): Promise<PaginatedWorksheetViewList> {
        const response = await this.worksheetListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetPartialUpdateRaw(requestParameters: WorksheetPartialUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<WorksheetEdit>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling worksheetPartialUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PATCH',
            headers: headerParameters,
            query: queryParameters,
            body: PatchedWorksheetEditRequestToJSON(requestParameters.patchedWorksheetEditRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => WorksheetEditFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetPartialUpdate(requestParameters: WorksheetPartialUpdateRequest, initOverrides?: RequestInit): Promise<WorksheetEdit> {
        const response = await this.worksheetPartialUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetRecordSheetRetrieveRaw(initOverrides?: RequestInit): Promise<runtime.ApiResponse<WorksheetEdit>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/record_sheet/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => WorksheetEditFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetRecordSheetRetrieve(initOverrides?: RequestInit): Promise<WorksheetEdit> {
        const response = await this.worksheetRecordSheetRetrieveRaw(initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetRestockCreateRaw(requestParameters: WorksheetRestockCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling worksheetRestockCreate.');
        }

        if (requestParameters.itemRestockRequest === null || requestParameters.itemRestockRequest === undefined) {
            throw new runtime.RequiredError('itemRestockRequest','Required parameter requestParameters.itemRestockRequest was null or undefined when calling worksheetRestockCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/{id}/restock/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: ItemRestockRequestToJSON(requestParameters.itemRestockRequest),
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetRestockCreate(requestParameters: WorksheetRestockCreateRequest, initOverrides?: RequestInit): Promise<void> {
        await this.worksheetRestockCreateRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetRetrieveRaw(requestParameters: WorksheetRetrieveRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<WorksheetView>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling worksheetRetrieve.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => WorksheetViewFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetRetrieve(requestParameters: WorksheetRetrieveRequest, initOverrides?: RequestInit): Promise<WorksheetView> {
        const response = await this.worksheetRetrieveRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetUpdateRaw(requestParameters: WorksheetUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<WorksheetEdit>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling worksheetUpdate.');
        }

        if (requestParameters.worksheetEditRequest === null || requestParameters.worksheetEditRequest === undefined) {
            throw new runtime.RequiredError('worksheetEditRequest','Required parameter requestParameters.worksheetEditRequest was null or undefined when calling worksheetUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PUT',
            headers: headerParameters,
            query: queryParameters,
            body: WorksheetEditRequestToJSON(requestParameters.worksheetEditRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => WorksheetEditFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetUpdate(requestParameters: WorksheetUpdateRequest, initOverrides?: RequestInit): Promise<WorksheetEdit> {
        const response = await this.worksheetUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetWithdrawCreateRaw(requestParameters: WorksheetWithdrawCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling worksheetWithdrawCreate.');
        }

        if (requestParameters.itemWithdrawRequest === null || requestParameters.itemWithdrawRequest === undefined) {
            throw new runtime.RequiredError('itemWithdrawRequest','Required parameter requestParameters.itemWithdrawRequest was null or undefined when calling worksheetWithdrawCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/worksheet/{id}/withdraw/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: ItemWithdrawRequestToJSON(requestParameters.itemWithdrawRequest),
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for managing worksheet inventory.
     */
    async worksheetWithdrawCreate(requestParameters: WorksheetWithdrawCreateRequest, initOverrides?: RequestInit): Promise<void> {
        await this.worksheetWithdrawCreateRaw(requestParameters, initOverrides);
    }

}
