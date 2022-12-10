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
from swagger_client.api.evidencegraph_api import EvidencegraphApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEvidencegraphApi(unittest.TestCase):
    """EvidencegraphApi unit test stubs"""

    def setUp(self):
        self.api = EvidencegraphApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_evidence_graph_object(self):
        """Test case for get_evidence_graph_object

        Returns evidence graph object for a given association  # noqa: E501
        """
        pass

    def test_get_evidence_graph_table(self):
        """Test case for get_evidence_graph_table

        Returns evidence as a association_results object given an association  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()