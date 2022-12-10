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


class OntolidentifierApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_ontol_identifier_resource(self, label, **kwargs):  # noqa: E501
        """Fetches a map from CURIEs/IDs to labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ontol_identifier_resource(label, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] label: List of labels (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ontol_identifier_resource_with_http_info(label, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ontol_identifier_resource_with_http_info(label, **kwargs)  # noqa: E501
            return data

    def get_ontol_identifier_resource_with_http_info(self, label, **kwargs):  # noqa: E501
        """Fetches a map from CURIEs/IDs to labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ontol_identifier_resource_with_http_info(label, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] label: List of labels (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['label']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ontol_identifier_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'label' is set
        if ('label' not in params or
                params['label'] is None):
            raise ValueError("Missing the required parameter `label` when calling `get_ontol_identifier_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'label' in params:
            query_params.append(('label', params['label']))  # noqa: E501
            collection_formats['label'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ontol/identifier/', 'GET',
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

    def post_ontol_identifier_resource(self, label, **kwargs):  # noqa: E501
        """Fetches a map from CURIEs/IDs to labels  # noqa: E501

        Takes 'label' list argument either as a querystring argument or as a key in the POST body when content-type is application/json.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_ontol_identifier_resource(label, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] label: List of labels (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_ontol_identifier_resource_with_http_info(label, **kwargs)  # noqa: E501
        else:
            (data) = self.post_ontol_identifier_resource_with_http_info(label, **kwargs)  # noqa: E501
            return data

    def post_ontol_identifier_resource_with_http_info(self, label, **kwargs):  # noqa: E501
        """Fetches a map from CURIEs/IDs to labels  # noqa: E501

        Takes 'label' list argument either as a querystring argument or as a key in the POST body when content-type is application/json.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_ontol_identifier_resource_with_http_info(label, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] label: List of labels (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['label']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_ontol_identifier_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'label' is set
        if ('label' not in params or
                params['label'] is None):
            raise ValueError("Missing the required parameter `label` when calling `post_ontol_identifier_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'label' in params:
            query_params.append(('label', params['label']))  # noqa: E501
            collection_formats['label'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ontol/identifier/', 'POST',
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
