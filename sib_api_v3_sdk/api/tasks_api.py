# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sib_api_v3_sdk.api_client import ApiClient


class TasksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def crm_tasks_get(self, **kwargs):  # noqa: E501
        """Get all tasks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter_type: Filter by task type (ID)
        :param str filter_status: Filter by task status
        :param str filter_date: Filter by date
        :param str filter_assign_to: Filter by assignTo id
        :param str filter_contacts: Filter by contact ids
        :param str filter_deals: Filter by deals ids
        :param str filter_companies: Filter by companies ids
        :param int date_from: dateFrom to date range filter type (timestamp in milliseconds)
        :param int date_to: dateTo to date range filter type (timestamp in milliseconds)
        :param int offset: Index of the first document of the page
        :param int limit: Number of documents per page
        :param str sort: Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed
        :param str sort_by: The field used to sort field names.
        :return: TaskList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.crm_tasks_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.crm_tasks_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def crm_tasks_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all tasks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter_type: Filter by task type (ID)
        :param str filter_status: Filter by task status
        :param str filter_date: Filter by date
        :param str filter_assign_to: Filter by assignTo id
        :param str filter_contacts: Filter by contact ids
        :param str filter_deals: Filter by deals ids
        :param str filter_companies: Filter by companies ids
        :param int date_from: dateFrom to date range filter type (timestamp in milliseconds)
        :param int date_to: dateTo to date range filter type (timestamp in milliseconds)
        :param int offset: Index of the first document of the page
        :param int limit: Number of documents per page
        :param str sort: Sort the results in the ascending/descending order. Default order is **descending** by creation if `sort` is not passed
        :param str sort_by: The field used to sort field names.
        :return: TaskList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_type', 'filter_status', 'filter_date', 'filter_assign_to', 'filter_contacts', 'filter_deals', 'filter_companies', 'date_from', 'date_to', 'offset', 'limit', 'sort', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method crm_tasks_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_type' in params:
            query_params.append(('filter[type]', params['filter_type']))  # noqa: E501
        if 'filter_status' in params:
            query_params.append(('filter[status]', params['filter_status']))  # noqa: E501
        if 'filter_date' in params:
            query_params.append(('filter[date]', params['filter_date']))  # noqa: E501
        if 'filter_assign_to' in params:
            query_params.append(('filter[assignTo]', params['filter_assign_to']))  # noqa: E501
        if 'filter_contacts' in params:
            query_params.append(('filter[contacts]', params['filter_contacts']))  # noqa: E501
        if 'filter_deals' in params:
            query_params.append(('filter[deals]', params['filter_deals']))  # noqa: E501
        if 'filter_companies' in params:
            query_params.append(('filter[companies]', params['filter_companies']))  # noqa: E501
        if 'date_from' in params:
            query_params.append(('dateFrom', params['date_from']))  # noqa: E501
        if 'date_to' in params:
            query_params.append(('dateTo', params['date_to']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/crm/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def crm_tasks_id_delete(self, id, **kwargs):  # noqa: E501
        """Delete a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.crm_tasks_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.crm_tasks_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def crm_tasks_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method crm_tasks_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `crm_tasks_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/crm/tasks/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def crm_tasks_id_get(self, id, **kwargs):  # noqa: E501
        """Get a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.crm_tasks_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.crm_tasks_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def crm_tasks_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: Task
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method crm_tasks_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `crm_tasks_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/crm/tasks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Task',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def crm_tasks_id_patch(self, id, body, **kwargs):  # noqa: E501
        """Update a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_id_patch(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param Body7 body: Updated task details. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.crm_tasks_id_patch_with_http_info(id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.crm_tasks_id_patch_with_http_info(id, body, **kwargs)  # noqa: E501
            return data

    def crm_tasks_id_patch_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """Update a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_id_patch_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param Body7 body: Updated task details. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method crm_tasks_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `crm_tasks_id_patch`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `crm_tasks_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/crm/tasks/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def crm_tasks_post(self, body, **kwargs):  # noqa: E501
        """Create a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body6 body: Task name. (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.crm_tasks_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.crm_tasks_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def crm_tasks_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasks_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body6 body: Task name. (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method crm_tasks_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `crm_tasks_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/crm/tasks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def crm_tasktypes_get(self, **kwargs):  # noqa: E501
        """Get all task types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasktypes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TaskTypes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.crm_tasktypes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.crm_tasktypes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def crm_tasktypes_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all task types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.crm_tasktypes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TaskTypes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method crm_tasktypes_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/crm/tasktypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskTypes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)