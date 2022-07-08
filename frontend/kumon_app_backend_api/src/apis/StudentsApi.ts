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
    Class,
    ClassFromJSON,
    ClassToJSON,
    PaginatedLessonViewList,
    PaginatedLessonViewListFromJSON,
    PaginatedLessonViewListToJSON,
    PaginatedStudentGetAttendanceList,
    PaginatedStudentGetAttendanceListFromJSON,
    PaginatedStudentGetAttendanceListToJSON,
    PaginatedStudentListList,
    PaginatedStudentListListFromJSON,
    PaginatedStudentListListToJSON,
    PatchedStudentRequest,
    PatchedStudentRequestFromJSON,
    PatchedStudentRequestToJSON,
    Student,
    StudentFromJSON,
    StudentToJSON,
    StudentAddContactsRequest,
    StudentAddContactsRequestFromJSON,
    StudentAddContactsRequestToJSON,
    StudentDeleted,
    StudentDeletedFromJSON,
    StudentDeletedToJSON,
    StudentGetContacts,
    StudentGetContactsFromJSON,
    StudentGetContactsToJSON,
    StudentRemoveContactsRequest,
    StudentRemoveContactsRequestFromJSON,
    StudentRemoveContactsRequestToJSON,
    StudentRequest,
    StudentRequestFromJSON,
    StudentRequestToJSON,
} from '../models';

export interface StudentsAddContactsCreateRequest {
    id: number;
    studentAddContactsRequest: Array<StudentAddContactsRequest>;
}

export interface StudentsCreateRequest {
    studentRequest: StudentRequest;
}

export interface StudentsDestroyRequest {
    id: number;
}

export interface StudentsGdprDeleteDestroyRequest {
    id: number;
}

export interface StudentsGdprRestoreCreateRequest {
    id: number;
}

export interface StudentsGetAttendanceListRequest {
    id: number;
    page?: number;
    search?: string;
}

export interface StudentsGetClassesListRequest {
    id: number;
    search?: string;
}

export interface StudentsGetContactsListRequest {
    id: number;
    search?: string;
}

export interface StudentsGetDataRetrieveRequest {
    id: number;
}

export interface StudentsGetLessonsListRequest {
    id: number;
    page?: number;
    search?: string;
}

export interface StudentsListRequest {
    page?: number;
    search?: string;
}

export interface StudentsListDeletedListRequest {
    search?: string;
}

export interface StudentsPartialUpdateRequest {
    id: number;
    patchedStudentRequest?: PatchedStudentRequest;
}

export interface StudentsRemoveContactsCreateRequest {
    id: number;
    studentRemoveContactsRequest: Array<StudentRemoveContactsRequest>;
}

export interface StudentsRetrieveRequest {
    id: number;
}

export interface StudentsUpdateRequest {
    id: number;
    studentRequest: StudentRequest;
}

/**
 * 
 */
export class StudentsApi extends runtime.BaseAPI {

    /**
     * Adds the given contacts to the specified student.
     */
    async studentsAddContactsCreateRaw(requestParameters: StudentsAddContactsCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsAddContactsCreate.');
        }

        if (requestParameters.studentAddContactsRequest === null || requestParameters.studentAddContactsRequest === undefined) {
            throw new runtime.RequiredError('studentAddContactsRequest','Required parameter requestParameters.studentAddContactsRequest was null or undefined when calling studentsAddContactsCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/{id}/add_contacts/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: requestParameters.studentAddContactsRequest.map(StudentAddContactsRequestToJSON),
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Adds the given contacts to the specified student.
     */
    async studentsAddContactsCreate(requestParameters: StudentsAddContactsCreateRequest, initOverrides?: RequestInit): Promise<void> {
        await this.studentsAddContactsCreateRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsCreateRaw(requestParameters: StudentsCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Student>> {
        if (requestParameters.studentRequest === null || requestParameters.studentRequest === undefined) {
            throw new runtime.RequiredError('studentRequest','Required parameter requestParameters.studentRequest was null or undefined when calling studentsCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: StudentRequestToJSON(requestParameters.studentRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => StudentFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsCreate(requestParameters: StudentsCreateRequest, initOverrides?: RequestInit): Promise<Student> {
        const response = await this.studentsCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsDestroyRaw(requestParameters: StudentsDestroyRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsDestroy.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsDestroy(requestParameters: StudentsDestroyRequest, initOverrides?: RequestInit): Promise<void> {
        await this.studentsDestroyRaw(requestParameters, initOverrides);
    }

    /**
     * Deletes records in a GDPR-compliant manner
     */
    async studentsGdprDeleteDestroyRaw(requestParameters: StudentsGdprDeleteDestroyRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsGdprDeleteDestroy.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/{id}/gdpr_delete/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Deletes records in a GDPR-compliant manner
     */
    async studentsGdprDeleteDestroy(requestParameters: StudentsGdprDeleteDestroyRequest, initOverrides?: RequestInit): Promise<void> {
        await this.studentsGdprDeleteDestroyRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsGdprRestoreCreateRaw(requestParameters: StudentsGdprRestoreCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsGdprRestoreCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/{id}/gdpr_restore/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsGdprRestoreCreate(requestParameters: StudentsGdprRestoreCreateRequest, initOverrides?: RequestInit): Promise<void> {
        await this.studentsGdprRestoreCreateRaw(requestParameters, initOverrides);
    }

    /**
     * Retrieves the lesson attendance record for the specified student.
     */
    async studentsGetAttendanceListRaw(requestParameters: StudentsGetAttendanceListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<PaginatedStudentGetAttendanceList>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsGetAttendanceList.');
        }

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
            path: `/api/students/{id}/get_attendance/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => PaginatedStudentGetAttendanceListFromJSON(jsonValue));
    }

    /**
     * Retrieves the lesson attendance record for the specified student.
     */
    async studentsGetAttendanceList(requestParameters: StudentsGetAttendanceListRequest, initOverrides?: RequestInit): Promise<PaginatedStudentGetAttendanceList> {
        const response = await this.studentsGetAttendanceListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Retrieves classes for the specified student belongs to.
     */
    async studentsGetClassesListRaw(requestParameters: StudentsGetClassesListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<Class>>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsGetClassesList.');
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
            path: `/api/students/{id}/get_classes/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(ClassFromJSON));
    }

    /**
     * Retrieves classes for the specified student belongs to.
     */
    async studentsGetClassesList(requestParameters: StudentsGetClassesListRequest, initOverrides?: RequestInit): Promise<Array<Class>> {
        const response = await this.studentsGetClassesListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Retrieves the contacts for the specified student.
     */
    async studentsGetContactsListRaw(requestParameters: StudentsGetContactsListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<StudentGetContacts>>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsGetContactsList.');
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
            path: `/api/students/{id}/get_contacts/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(StudentGetContactsFromJSON));
    }

    /**
     * Retrieves the contacts for the specified student.
     */
    async studentsGetContactsList(requestParameters: StudentsGetContactsListRequest, initOverrides?: RequestInit): Promise<Array<StudentGetContacts>> {
        const response = await this.studentsGetContactsListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Returns a summary of all of the data stored about a student in PDF format
     */
    async studentsGetDataRetrieveRaw(requestParameters: StudentsGetDataRetrieveRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Blob>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsGetDataRetrieve.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/{id}/get_data/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.BlobApiResponse(response);
    }

    /**
     * Returns a summary of all of the data stored about a student in PDF format
     */
    async studentsGetDataRetrieve(requestParameters: StudentsGetDataRetrieveRequest, initOverrides?: RequestInit): Promise<Blob> {
        const response = await this.studentsGetDataRetrieveRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Retrieves the specified student\'s lessons.
     */
    async studentsGetLessonsListRaw(requestParameters: StudentsGetLessonsListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<PaginatedLessonViewList>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsGetLessonsList.');
        }

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
            path: `/api/students/{id}/get_lessons/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => PaginatedLessonViewListFromJSON(jsonValue));
    }

    /**
     * Retrieves the specified student\'s lessons.
     */
    async studentsGetLessonsList(requestParameters: StudentsGetLessonsListRequest, initOverrides?: RequestInit): Promise<PaginatedLessonViewList> {
        const response = await this.studentsGetLessonsListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsListRaw(requestParameters: StudentsListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<PaginatedStudentListList>> {
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
            path: `/api/students/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => PaginatedStudentListListFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsList(requestParameters: StudentsListRequest, initOverrides?: RequestInit): Promise<PaginatedStudentListList> {
        const response = await this.studentsListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsListDeletedListRaw(requestParameters: StudentsListDeletedListRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Array<StudentDeleted>>> {
        const queryParameters: any = {};

        if (requestParameters.search !== undefined) {
            queryParameters['search'] = requestParameters.search;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/list_deleted/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(StudentDeletedFromJSON));
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsListDeletedList(requestParameters: StudentsListDeletedListRequest, initOverrides?: RequestInit): Promise<Array<StudentDeleted>> {
        const response = await this.studentsListDeletedListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsPartialUpdateRaw(requestParameters: StudentsPartialUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Student>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsPartialUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PATCH',
            headers: headerParameters,
            query: queryParameters,
            body: PatchedStudentRequestToJSON(requestParameters.patchedStudentRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => StudentFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsPartialUpdate(requestParameters: StudentsPartialUpdateRequest, initOverrides?: RequestInit): Promise<Student> {
        const response = await this.studentsPartialUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Removes the given contacts from the specified student.
     */
    async studentsRemoveContactsCreateRaw(requestParameters: StudentsRemoveContactsCreateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsRemoveContactsCreate.');
        }

        if (requestParameters.studentRemoveContactsRequest === null || requestParameters.studentRemoveContactsRequest === undefined) {
            throw new runtime.RequiredError('studentRemoveContactsRequest','Required parameter requestParameters.studentRemoveContactsRequest was null or undefined when calling studentsRemoveContactsCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/{id}/remove_contacts/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: requestParameters.studentRemoveContactsRequest.map(StudentRemoveContactsRequestToJSON),
        }, initOverrides);

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Removes the given contacts from the specified student.
     */
    async studentsRemoveContactsCreate(requestParameters: StudentsRemoveContactsCreateRequest, initOverrides?: RequestInit): Promise<void> {
        await this.studentsRemoveContactsCreateRaw(requestParameters, initOverrides);
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsRetrieveRaw(requestParameters: StudentsRetrieveRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Student>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsRetrieve.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => StudentFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsRetrieve(requestParameters: StudentsRetrieveRequest, initOverrides?: RequestInit): Promise<Student> {
        const response = await this.studentsRetrieveRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsUpdateRaw(requestParameters: StudentsUpdateRequest, initOverrides?: RequestInit): Promise<runtime.ApiResponse<Student>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling studentsUpdate.');
        }

        if (requestParameters.studentRequest === null || requestParameters.studentRequest === undefined) {
            throw new runtime.RequiredError('studentRequest','Required parameter requestParameters.studentRequest was null or undefined when calling studentsUpdate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && this.configuration.apiKey) {
            headerParameters["Authorization"] = this.configuration.apiKey("Authorization"); // tokenAuth authentication
        }

        const response = await this.request({
            path: `/api/students/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'PUT',
            headers: headerParameters,
            query: queryParameters,
            body: StudentRequestToJSON(requestParameters.studentRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => StudentFromJSON(jsonValue));
    }

    /**
     * Provides API functionality for viewing and editing student information.
     */
    async studentsUpdate(requestParameters: StudentsUpdateRequest, initOverrides?: RequestInit): Promise<Student> {
        const response = await this.studentsUpdateRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
