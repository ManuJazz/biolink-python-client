# coding: utf-8

"""
    BioLink API

    API integration layer for linked biological objects.   __Source:__ https://github.com/biolink/biolink-api/  # noqa: E501

    OpenAPI spec version: 1.1.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class IdentifierprefixesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_prefix_collection(self, **kwargs):  # noqa: E501
        """Returns list of prefixes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prefix_collection(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_prefix_collection_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_prefix_collection_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_prefix_collection_with_http_info(self, **kwargs):  # noqa: E501
        """Returns list of prefixes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prefix_collection_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method get_prefix_collection" % key
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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/identifier/prefixes/', 'GET',
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

    def get_prefix_contract(self, uri, **kwargs):  # noqa: E501
        """Returns contracted URI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prefix_contract(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: URI of entity to be contracted to identifier/CURIE, e.g \"http://www.informatics.jax.org/accession/MGI:1\" (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_prefix_contract_with_http_info(uri, **kwargs)  # noqa: E501
        else:
            (data) = self.get_prefix_contract_with_http_info(uri, **kwargs)  # noqa: E501
            return data

    def get_prefix_contract_with_http_info(self, uri, **kwargs):  # noqa: E501
        """Returns contracted URI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prefix_contract_with_http_info(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: URI of entity to be contracted to identifier/CURIE, e.g \"http://www.informatics.jax.org/accession/MGI:1\" (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prefix_contract" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uri' is set
        if ('uri' not in params or
                params['uri'] is None):
            raise ValueError("Missing the required parameter `uri` when calling `get_prefix_contract`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uri' in params:
            path_params['uri'] = params['uri']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/identifier/prefixes/contract/{uri}', 'GET',
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

    def get_prefix_expand(self, id, **kwargs):  # noqa: E501
        """Returns expanded URI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prefix_expand(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of entity to be contracted to URI, e.g \"MGI:1\" (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_prefix_expand_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_prefix_expand_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_prefix_expand_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns expanded URI  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prefix_expand_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of entity to be contracted to URI, e.g \"MGI:1\" (required)
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
                    " to method get_prefix_expand" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_prefix_expand`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/identifier/prefixes/expand/{id}', 'GET',
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
