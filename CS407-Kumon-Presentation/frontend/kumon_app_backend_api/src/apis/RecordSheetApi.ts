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
    StudentRecordSheetRequest,
    StudentRecordSheetRequestFromJSON,
    StudentRecordSheetRequestToJSON,
} from '../models';

export interface RecordSheetCreateStudentSheetCreateRequest {
    studentRecordSheetRequest: StudentRecordSheetRequest;
}

/**
 * 
 */
export class RecordSheetApi extends runtime.BaseAPI {

    /**
     */
    async recordSheetCreateStudentSheetCreateRaw(requestParameters: RecordSheetCreateStudentSheetCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Blob>> {
        if (requestParameters.studentRecordSheetRequest === null || requestParameters.studentRecordSheetRequest === undefined) {
            throw new runtime.RequiredError('studentRecordSheetRequest','Required parameter requestParameters.studentRecordSheetRequest was null or undefined when calling recordSheetCreateStudentSheetCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/record-sheet/create_student_sheet/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: StudentRecordSheetRequestToJSON(requestParameters.studentRecordSheetRequest),
        }, initOverrides);

        return new runtime.BlobApiResponse(response);
    }

    /**
     */
    async recordSheetCreateStudentSheetCreate(requestParameters: RecordSheetCreateStudentSheetCreateRequest, initOverrides?: RequestInit): Promise<Blob> {
        const response = await this.recordSheetCreateStudentSheetCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
