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
from swagger_client.api.ontolidentifier_api import OntolidentifierApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOntolidentifierApi(unittest.TestCase):
    """OntolidentifierApi unit test stubs"""

    def setUp(self):
        self.api = OntolidentifierApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_ontol_identifier_resource(self):
        """Test case for get_ontol_identifier_resource

        Fetches a map from CURIEs/IDs to labels  # noqa: E501
        """
        pass

    def test_post_ontol_identifier_resource(self):
        """Test case for post_ontol_identifier_resource

        Fetches a map from CURIEs/IDs to labels  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()