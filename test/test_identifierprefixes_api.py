# coding: utf-8

"""
    BioLink API

    API integration layer for linked biological objects.   __Source:__ https://github.com/biolink/biolink-api/  # noqa: E501

    OpenAPI spec version: 1.1.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.identifierprefixes_api import IdentifierprefixesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIdentifierprefixesApi(unittest.TestCase):
    """IdentifierprefixesApi unit test stubs"""

    def setUp(self):
        self.api = IdentifierprefixesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_prefix_collection(self):
        """Test case for get_prefix_collection

        Returns list of prefixes  # noqa: E501
        """
        pass

    def test_get_prefix_contract(self):
        """Test case for get_prefix_contract

        Returns contracted URI  # noqa: E501
        """
        pass

    def test_get_prefix_expand(self):
        """Test case for get_prefix_expand

        Returns expanded URI  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
