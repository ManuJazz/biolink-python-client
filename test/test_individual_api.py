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
from swagger_client.api.individual_api import IndividualApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIndividualApi(unittest.TestCase):
    """IndividualApi unit test stubs"""

    def setUp(self):
        self.api = IndividualApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_individual(self):
        """Test case for get_individual

        Returns list of matches  # noqa: E501
        """
        pass

    def test_get_pedigree(self):
        """Test case for get_pedigree

        Returns list of matches  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
