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
    LessonEdit,
    LessonEditFromJSON,
    LessonEditToJSON,
    LessonEditRequest,
    LessonEditRequestFromJSON,
    LessonEditRequestToJSON,
    LessonGetAttendance,
    LessonGetAttendanceFromJSON,
    LessonGetAttendanceToJSON,
    LessonSetAttendanceRequest,
    LessonSetAttendanceRequestFromJSON,
    LessonSetAttendanceRequestToJSON,
    LessonView,
    LessonViewFromJSON,
    LessonViewToJSON,
    PaginatedLessonViewList,
    PaginatedLessonViewListFromJSON,
    PaginatedLessonViewListToJSON,
    PatchedLessonEditRequest,
    PatchedLessonEditRequestFromJSON,
    PatchedLessonEditRequestToJSON,
} from '../models';

export interface LessonCreateRequest {
    lessonEditRequest: LessonEditRequest;
}

export interface LessonDestroyRequest {
    id: number;
}

export interface LessonGetAttendanceListRequest {
    id: number;
}

export interface LessonGetAttendanceSheetRetrieveRequest {
    id: number;
}

export interface LessonListRequest {
    page?: number;
}

export interface LessonPartialUpdateRequest {
    id: number;
    patchedLessonEditRequest?: PatchedLessonEditRequest;
}

export interface LessonPastListRequest {
    page?: number;
}

export interface LessonRetrieveRequest {
    id: number;
}

export interface LessonSetAttendanceCreateRequest {
    id: number;
    lessonSetAttendanceRequest: Array<LessonSetAttendanceRequest>;
}

export interface LessonUpdateRequest {
    id: number;
    lessonEditRequest: LessonEditRequest;
}

/**
 * 
 */
export class LessonApi extends runtime.BaseAPI {

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonCreateRaw(requestParameters: LessonCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<LessonEdit>> {
        if (requestParameters.lessonEditRequest === null || requestParameters.lessonEditRequest === undefined) {
            throw new runtime.RequiredError('lessonEditRequest','Required parameter requestParameters.lessonEditRequest was null or undefined when calling lessonCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: LessonEditRequestToJSON(requestParameters.lessonEditRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => LessonEditFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonCreate(requestParameters: LessonCreateRequest, initOverrides?: RequestInit): Promise<LessonEdit> {
        const response = await this.lessonCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonDestroyRaw(requestParameters: LessonDestroyRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling lessonDestroy.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonDestroy(requestParameters: LessonDestroyRequest, initOverrides?: RequestInit): Promise<void> {
        await this.lessonDestroyRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonGetAttendanceListRaw(requestParameters: LessonGetAttendanceListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<LessonGetAttendance>>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling lessonGetAttendanceList.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/{id}/get_attendance/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(LessonGetAttendanceFromJSON));
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonGetAttendanceList(requestParameters: LessonGetAttendanceListRequest, initOverrides?: RequestInit): Promise<Array<LessonGetAttendance>> {
        const response = await this.lessonGetAttendanceListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Returns a printable PDF for recording attendance
     */
    async lessonGetAttendanceSheetRetrieveRaw(requestParameters: LessonGetAttendanceSheetRetrieveRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Blob>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling lessonGetAttendanceSheetRetrieve.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/{id}/get_attendance_sheet/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.BlobApiResponse(response);
    }

    /**
     * Returns a printable PDF for recording attendance
     */
    async lessonGetAttendanceSheetRetrieve(requestParameters: LessonGetAttendanceSheetRetrieveRequest, initOverrides?: RequestInit): Promise<Blob> {
        const response = await this.lessonGetAttendanceSheetRetrieveRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonListRaw(requestParameters: LessonListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<PaginatedLessonViewList>> {
        const queryParameters: any = {};

        if (requestParameters.page !== undefined) {
            queryParameters['page'] = requestParameters.page;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => PaginatedLessonViewListFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonList(requestParameters: LessonListRequest, initOverrides?: RequestInit): Promise<PaginatedLessonViewList> {
        const response = await this.lessonListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonPartialUpdateRaw(requestParameters: LessonPartialUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<LessonEdit>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling lessonPartialUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PATCH',
            headers: headerParameters,
            query: queryParameters,
            body: PatchedLessonEditRequestToJSON(requestParameters.patchedLessonEditRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => LessonEditFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonPartialUpdate(requestParameters: LessonPartialUpdateRequest, initOverrides?: RequestInit): Promise<LessonEdit> {
        const response = await this.lessonPartialUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonPastListRaw(requestParameters: LessonPastListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<PaginatedLessonViewList>> {
        const queryParameters: any = {};

        if (requestParameters.page !== undefined) {
            queryParameters['page'] = requestParameters.page;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/past/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => PaginatedLessonViewListFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonPastList(requestParameters: LessonPastListRequest, initOverrides?: RequestInit): Promise<PaginatedLessonViewList> {
        const response = await this.lessonPastListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonRetrieveRaw(requestParameters: LessonRetrieveRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<LessonView>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling lessonRetrieve.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => LessonViewFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonRetrieve(requestParameters: LessonRetrieveRequest, initOverrides?: RequestInit): Promise<LessonView> {
        const response = await this.lessonRetrieveRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonSetAttendanceCreateRaw(requestParameters: LessonSetAttendanceCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling lessonSetAttendanceCreate.');
        }

        if (requestParameters.lessonSetAttendanceRequest === null || requestParameters.lessonSetAttendanceRequest === undefined) {
            throw new runtime.RequiredError('lessonSetAttendanceRequest','Required parameter requestParameters.lessonSetAttendanceRequest was null or undefined when calling lessonSetAttendanceCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/{id}/set_attendance/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: requestParameters.lessonSetAttendanceRequest.map(LessonSetAttendanceRequestToJSON),
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonSetAttendanceCreate(requestParameters: LessonSetAttendanceCreateRequest, initOverrides?: RequestInit): Promise<void> {
        await this.lessonSetAttendanceCreateRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonTodayListRaw(initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<LessonView>>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/today/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(LessonViewFromJSON));
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonTodayList(initOverrides?: RequestInit): Promise<Array<LessonView>> {
        const response = await this.lessonTodayListRaw(initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonUpdateRaw(requestParameters: LessonUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<LessonEdit>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling lessonUpdate.');
        }

        if (requestParameters.lessonEditRequest === null || requestParameters.lessonEditRequest === undefined) {
            throw new runtime.RequiredError('lessonEditRequest','Required parameter requestParameters.lessonEditRequest was null or undefined when calling lessonUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/lesson/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PUT',
            headers: headerParameters,
            query: queryParameters,
            body: LessonEditRequestToJSON(requestParameters.lessonEditRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => LessonEditFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing lesson information.
     */
    async lessonUpdate(requestParameters: LessonUpdateRequest, initOverrides?: RequestInit): Promise<LessonEdit> {
        const response = await this.lessonUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
