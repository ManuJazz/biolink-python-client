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
from swagger_client.api.relationusage_api import RelationusageApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRelationusageApi(unittest.TestCase):
    """RelationusageApi unit test stubs"""

    def setUp(self):
        self.api = RelationusageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_relation_usage_between_resource(self):
        """Test case for get_relation_usage_between_resource

        All relations used plus count of associations  # noqa: E501
        """
        pass

    def test_get_relation_usage_pivot_label_resource(self):
        """Test case for get_relation_usage_pivot_label_resource

        Relation usage count for all subj x obj category combinations, showing label  # noqa: E501
        """
        pass

    def test_get_relation_usage_pivot_resource(self):
        """Test case for get_relation_usage_pivot_resource

        Relation usage count for all subj x obj category combinations  # noqa: E501
        """
        pass

    def test_get_relation_usage_resource(self):
        """Test case for get_relation_usage_resource

        All relations used plus count of associations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
