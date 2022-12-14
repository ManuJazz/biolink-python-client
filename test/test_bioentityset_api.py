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
from swagger_client.api.bioentityset_api import BioentitysetApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBioentitysetApi(unittest.TestCase):
    """BioentitysetApi unit test stubs"""

    def setUp(self):
        self.api = BioentitysetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_entity_set_associations(self):
        """Test case for get_entity_set_associations

        Returns compact associations for a given input set  # noqa: E501
        """
        pass

    def test_get_entity_set_graph_resource(self):
        """Test case for get_entity_set_graph_resource

        TODO Graph object spanning all entities  # noqa: E501
        """
        pass

    def test_get_entity_set_summary(self):
        """Test case for get_entity_set_summary

        Summary statistics for objects associated  # noqa: E501
        """
        pass

    def test_get_over_representation(self):
        """Test case for get_over_representation

        Summary statistics for objects associated  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
