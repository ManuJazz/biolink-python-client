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
from swagger_client.api.pairsim_api import PairsimApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPairsimApi(unittest.TestCase):
    """PairsimApi unit test stubs"""

    def setUp(self):
        self.api = PairsimApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_pair_sim_jaccard_resource(self):
        """Test case for get_pair_sim_jaccard_resource

        Get pairwise similarity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
