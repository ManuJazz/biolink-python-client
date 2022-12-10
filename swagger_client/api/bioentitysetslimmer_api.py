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


class BioentitysetslimmerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_entity_set_anatomy_slimmer(self, subject, slim, **kwargs):  # noqa: E501
        """For a given gene(s), summarize its annotations over a defined set of slim  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_set_anatomy_slimmer(subject, slim, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (required)
        :param list[str] slim: Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) (required)
        :param bool exclude_automatic_assertions: If set, excludes associations that involve IEAs (ECO:0000501)
        :param int rows: number of rows
        :param int start: beginning row
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_entity_set_anatomy_slimmer_with_http_info(subject, slim, **kwargs)  # noqa: E501
        else:
            (data) = self.get_entity_set_anatomy_slimmer_with_http_info(subject, slim, **kwargs)  # noqa: E501
            return data

    def get_entity_set_anatomy_slimmer_with_http_info(self, subject, slim, **kwargs):  # noqa: E501
        """For a given gene(s), summarize its annotations over a defined set of slim  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_set_anatomy_slimmer_with_http_info(subject, slim, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (required)
        :param list[str] slim: Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) (required)
        :param bool exclude_automatic_assertions: If set, excludes associations that involve IEAs (ECO:0000501)
        :param int rows: number of rows
        :param int start: beginning row
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subject', 'slim', 'exclude_automatic_assertions', 'rows', 'start']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_entity_set_anatomy_slimmer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subject' is set
        if ('subject' not in params or
                params['subject'] is None):
            raise ValueError("Missing the required parameter `subject` when calling `get_entity_set_anatomy_slimmer`")  # noqa: E501
        # verify the required parameter 'slim' is set
        if ('slim' not in params or
                params['slim'] is None):
            raise ValueError("Missing the required parameter `slim` when calling `get_entity_set_anatomy_slimmer`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subject' in params:
            query_params.append(('subject', params['subject']))  # noqa: E501
            collection_formats['subject'] = 'multi'  # noqa: E501
        if 'slim' in params:
            query_params.append(('slim', params['slim']))  # noqa: E501
            collection_formats['slim'] = 'multi'  # noqa: E501
        if 'exclude_automatic_assertions' in params:
            query_params.append(('exclude_automatic_assertions', params['exclude_automatic_assertions']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/bioentityset/slimmer/anatomy', 'GET',
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

    def get_entity_set_function_slimmer(self, subject, slim, **kwargs):  # noqa: E501
        """For a given gene(s), summarize its annotations over a defined set of slim  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_set_function_slimmer(subject, slim, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (required)
        :param list[str] slim: Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) (required)
        :param str relationship_type: relationship type ('involved_in' or 'acts_upstream_of_or_within')
        :param bool exclude_automatic_assertions: If set, excludes associations that involve IEAs (ECO:0000501)
        :param int rows: number of rows
        :param int start: beginning row
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_entity_set_function_slimmer_with_http_info(subject, slim, **kwargs)  # noqa: E501
        else:
            (data) = self.get_entity_set_function_slimmer_with_http_info(subject, slim, **kwargs)  # noqa: E501
            return data

    def get_entity_set_function_slimmer_with_http_info(self, subject, slim, **kwargs):  # noqa: E501
        """For a given gene(s), summarize its annotations over a defined set of slim  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_set_function_slimmer_with_http_info(subject, slim, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (required)
        :param list[str] slim: Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) (required)
        :param str relationship_type: relationship type ('involved_in' or 'acts_upstream_of_or_within')
        :param bool exclude_automatic_assertions: If set, excludes associations that involve IEAs (ECO:0000501)
        :param int rows: number of rows
        :param int start: beginning row
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subject', 'slim', 'relationship_type', 'exclude_automatic_assertions', 'rows', 'start']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_entity_set_function_slimmer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subject' is set
        if ('subject' not in params or
                params['subject'] is None):
            raise ValueError("Missing the required parameter `subject` when calling `get_entity_set_function_slimmer`")  # noqa: E501
        # verify the required parameter 'slim' is set
        if ('slim' not in params or
                params['slim'] is None):
            raise ValueError("Missing the required parameter `slim` when calling `get_entity_set_function_slimmer`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'relationship_type' in params:
            query_params.append(('relationship_type', params['relationship_type']))  # noqa: E501
        if 'subject' in params:
            query_params.append(('subject', params['subject']))  # noqa: E501
            collection_formats['subject'] = 'multi'  # noqa: E501
        if 'slim' in params:
            query_params.append(('slim', params['slim']))  # noqa: E501
            collection_formats['slim'] = 'multi'  # noqa: E501
        if 'exclude_automatic_assertions' in params:
            query_params.append(('exclude_automatic_assertions', params['exclude_automatic_assertions']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/bioentityset/slimmer/function', 'GET',
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

    def get_entity_set_phenotype_slimmer(self, subject, slim, **kwargs):  # noqa: E501
        """For a given gene(s), summarize its annotations over a defined set of slim  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_set_phenotype_slimmer(subject, slim, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (required)
        :param list[str] slim: Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) (required)
        :param bool exclude_automatic_assertions: If set, excludes associations that involve IEAs (ECO:0000501)
        :param int rows: number of rows
        :param int start: beginning row
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_entity_set_phenotype_slimmer_with_http_info(subject, slim, **kwargs)  # noqa: E501
        else:
            (data) = self.get_entity_set_phenotype_slimmer_with_http_info(subject, slim, **kwargs)  # noqa: E501
            return data

    def get_entity_set_phenotype_slimmer_with_http_info(self, subject, slim, **kwargs):  # noqa: E501
        """For a given gene(s), summarize its annotations over a defined set of slim  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_set_phenotype_slimmer_with_http_info(subject, slim, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] subject: Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (required)
        :param list[str] slim: Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) (required)
        :param bool exclude_automatic_assertions: If set, excludes associations that involve IEAs (ECO:0000501)
        :param int rows: number of rows
        :param int start: beginning row
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subject', 'slim', 'exclude_automatic_assertions', 'rows', 'start']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_entity_set_phenotype_slimmer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subject' is set
        if ('subject' not in params or
                params['subject'] is None):
            raise ValueError("Missing the required parameter `subject` when calling `get_entity_set_phenotype_slimmer`")  # noqa: E501
        # verify the required parameter 'slim' is set
        if ('slim' not in params or
                params['slim'] is None):
            raise ValueError("Missing the required parameter `slim` when calling `get_entity_set_phenotype_slimmer`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subject' in params:
            query_params.append(('subject', params['subject']))  # noqa: E501
            collection_formats['subject'] = 'multi'  # noqa: E501
        if 'slim' in params:
            query_params.append(('slim', params['slim']))  # noqa: E501
            collection_formats['slim'] = 'multi'  # noqa: E501
        if 'exclude_automatic_assertions' in params:
            query_params.append(('exclude_automatic_assertions', params['exclude_automatic_assertions']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/bioentityset/slimmer/phenotype', 'GET',
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