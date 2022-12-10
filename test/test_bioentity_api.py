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
from swagger_client.api.bioentity_api import BioentityApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBioentityApi(unittest.TestCase):
    """BioentityApi unit test stubs"""

    def setUp(self):
        self.api = BioentityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_anatomy_gene_associations(self):
        """Test case for get_anatomy_gene_associations

        Returns genes associated with a given anatomy  # noqa: E501
        """
        pass

    def test_get_anatomy_gene_by_taxon_associations(self):
        """Test case for get_anatomy_gene_by_taxon_associations

        Returns gene IDs for all genes associated with a given anatomy, filtered by taxon  # noqa: E501
        """
        pass

    def test_get_case_disease_associations(self):
        """Test case for get_case_disease_associations

        Returns diseases associated with a case  # noqa: E501
        """
        pass

    def test_get_case_genotype_associations(self):
        """Test case for get_case_genotype_associations

        Returns genotypes associated with a case  # noqa: E501
        """
        pass

    def test_get_case_model_associations(self):
        """Test case for get_case_model_associations

        Returns models associated with a case  # noqa: E501
        """
        pass

    def test_get_case_phenotype_associations(self):
        """Test case for get_case_phenotype_associations

        Returns phenotypes associated with a case  # noqa: E501
        """
        pass

    def test_get_case_variant_associations(self):
        """Test case for get_case_variant_associations

        Returns variants associated with a case  # noqa: E501
        """
        pass

    def test_get_disease_case_associations(self):
        """Test case for get_disease_case_associations

        Returns cases associated with a disease  # noqa: E501
        """
        pass

    def test_get_disease_gene_associations(self):
        """Test case for get_disease_gene_associations

        Returns genes associated with a disease  # noqa: E501
        """
        pass

    def test_get_disease_genotype_associations(self):
        """Test case for get_disease_genotype_associations

        Returns genotypes associated with a disease  # noqa: E501
        """
        pass

    def test_get_disease_model_associations(self):
        """Test case for get_disease_model_associations

        Returns associations to models of the disease  # noqa: E501
        """
        pass

    def test_get_disease_model_taxon_associations(self):
        """Test case for get_disease_model_taxon_associations

        Returns associations to models of the disease constrained by taxon  # noqa: E501
        """
        pass

    def test_get_disease_pathway_associations(self):
        """Test case for get_disease_pathway_associations

        Returns pathways associated with a disease  # noqa: E501
        """
        pass

    def test_get_disease_phenotype_associations(self):
        """Test case for get_disease_phenotype_associations

        Returns phenotypes associated with disease  # noqa: E501
        """
        pass

    def test_get_disease_publication_associations(self):
        """Test case for get_disease_publication_associations

        Returns publications associated with a disease  # noqa: E501
        """
        pass

    def test_get_disease_substance_associations(self):
        """Test case for get_disease_substance_associations

        Returns substances associated with a disease  # noqa: E501
        """
        pass

    def test_get_disease_variant_associations(self):
        """Test case for get_disease_variant_associations

        Returns variants associated with a disease  # noqa: E501
        """
        pass

    def test_get_function_associations(self):
        """Test case for get_function_associations

        Returns annotations associated to a function term  # noqa: E501
        """
        pass

    def test_get_function_gene_associations(self):
        """Test case for get_function_gene_associations

        Returns genes associated to a GO term  # noqa: E501
        """
        pass

    def test_get_function_publication_associations(self):
        """Test case for get_function_publication_associations

        Returns publications associated to a GO term  # noqa: E501
        """
        pass

    def test_get_function_taxon_associations(self):
        """Test case for get_function_taxon_associations

        Returns taxons associated to a GO term  # noqa: E501
        """
        pass

    def test_get_gene_anatomy_associations(self):
        """Test case for get_gene_anatomy_associations

        Returns anatomical entities associated with a gene  # noqa: E501
        """
        pass

    def test_get_gene_case_associations(self):
        """Test case for get_gene_case_associations

        Returns cases associated with a gene  # noqa: E501
        """
        pass

    def test_get_gene_disease_associations(self):
        """Test case for get_gene_disease_associations

        Returns diseases associated with gene  # noqa: E501
        """
        pass

    def test_get_gene_expression_associations(self):
        """Test case for get_gene_expression_associations

        Returns expression events for a gene  # noqa: E501
        """
        pass

    def test_get_gene_function_associations(self):
        """Test case for get_gene_function_associations

        Returns function associations for a gene  # noqa: E501
        """
        pass

    def test_get_gene_genotype_associations(self):
        """Test case for get_gene_genotype_associations

        Returns genotypes associated with a gene  # noqa: E501
        """
        pass

    def test_get_gene_homolog_associations(self):
        """Test case for get_gene_homolog_associations

        Returns homologs for a gene  # noqa: E501
        """
        pass

    def test_get_gene_interactions(self):
        """Test case for get_gene_interactions

        Returns interactions for a gene  # noqa: E501
        """
        pass

    def test_get_gene_model_associations(self):
        """Test case for get_gene_model_associations

        Returns models associated with a gene  # noqa: E501
        """
        pass

    def test_get_gene_ortholog_disease_associations(self):
        """Test case for get_gene_ortholog_disease_associations

        Return diseases associated with orthologs of a gene  # noqa: E501
        """
        pass

    def test_get_gene_ortholog_phenotype_associations(self):
        """Test case for get_gene_ortholog_phenotype_associations

        Return phenotypes associated with orthologs for a gene  # noqa: E501
        """
        pass

    def test_get_gene_pathway_associations(self):
        """Test case for get_gene_pathway_associations

        Returns pathways associated with gene  # noqa: E501
        """
        pass

    def test_get_gene_phenotype_associations(self):
        """Test case for get_gene_phenotype_associations

        Returns phenotypes associated with gene  # noqa: E501
        """
        pass

    def test_get_gene_publication_associations(self):
        """Test case for get_gene_publication_associations

        Returns publications associated with a gene  # noqa: E501
        """
        pass

    def test_get_gene_variant_associations(self):
        """Test case for get_gene_variant_associations

        Returns variants associated with a gene  # noqa: E501
        """
        pass

    def test_get_generic_associations(self):
        """Test case for get_generic_associations

        Returns associations for an entity regardless of the type  # noqa: E501
        """
        pass

    def test_get_generic_object(self):
        """Test case for get_generic_object

        Returns basic info on object of any type  # noqa: E501
        """
        pass

    def test_get_generic_object_by_type(self):
        """Test case for get_generic_object_by_type

        Return basic info on an object for a given type  # noqa: E501
        """
        pass

    def test_get_genotype_case_associations(self):
        """Test case for get_genotype_case_associations

        Returns cases associated with a genotype  # noqa: E501
        """
        pass

    def test_get_genotype_disease_associations(self):
        """Test case for get_genotype_disease_associations

        Returns diseases associated with a genotype  # noqa: E501
        """
        pass

    def test_get_genotype_gene_associations(self):
        """Test case for get_genotype_gene_associations

        Returns genes associated with a genotype  # noqa: E501
        """
        pass

    def test_get_genotype_genotype_associations(self):
        """Test case for get_genotype_genotype_associations

        Returns genotypes-genotype associations  # noqa: E501
        """
        pass

    def test_get_genotype_model_associations(self):
        """Test case for get_genotype_model_associations

        Returns models associated with a genotype  # noqa: E501
        """
        pass

    def test_get_genotype_phenotype_associations(self):
        """Test case for get_genotype_phenotype_associations

        Returns phenotypes associated with a genotype  # noqa: E501
        """
        pass

    def test_get_genotype_publication_associations(self):
        """Test case for get_genotype_publication_associations

        Returns publications associated with a genotype  # noqa: E501
        """
        pass

    def test_get_genotype_variant_associations(self):
        """Test case for get_genotype_variant_associations

        Returns genotypes-variant associations  # noqa: E501
        """
        pass

    def test_get_goterm_gene_associations(self):
        """Test case for get_goterm_gene_associations

        Returns associations to GO terms for a gene  # noqa: E501
        """
        pass

    def test_get_model_case_associations(self):
        """Test case for get_model_case_associations

        Returns cases associated with a model  # noqa: E501
        """
        pass

    def test_get_model_disease_associations(self):
        """Test case for get_model_disease_associations

        Returns diseases associated with a model  # noqa: E501
        """
        pass

    def test_get_model_gene_associations(self):
        """Test case for get_model_gene_associations

        Returns genes associated with a model  # noqa: E501
        """
        pass

    def test_get_model_genotype_associations(self):
        """Test case for get_model_genotype_associations

        Returns genotypes associated with a model  # noqa: E501
        """
        pass

    def test_get_model_phenotype_associations(self):
        """Test case for get_model_phenotype_associations

        Returns phenotypes associated with a model  # noqa: E501
        """
        pass

    def test_get_model_publication_associations(self):
        """Test case for get_model_publication_associations

        Returns publications associated with a model  # noqa: E501
        """
        pass

    def test_get_model_variant_associations(self):
        """Test case for get_model_variant_associations

        Returns variants associated with a model  # noqa: E501
        """
        pass

    def test_get_pathway_disease_associations(self):
        """Test case for get_pathway_disease_associations

        Returns diseases associated with a pathway  # noqa: E501
        """
        pass

    def test_get_pathway_gene_associations(self):
        """Test case for get_pathway_gene_associations

        Returns genes associated with a pathway  # noqa: E501
        """
        pass

    def test_get_pathway_phenotype_associations(self):
        """Test case for get_pathway_phenotype_associations

        Returns phenotypes associated with a pathway  # noqa: E501
        """
        pass

    def test_get_phenotype_anatomy_associations(self):
        """Test case for get_phenotype_anatomy_associations

        Returns anatomical entities associated with a phenotype  # noqa: E501
        """
        pass

    def test_get_phenotype_case_associations(self):
        """Test case for get_phenotype_case_associations

        Returns cases associated with a phenotype  # noqa: E501
        """
        pass

    def test_get_phenotype_disease_associations(self):
        """Test case for get_phenotype_disease_associations

        Returns diseases associated with a phenotype  # noqa: E501
        """
        pass

    def test_get_phenotype_gene_associations(self):
        """Test case for get_phenotype_gene_associations

        Returns genes associated with a phenotype  # noqa: E501
        """
        pass

    def test_get_phenotype_gene_by_taxon_associations(self):
        """Test case for get_phenotype_gene_by_taxon_associations

        Returns gene IDs for all genes associated with a given phenotype, filtered by taxon  # noqa: E501
        """
        pass

    def test_get_phenotype_genotype_associations(self):
        """Test case for get_phenotype_genotype_associations

        Returns genotypes associated with a phenotype  # noqa: E501
        """
        pass

    def test_get_phenotype_pathway_associations(self):
        """Test case for get_phenotype_pathway_associations

        Returns pathways associated with a phenotype  # noqa: E501
        """
        pass

    def test_get_phenotype_publication_associations(self):
        """Test case for get_phenotype_publication_associations

        Returns publications associated with a phenotype  # noqa: E501
        """
        pass

    def test_get_phenotype_variant_associations(self):
        """Test case for get_phenotype_variant_associations

        Returns variants associated with a phenotype  # noqa: E501
        """
        pass

    def test_get_publication_disease_associations(self):
        """Test case for get_publication_disease_associations

        Returns diseases associated with a publication  # noqa: E501
        """
        pass

    def test_get_publication_gene_associations(self):
        """Test case for get_publication_gene_associations

        Returns genes associated with a publication  # noqa: E501
        """
        pass

    def test_get_publication_genotype_associations(self):
        """Test case for get_publication_genotype_associations

        Returns genotypes associated with a publication  # noqa: E501
        """
        pass

    def test_get_publication_model_associations(self):
        """Test case for get_publication_model_associations

        Returns models associated with a publication  # noqa: E501
        """
        pass

    def test_get_publication_phenotype_associations(self):
        """Test case for get_publication_phenotype_associations

        Returns phenotypes associated with a publication  # noqa: E501
        """
        pass

    def test_get_publication_variant_associations(self):
        """Test case for get_publication_variant_associations

        Returns variants associated with a publication  # noqa: E501
        """
        pass

    def test_get_substance_participant_in_associations(self):
        """Test case for get_substance_participant_in_associations

        Returns associations between an activity and process and the specified substance  # noqa: E501
        """
        pass

    def test_get_substance_role_associations(self):
        """Test case for get_substance_role_associations

        Returns associations between given drug and roles  # noqa: E501
        """
        pass

    def test_get_substance_treats_associations(self):
        """Test case for get_substance_treats_associations

        Returns substances associated with a disease  # noqa: E501
        """
        pass

    def test_get_variant_case_associations(self):
        """Test case for get_variant_case_associations

        Returns cases associated with a variant  # noqa: E501
        """
        pass

    def test_get_variant_disease_associations(self):
        """Test case for get_variant_disease_associations

        Returns diseases associated with a variant  # noqa: E501
        """
        pass

    def test_get_variant_gene_associations(self):
        """Test case for get_variant_gene_associations

        Returns genes associated with a variant  # noqa: E501
        """
        pass

    def test_get_variant_genotype_associations(self):
        """Test case for get_variant_genotype_associations

        Returns genotypes associated with a variant  # noqa: E501
        """
        pass

    def test_get_variant_model_associations(self):
        """Test case for get_variant_model_associations

        Returns models associated with a variant  # noqa: E501
        """
        pass

    def test_get_variant_phenotype_associations(self):
        """Test case for get_variant_phenotype_associations

        Returns phenotypes associated with a variant  # noqa: E501
        """
        pass

    def test_get_variant_publication_associations(self):
        """Test case for get_variant_publication_associations

        Returns publications associated with a variant  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()