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
from swagger_client.api.ontol_api import OntolApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOntolApi(unittest.TestCase):
    """OntolApi unit test stubs"""

    def setUp(self):
        self.api = OntolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_extract_ontology_subgraph_resource(self):
        """Test case for get_extract_ontology_subgraph_resource

        Extract a subgraph from an ontology  # noqa: E501
        """
        pass

    def test_get_information_content_resource(self):
        """Test case for get_information_content_resource

        Returns information content (IC) for a set of relevant ontology classes  # noqa: E501
        """
        pass

    def test_post_extract_ontology_subgraph_resource(self):
        """Test case for post_extract_ontology_subgraph_resource

        Extract a subgraph from an ontology  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
