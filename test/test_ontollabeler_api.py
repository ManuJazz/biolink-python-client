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
from swagger_client.api.ontollabeler_api import OntollabelerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOntollabelerApi(unittest.TestCase):
    """OntollabelerApi unit test stubs"""

    def setUp(self):
        self.api = OntollabelerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_ontol_labeler_resource(self):
        """Test case for get_ontol_labeler_resource

        Fetches a map from CURIEs/IDs to labels  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()