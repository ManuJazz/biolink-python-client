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


class NlpannotateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_annotate(self, **kwargs):  # noqa: E501
        """Annotate a given text using SciGraph annotator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotate(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The text content to annotate
        :param list[str] include_category: Categories to include for annotation
        :param list[str] exclude_category: Categories to exclude for annotation
        :param str min_length: The minimum number of characters in the annotated entity
        :param bool longest_only: Should only the longest entity be returned for an overlapping group
        :param bool include_abbreviation: Should abbreviations be included
        :param bool include_acronym: Should acronyms be included
        :param bool include_numbers: Should numbers be included
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_annotate_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_annotate_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_annotate_with_http_info(self, **kwargs):  # noqa: E501
        """Annotate a given text using SciGraph annotator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotate_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The text content to annotate
        :param list[str] include_category: Categories to include for annotation
        :param list[str] exclude_category: Categories to exclude for annotation
        :param str min_length: The minimum number of characters in the annotated entity
        :param bool longest_only: Should only the longest entity be returned for an overlapping group
        :param bool include_abbreviation: Should abbreviations be included
        :param bool include_acronym: Should acronyms be included
        :param bool include_numbers: Should numbers be included
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content', 'include_category', 'exclude_category', 'min_length', 'longest_only', 'include_abbreviation', 'include_acronym', 'include_numbers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_annotate" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'content' in params:
            query_params.append(('content', params['content']))  # noqa: E501
        if 'include_category' in params:
            query_params.append(('include_category', params['include_category']))  # noqa: E501
            collection_formats['include_category'] = 'multi'  # noqa: E501
        if 'exclude_category' in params:
            query_params.append(('exclude_category', params['exclude_category']))  # noqa: E501
            collection_formats['exclude_category'] = 'multi'  # noqa: E501
        if 'min_length' in params:
            query_params.append(('min_length', params['min_length']))  # noqa: E501
        if 'longest_only' in params:
            query_params.append(('longest_only', params['longest_only']))  # noqa: E501
        if 'include_abbreviation' in params:
            query_params.append(('include_abbreviation', params['include_abbreviation']))  # noqa: E501
        if 'include_acronym' in params:
            query_params.append(('include_acronym', params['include_acronym']))  # noqa: E501
        if 'include_numbers' in params:
            query_params.append(('include_numbers', params['include_numbers']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/annotate/', 'GET',
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

    def get_annotate_entities(self, **kwargs):  # noqa: E501
        """Annotate a given content using SciGraph annotator and get all entities from content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotate_entities(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The text content to annotate
        :param list[str] include_category: Categories to include for annotation
        :param list[str] exclude_category: Categories to exclude for annotation
        :param str min_length: The minimum number of characters in the annotated entity
        :param bool longest_only: Should only the longest entity be returned for an overlapping group
        :param bool include_abbreviation: Should abbreviations be included
        :param bool include_acronym: Should acronyms be included
        :param bool include_numbers: Should numbers be included
        :return: EntityAnnotationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_annotate_entities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_annotate_entities_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_annotate_entities_with_http_info(self, **kwargs):  # noqa: E501
        """Annotate a given content using SciGraph annotator and get all entities from content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotate_entities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The text content to annotate
        :param list[str] include_category: Categories to include for annotation
        :param list[str] exclude_category: Categories to exclude for annotation
        :param str min_length: The minimum number of characters in the annotated entity
        :param bool longest_only: Should only the longest entity be returned for an overlapping group
        :param bool include_abbreviation: Should abbreviations be included
        :param bool include_acronym: Should acronyms be included
        :param bool include_numbers: Should numbers be included
        :return: EntityAnnotationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content', 'include_category', 'exclude_category', 'min_length', 'longest_only', 'include_abbreviation', 'include_acronym', 'include_numbers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_annotate_entities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'content' in params:
            query_params.append(('content', params['content']))  # noqa: E501
        if 'include_category' in params:
            query_params.append(('include_category', params['include_category']))  # noqa: E501
            collection_formats['include_category'] = 'multi'  # noqa: E501
        if 'exclude_category' in params:
            query_params.append(('exclude_category', params['exclude_category']))  # noqa: E501
            collection_formats['exclude_category'] = 'multi'  # noqa: E501
        if 'min_length' in params:
            query_params.append(('min_length', params['min_length']))  # noqa: E501
        if 'longest_only' in params:
            query_params.append(('longest_only', params['longest_only']))  # noqa: E501
        if 'include_abbreviation' in params:
            query_params.append(('include_abbreviation', params['include_abbreviation']))  # noqa: E501
        if 'include_acronym' in params:
            query_params.append(('include_acronym', params['include_acronym']))  # noqa: E501
        if 'include_numbers' in params:
            query_params.append(('include_numbers', params['include_numbers']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/annotate/entities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EntityAnnotationResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_annotate(self, **kwargs):  # noqa: E501
        """Annotate a given text using SciGraph annotator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_annotate(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The text content to annotate
        :param list[str] include_category: Categories to include for annotation
        :param list[str] exclude_category: Categories to exclude for annotation
        :param str min_length: The minimum number of characters in the annotated entity
        :param bool longest_only: Should only the longest entity be returned for an overlapping group
        :param bool include_abbreviation: Should abbreviations be included
        :param bool include_acronym: Should acronyms be included
        :param bool include_numbers: Should numbers be included
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_annotate_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_annotate_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_annotate_with_http_info(self, **kwargs):  # noqa: E501
        """Annotate a given text using SciGraph annotator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_annotate_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The text content to annotate
        :param list[str] include_category: Categories to include for annotation
        :param list[str] exclude_category: Categories to exclude for annotation
        :param str min_length: The minimum number of characters in the annotated entity
        :param bool longest_only: Should only the longest entity be returned for an overlapping group
        :param bool include_abbreviation: Should abbreviations be included
        :param bool include_acronym: Should acronyms be included
        :param bool include_numbers: Should numbers be included
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content', 'include_category', 'exclude_category', 'min_length', 'longest_only', 'include_abbreviation', 'include_acronym', 'include_numbers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_annotate" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'content' in params:
            query_params.append(('content', params['content']))  # noqa: E501
        if 'include_category' in params:
            query_params.append(('include_category', params['include_category']))  # noqa: E501
            collection_formats['include_category'] = 'multi'  # noqa: E501
        if 'exclude_category' in params:
            query_params.append(('exclude_category', params['exclude_category']))  # noqa: E501
            collection_formats['exclude_category'] = 'multi'  # noqa: E501
        if 'min_length' in params:
            query_params.append(('min_length', params['min_length']))  # noqa: E501
        if 'longest_only' in params:
            query_params.append(('longest_only', params['longest_only']))  # noqa: E501
        if 'include_abbreviation' in params:
            query_params.append(('include_abbreviation', params['include_abbreviation']))  # noqa: E501
        if 'include_acronym' in params:
            query_params.append(('include_acronym', params['include_acronym']))  # noqa: E501
        if 'include_numbers' in params:
            query_params.append(('include_numbers', params['include_numbers']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/annotate/', 'POST',
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

    def post_annotate_entities(self, **kwargs):  # noqa: E501
        """Annotate a given content using SciGraph annotator and get all entities from content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_annotate_entities(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The text content to annotate
        :param list[str] include_category: Categories to include for annotation
        :param list[str] exclude_category: Categories to exclude for annotation
        :param str min_length: The minimum number of characters in the annotated entity
        :param bool longest_only: Should only the longest entity be returned for an overlapping group
        :param bool include_abbreviation: Should abbreviations be included
        :param bool include_acronym: Should acronyms be included
        :param bool include_numbers: Should numbers be included
        :return: EntityAnnotationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_annotate_entities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_annotate_entities_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_annotate_entities_with_http_info(self, **kwargs):  # noqa: E501
        """Annotate a given content using SciGraph annotator and get all entities from content  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_annotate_entities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content: The text content to annotate
        :param list[str] include_category: Categories to include for annotation
        :param list[str] exclude_category: Categories to exclude for annotation
        :param str min_length: The minimum number of characters in the annotated entity
        :param bool longest_only: Should only the longest entity be returned for an overlapping group
        :param bool include_abbreviation: Should abbreviations be included
        :param bool include_acronym: Should acronyms be included
        :param bool include_numbers: Should numbers be included
        :return: EntityAnnotationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content', 'include_category', 'exclude_category', 'min_length', 'longest_only', 'include_abbreviation', 'include_acronym', 'include_numbers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_annotate_entities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'content' in params:
            query_params.append(('content', params['content']))  # noqa: E501
        if 'include_category' in params:
            query_params.append(('include_category', params['include_category']))  # noqa: E501
            collection_formats['include_category'] = 'multi'  # noqa: E501
        if 'exclude_category' in params:
            query_params.append(('exclude_category', params['exclude_category']))  # noqa: E501
            collection_formats['exclude_category'] = 'multi'  # noqa: E501
        if 'min_length' in params:
            query_params.append(('min_length', params['min_length']))  # noqa: E501
        if 'longest_only' in params:
            query_params.append(('longest_only', params['longest_only']))  # noqa: E501
        if 'include_abbreviation' in params:
            query_params.append(('include_abbreviation', params['include_abbreviation']))  # noqa: E501
        if 'include_acronym' in params:
            query_params.append(('include_acronym', params['include_acronym']))  # noqa: E501
        if 'include_numbers' in params:
            query_params.append(('include_numbers', params['include_numbers']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/nlp/annotate/entities', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EntityAnnotationResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)