# swagger_client.BioentityApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_anatomy_gene_associations**](BioentityApi.md#get_anatomy_gene_associations) | **GET** /bioentity/anatomy/{id}/genes | Returns genes associated with a given anatomy
[**get_anatomy_gene_by_taxon_associations**](BioentityApi.md#get_anatomy_gene_by_taxon_associations) | **GET** /bioentity/anatomy/{id}/genes/{taxid} | Returns gene IDs for all genes associated with a given anatomy, filtered by taxon
[**get_case_disease_associations**](BioentityApi.md#get_case_disease_associations) | **GET** /bioentity/case/{id}/diseases | Returns diseases associated with a case
[**get_case_genotype_associations**](BioentityApi.md#get_case_genotype_associations) | **GET** /bioentity/case/{id}/genotypes | Returns genotypes associated with a case
[**get_case_model_associations**](BioentityApi.md#get_case_model_associations) | **GET** /bioentity/case/{id}/models | Returns models associated with a case
[**get_case_phenotype_associations**](BioentityApi.md#get_case_phenotype_associations) | **GET** /bioentity/case/{id}/phenotypes | Returns phenotypes associated with a case
[**get_case_variant_associations**](BioentityApi.md#get_case_variant_associations) | **GET** /bioentity/case/{id}/variants | Returns variants associated with a case
[**get_disease_case_associations**](BioentityApi.md#get_disease_case_associations) | **GET** /bioentity/disease/{id}/cases | Returns cases associated with a disease
[**get_disease_gene_associations**](BioentityApi.md#get_disease_gene_associations) | **GET** /bioentity/disease/{id}/genes | Returns genes associated with a disease
[**get_disease_genotype_associations**](BioentityApi.md#get_disease_genotype_associations) | **GET** /bioentity/disease/{id}/genotypes | Returns genotypes associated with a disease
[**get_disease_model_associations**](BioentityApi.md#get_disease_model_associations) | **GET** /bioentity/disease/{id}/models | Returns associations to models of the disease
[**get_disease_model_taxon_associations**](BioentityApi.md#get_disease_model_taxon_associations) | **GET** /bioentity/disease/{id}/models/{taxon} | Returns associations to models of the disease constrained by taxon
[**get_disease_pathway_associations**](BioentityApi.md#get_disease_pathway_associations) | **GET** /bioentity/disease/{id}/pathways | Returns pathways associated with a disease
[**get_disease_phenotype_associations**](BioentityApi.md#get_disease_phenotype_associations) | **GET** /bioentity/disease/{id}/phenotypes | Returns phenotypes associated with disease
[**get_disease_publication_associations**](BioentityApi.md#get_disease_publication_associations) | **GET** /bioentity/disease/{id}/publications | Returns publications associated with a disease
[**get_disease_substance_associations**](BioentityApi.md#get_disease_substance_associations) | **GET** /bioentity/disease/{id}/treatment | Returns substances associated with a disease
[**get_disease_variant_associations**](BioentityApi.md#get_disease_variant_associations) | **GET** /bioentity/disease/{id}/variants | Returns variants associated with a disease
[**get_function_associations**](BioentityApi.md#get_function_associations) | **GET** /bioentity/function/{id} | Returns annotations associated to a function term
[**get_function_gene_associations**](BioentityApi.md#get_function_gene_associations) | **GET** /bioentity/function/{id}/genes | Returns genes associated to a GO term
[**get_function_publication_associations**](BioentityApi.md#get_function_publication_associations) | **GET** /bioentity/function/{id}/publications | Returns publications associated to a GO term
[**get_function_taxon_associations**](BioentityApi.md#get_function_taxon_associations) | **GET** /bioentity/function/{id}/taxons | Returns taxons associated to a GO term
[**get_gene_anatomy_associations**](BioentityApi.md#get_gene_anatomy_associations) | **GET** /bioentity/gene/{id}/anatomy | Returns anatomical entities associated with a gene
[**get_gene_case_associations**](BioentityApi.md#get_gene_case_associations) | **GET** /bioentity/gene/{id}/cases | Returns cases associated with a gene
[**get_gene_disease_associations**](BioentityApi.md#get_gene_disease_associations) | **GET** /bioentity/gene/{id}/diseases | Returns diseases associated with gene
[**get_gene_expression_associations**](BioentityApi.md#get_gene_expression_associations) | **GET** /bioentity/gene/{id}/expression/anatomy | Returns expression events for a gene
[**get_gene_function_associations**](BioentityApi.md#get_gene_function_associations) | **GET** /bioentity/gene/{id}/function | Returns function associations for a gene
[**get_gene_genotype_associations**](BioentityApi.md#get_gene_genotype_associations) | **GET** /bioentity/gene/{id}/genotypes | Returns genotypes associated with a gene
[**get_gene_homolog_associations**](BioentityApi.md#get_gene_homolog_associations) | **GET** /bioentity/gene/{id}/homologs | Returns homologs for a gene
[**get_gene_interactions**](BioentityApi.md#get_gene_interactions) | **GET** /bioentity/gene/{id}/interactions | Returns interactions for a gene
[**get_gene_model_associations**](BioentityApi.md#get_gene_model_associations) | **GET** /bioentity/gene/{id}/models | Returns models associated with a gene
[**get_gene_ortholog_disease_associations**](BioentityApi.md#get_gene_ortholog_disease_associations) | **GET** /bioentity/gene/{id}/ortholog/diseases | Return diseases associated with orthologs of a gene
[**get_gene_ortholog_phenotype_associations**](BioentityApi.md#get_gene_ortholog_phenotype_associations) | **GET** /bioentity/gene/{id}/ortholog/phenotypes | Return phenotypes associated with orthologs for a gene
[**get_gene_pathway_associations**](BioentityApi.md#get_gene_pathway_associations) | **GET** /bioentity/gene/{id}/pathways | Returns pathways associated with gene
[**get_gene_phenotype_associations**](BioentityApi.md#get_gene_phenotype_associations) | **GET** /bioentity/gene/{id}/phenotypes | Returns phenotypes associated with gene
[**get_gene_publication_associations**](BioentityApi.md#get_gene_publication_associations) | **GET** /bioentity/gene/{id}/publications | Returns publications associated with a gene
[**get_gene_variant_associations**](BioentityApi.md#get_gene_variant_associations) | **GET** /bioentity/gene/{id}/variants | Returns variants associated with a gene
[**get_generic_associations**](BioentityApi.md#get_generic_associations) | **GET** /bioentity/{id}/associations | Returns associations for an entity regardless of the type
[**get_generic_object**](BioentityApi.md#get_generic_object) | **GET** /bioentity/{id} | Returns basic info on object of any type
[**get_generic_object_by_type**](BioentityApi.md#get_generic_object_by_type) | **GET** /bioentity/{type}/{id} | Return basic info on an object for a given type
[**get_genotype_case_associations**](BioentityApi.md#get_genotype_case_associations) | **GET** /bioentity/genotype/{id}/cases | Returns cases associated with a genotype
[**get_genotype_disease_associations**](BioentityApi.md#get_genotype_disease_associations) | **GET** /bioentity/genotype/{id}/diseases | Returns diseases associated with a genotype
[**get_genotype_gene_associations**](BioentityApi.md#get_genotype_gene_associations) | **GET** /bioentity/genotype/{id}/genes | Returns genes associated with a genotype
[**get_genotype_genotype_associations**](BioentityApi.md#get_genotype_genotype_associations) | **GET** /bioentity/genotype/{id}/genotypes | Returns genotypes-genotype associations
[**get_genotype_model_associations**](BioentityApi.md#get_genotype_model_associations) | **GET** /bioentity/genotype/{id}/models | Returns models associated with a genotype
[**get_genotype_phenotype_associations**](BioentityApi.md#get_genotype_phenotype_associations) | **GET** /bioentity/genotype/{id}/phenotypes | Returns phenotypes associated with a genotype
[**get_genotype_publication_associations**](BioentityApi.md#get_genotype_publication_associations) | **GET** /bioentity/genotype/{id}/publications | Returns publications associated with a genotype
[**get_genotype_variant_associations**](BioentityApi.md#get_genotype_variant_associations) | **GET** /bioentity/genotype/{id}/variants | Returns genotypes-variant associations
[**get_goterm_gene_associations**](BioentityApi.md#get_goterm_gene_associations) | **GET** /bioentity/goterm/{id}/genes | Returns associations to GO terms for a gene
[**get_model_case_associations**](BioentityApi.md#get_model_case_associations) | **GET** /bioentity/model/{id}/cases | Returns cases associated with a model
[**get_model_disease_associations**](BioentityApi.md#get_model_disease_associations) | **GET** /bioentity/model/{id}/diseases | Returns diseases associated with a model
[**get_model_gene_associations**](BioentityApi.md#get_model_gene_associations) | **GET** /bioentity/model/{id}/genes | Returns genes associated with a model
[**get_model_genotype_associations**](BioentityApi.md#get_model_genotype_associations) | **GET** /bioentity/model/{id}/genotypes | Returns genotypes associated with a model
[**get_model_phenotype_associations**](BioentityApi.md#get_model_phenotype_associations) | **GET** /bioentity/model/{id}/phenotypes | Returns phenotypes associated with a model
[**get_model_publication_associations**](BioentityApi.md#get_model_publication_associations) | **GET** /bioentity/model/{id}/publications | Returns publications associated with a model
[**get_model_variant_associations**](BioentityApi.md#get_model_variant_associations) | **GET** /bioentity/model/{id}/variants | Returns variants associated with a model
[**get_pathway_disease_associations**](BioentityApi.md#get_pathway_disease_associations) | **GET** /bioentity/pathway/{id}/diseases | Returns diseases associated with a pathway
[**get_pathway_gene_associations**](BioentityApi.md#get_pathway_gene_associations) | **GET** /bioentity/pathway/{id}/genes | Returns genes associated with a pathway
[**get_pathway_phenotype_associations**](BioentityApi.md#get_pathway_phenotype_associations) | **GET** /bioentity/pathway/{id}/phenotypes | Returns phenotypes associated with a pathway
[**get_phenotype_anatomy_associations**](BioentityApi.md#get_phenotype_anatomy_associations) | **GET** /bioentity/phenotype/{id}/anatomy | Returns anatomical entities associated with a phenotype
[**get_phenotype_case_associations**](BioentityApi.md#get_phenotype_case_associations) | **GET** /bioentity/phenotype/{id}/cases | Returns cases associated with a phenotype
[**get_phenotype_disease_associations**](BioentityApi.md#get_phenotype_disease_associations) | **GET** /bioentity/phenotype/{id}/diseases | Returns diseases associated with a phenotype
[**get_phenotype_gene_associations**](BioentityApi.md#get_phenotype_gene_associations) | **GET** /bioentity/phenotype/{id}/genes | Returns genes associated with a phenotype
[**get_phenotype_gene_by_taxon_associations**](BioentityApi.md#get_phenotype_gene_by_taxon_associations) | **GET** /bioentity/phenotype/{id}/gene/{taxid}/ids | Returns gene IDs for all genes associated with a given phenotype, filtered by taxon
[**get_phenotype_genotype_associations**](BioentityApi.md#get_phenotype_genotype_associations) | **GET** /bioentity/phenotype/{id}/genotypes | Returns genotypes associated with a phenotype
[**get_phenotype_pathway_associations**](BioentityApi.md#get_phenotype_pathway_associations) | **GET** /bioentity/phenotype/{id}/pathways | Returns pathways associated with a phenotype
[**get_phenotype_publication_associations**](BioentityApi.md#get_phenotype_publication_associations) | **GET** /bioentity/phenotype/{id}/publications | Returns publications associated with a phenotype
[**get_phenotype_variant_associations**](BioentityApi.md#get_phenotype_variant_associations) | **GET** /bioentity/phenotype/{id}/variants | Returns variants associated with a phenotype
[**get_publication_disease_associations**](BioentityApi.md#get_publication_disease_associations) | **GET** /bioentity/publication/{id}/diseases | Returns diseases associated with a publication
[**get_publication_gene_associations**](BioentityApi.md#get_publication_gene_associations) | **GET** /bioentity/publication/{id}/genes | Returns genes associated with a publication
[**get_publication_genotype_associations**](BioentityApi.md#get_publication_genotype_associations) | **GET** /bioentity/publication/{id}/genotypes | Returns genotypes associated with a publication
[**get_publication_model_associations**](BioentityApi.md#get_publication_model_associations) | **GET** /bioentity/publication/{id}/models | Returns models associated with a publication
[**get_publication_phenotype_associations**](BioentityApi.md#get_publication_phenotype_associations) | **GET** /bioentity/publication/{id}/phenotypes | Returns phenotypes associated with a publication
[**get_publication_variant_associations**](BioentityApi.md#get_publication_variant_associations) | **GET** /bioentity/publication/{id}/variants | Returns variants associated with a publication
[**get_substance_participant_in_associations**](BioentityApi.md#get_substance_participant_in_associations) | **GET** /bioentity/substance/{id}/participant_in | Returns associations between an activity and process and the specified substance
[**get_substance_role_associations**](BioentityApi.md#get_substance_role_associations) | **GET** /bioentity/substance/{id}/roles | Returns associations between given drug and roles
[**get_substance_treats_associations**](BioentityApi.md#get_substance_treats_associations) | **GET** /bioentity/substance/{id}/treats | Returns substances associated with a disease
[**get_variant_case_associations**](BioentityApi.md#get_variant_case_associations) | **GET** /bioentity/variant/{id}/cases | Returns cases associated with a variant
[**get_variant_disease_associations**](BioentityApi.md#get_variant_disease_associations) | **GET** /bioentity/variant/{id}/diseases | Returns diseases associated with a variant
[**get_variant_gene_associations**](BioentityApi.md#get_variant_gene_associations) | **GET** /bioentity/variant/{id}/genes | Returns genes associated with a variant
[**get_variant_genotype_associations**](BioentityApi.md#get_variant_genotype_associations) | **GET** /bioentity/variant/{id}/genotypes | Returns genotypes associated with a variant
[**get_variant_model_associations**](BioentityApi.md#get_variant_model_associations) | **GET** /bioentity/variant/{id}/models | Returns models associated with a variant
[**get_variant_phenotype_associations**](BioentityApi.md#get_variant_phenotype_associations) | **GET** /bioentity/variant/{id}/phenotypes | Returns phenotypes associated with a variant
[**get_variant_publication_associations**](BioentityApi.md#get_variant_publication_associations) | **GET** /bioentity/variant/{id}/publications | Returns publications associated with a variant

# **get_anatomy_gene_associations**
> AssociationResults get_anatomy_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genes associated with a given anatomy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genes associated with a given anatomy
    api_response = api_instance.get_anatomy_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_anatomy_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anatomy_gene_by_taxon_associations**
> get_anatomy_gene_by_taxon_associations(taxid, id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns gene IDs for all genes associated with a given anatomy, filtered by taxon

For example, + NCBITaxon:10090 (mouse)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
taxid = 'taxid_example' # str | Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus)
id = 'id_example' # str | CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns gene IDs for all genes associated with a given anatomy, filtered by taxon
    api_instance.get_anatomy_gene_by_taxon_associations(taxid, id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
except ApiException as e:
    print("Exception when calling BioentityApi->get_anatomy_gene_by_taxon_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxid** | **str**| Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus) | 
 **id** | **str**| CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_disease_associations**
> AssociationResults get_case_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns diseases associated with a case

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a case
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns diseases associated with a case
    api_response = api_instance.get_case_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_case_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a case | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_genotype_associations**
> AssociationResults get_case_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns genotypes associated with a case

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a case
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns genotypes associated with a case
    api_response = api_instance.get_case_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_case_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a case | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_model_associations**
> AssociationResults get_case_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns models associated with a case

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a case
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns models associated with a case
    api_response = api_instance.get_case_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_case_model_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a case | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_phenotype_associations**
> AssociationResults get_case_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns phenotypes associated with a case

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a case
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns phenotypes associated with a case
    api_response = api_instance.get_case_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_case_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a case | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_variant_associations**
> AssociationResults get_case_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns variants associated with a case

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a case
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns variants associated with a case
    api_response = api_instance.get_case_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_case_variant_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a case | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_case_associations**
> AssociationResults get_disease_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns cases associated with a disease

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. MONDO:0007103, MONDO:0010918. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns cases associated with a disease
    api_response = api_instance.get_disease_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_case_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. MONDO:0007103, MONDO:0010918. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_gene_associations**
> AssociationResults get_disease_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q, association_type=association_type)

Returns genes associated with a disease

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)
association_type = 'both' # str | Additional filters: causal, non_causal, both (optional) (default to both)

try:
    # Returns genes associated with a disease
    api_response = api_instance.get_disease_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q, association_type=association_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 
 **association_type** | **str**| Additional filters: causal, non_causal, both | [optional] [default to both]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_genotype_associations**
> AssociationResults get_disease_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genotypes associated with a disease

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. Orphanet:399158, DOID:0080008. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genotypes associated with a disease
    api_response = api_instance.get_disease_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. Orphanet:399158, DOID:0080008. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_model_associations**
> AssociationResults get_disease_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns associations to models of the disease

In the association object returned, the subject will be the disease, and the object will be the model. The model may be a gene or genetic element.  If the query disease is a general class, the association subject may be to a specific disease.  In some cases the association will be *direct*, for example if a paper asserts a genotype is a model of a disease.  In other cases, the association will be *indirect*, for example, chaining over orthology. In these cases the chain will be reflected in the *evidence graph*  * TODO: provide hook into owlsim for dynamic computation of models by similarity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns associations to models of the disease
    api_response = api_instance.get_disease_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_model_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_model_taxon_associations**
> AssociationResults get_disease_model_taxon_associations(taxon, id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns associations to models of the disease constrained by taxon

See /disease/<id>/models route for full details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
taxon = 'taxon_example' # str | CURIE of organism taxonomy class to constrain models, e.g NCBITaxon:10090 (M. musculus).   Higher level taxa may be used
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns associations to models of the disease constrained by taxon
    api_response = api_instance.get_disease_model_taxon_associations(taxon, id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_model_taxon_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| CURIE of organism taxonomy class to constrain models, e.g NCBITaxon:10090 (M. musculus).   Higher level taxa may be used | 
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_pathway_associations**
> AssociationResults get_disease_pathway_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns pathways associated with a disease

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. DOID:4450. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns pathways associated with a disease
    api_response = api_instance.get_disease_pathway_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_pathway_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. DOID:4450. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_phenotype_associations**
> D2PAssociationResults get_disease_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns phenotypes associated with disease

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, Orphanet:1934, DOID:678. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns phenotypes associated with disease
    api_response = api_instance.get_disease_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, Orphanet:1934, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**D2PAssociationResults**](D2PAssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_publication_associations**
> AssociationResults get_disease_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns publications associated with a disease

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns publications associated with a disease
    api_response = api_instance.get_disease_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_publication_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_substance_associations**
> get_disease_substance_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns substances associated with a disease

e.g. drugs or small molecules used to treat

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. DOID:2841 (asthma). Equivalent IDs not yet supported
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns substances associated with a disease
    api_instance.get_disease_substance_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_substance_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. DOID:2841 (asthma). Equivalent IDs not yet supported | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_variant_associations**
> AssociationResults get_disease_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns variants associated with a disease

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns variants associated with a disease
    api_response = api_instance.get_disease_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_variant_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_associations**
> get_function_associations(id, start=start, rows=rows, evidence=evidence)

Returns annotations associated to a function term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of a function term (e.g. GO:0044598)
start = 0 # int | beginning row (optional) (default to 0)
rows = 100 # int | number of rows (optional) (default to 100)
evidence = ['evidence_example'] # list[str] | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)

try:
    # Returns annotations associated to a function term
    api_instance.get_function_associations(id, start=start, rows=rows, evidence=evidence)
except ApiException as e:
    print("Exception when calling BioentityApi->get_function_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of a function term (e.g. GO:0044598) | 
 **start** | **int**| beginning row | [optional] [default to 0]
 **rows** | **int**| number of rows | [optional] [default to 100]
 **evidence** | [**list[str]**](str.md)| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_gene_associations**
> AssociationResults get_function_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q, relationship_type=relationship_type)

Returns genes associated to a GO term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of a GO term, e.g. GO:0044598
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)
relationship_type = 'involved_in' # str | relationship type ('involved_in', 'involved_in_regulation_of' or 'acts_upstream_of_or_within') (optional) (default to involved_in)

try:
    # Returns genes associated to a GO term
    api_response = api_instance.get_function_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q, relationship_type=relationship_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_function_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of a GO term, e.g. GO:0044598 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 
 **relationship_type** | **str**| relationship type (&#x27;involved_in&#x27;, &#x27;involved_in_regulation_of&#x27; or &#x27;acts_upstream_of_or_within&#x27;) | [optional] [default to involved_in]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_publication_associations**
> get_function_publication_associations(id, start=start, rows=rows, evidence=evidence)

Returns publications associated to a GO term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of a GO term, e.g. GO:0044598
start = 0 # int | beginning row (optional) (default to 0)
rows = 100 # int | number of rows (optional) (default to 100)
evidence = ['evidence_example'] # list[str] | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)

try:
    # Returns publications associated to a GO term
    api_instance.get_function_publication_associations(id, start=start, rows=rows, evidence=evidence)
except ApiException as e:
    print("Exception when calling BioentityApi->get_function_publication_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of a GO term, e.g. GO:0044598 | 
 **start** | **int**| beginning row | [optional] [default to 0]
 **rows** | **int**| number of rows | [optional] [default to 100]
 **evidence** | [**list[str]**](str.md)| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_taxon_associations**
> get_function_taxon_associations(id, start=start, rows=rows, evidence=evidence)

Returns taxons associated to a GO term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of a GO term, e.g. GO:0044598
start = 0 # int | beginning row (optional) (default to 0)
rows = 100 # int | number of rows (optional) (default to 100)
evidence = ['evidence_example'] # list[str] | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)

try:
    # Returns taxons associated to a GO term
    api_instance.get_function_taxon_associations(id, start=start, rows=rows, evidence=evidence)
except ApiException as e:
    print("Exception when calling BioentityApi->get_function_taxon_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of a GO term, e.g. GO:0044598 | 
 **start** | **int**| beginning row | [optional] [default to 0]
 **rows** | **int**| number of rows | [optional] [default to 100]
 **evidence** | [**list[str]**](str.md)| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_anatomy_associations**
> AssociationResults get_gene_anatomy_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns anatomical entities associated with a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:13434
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns anatomical entities associated with a gene
    api_response = api_instance.get_gene_anatomy_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_anatomy_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:13434 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_case_associations**
> AssociationResults get_gene_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns cases associated with a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. HGNC:613, HGNC:11025
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns cases associated with a gene
    api_response = api_instance.get_gene_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_case_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. HGNC:613, HGNC:11025 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_disease_associations**
> AssociationResults get_gene_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q, association_type=association_type)

Returns diseases associated with gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)
association_type = 'both' # str | Additional filters: causal, non_causal, both (optional) (default to both)

try:
    # Returns diseases associated with gene
    api_response = api_instance.get_gene_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q, association_type=association_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 
 **association_type** | **str**| Additional filters: causal, non_causal, both | [optional] [default to both]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_expression_associations**
> AssociationResults get_gene_expression_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns expression events for a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns expression events for a gene
    api_response = api_instance.get_gene_expression_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_expression_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_function_associations**
> AssociationResults get_gene_function_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns function associations for a gene

IMPLEMENTATION DETAILS ----------------------  Note: currently this is implemented as a query to the GO/AmiGO solr instance. This directly supports IDs such as:   - ZFIN e.g. ZFIN:ZDB-GENE-050417-357  Note that the AmiGO GOlr natively stores MGI annotations to MGI:MGI:nn. However, the standard for biolink is MGI:nnnn, so you should use this (will be transparently mapped to legacy ID)  Additionally, for some species such as Human, GO has the annotation attached to the UniProt ID. Again, this should be transparently handled; e.g. you can use NCBIGene:6469, and this will be mapped behind the scenes for querying.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id, e.g. NCBIGene:6469. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns function associations for a gene
    api_response = api_instance.get_gene_function_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_function_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id, e.g. NCBIGene:6469. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_genotype_associations**
> AssociationResults get_gene_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genotypes associated with a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. ZFIN:ZDB-GENE-980526-166
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genotypes associated with a gene
    api_response = api_instance.get_gene_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. ZFIN:ZDB-GENE-980526-166 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_homolog_associations**
> AssociationResults get_gene_homolog_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, homology_type=homology_type, direct_taxon=direct_taxon)

Returns homologs for a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | Taxon CURIE of homolog, e.g. NCBITaxon:9606 (Can be an ancestral node in the ontology; includes inferred associations by default) (optional)
homology_type = 'homology_type_example' # str | P (paralog), O (Ortholog) or LDO (least-diverged ortholog) (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)

try:
    # Returns homologs for a gene
    api_response = api_instance.get_gene_homolog_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, homology_type=homology_type, direct_taxon=direct_taxon)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_homolog_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| Taxon CURIE of homolog, e.g. NCBITaxon:9606 (Can be an ancestral node in the ontology; includes inferred associations by default) | [optional] 
 **homology_type** | **str**| P (paralog), O (Ortholog) or LDO (least-diverged ortholog) | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_interactions**
> AssociationResults get_gene_interactions(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns interactions for a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns interactions for a gene
    api_response = api_instance.get_gene_interactions(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_model_associations**
> AssociationResults get_gene_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns models associated with a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:17988
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns models associated with a gene
    api_response = api_instance.get_gene_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_model_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:17988 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_ortholog_disease_associations**
> AssociationResults get_gene_ortholog_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Return diseases associated with orthologs of a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Return diseases associated with orthologs of a gene
    api_response = api_instance.get_gene_ortholog_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_ortholog_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_ortholog_phenotype_associations**
> AssociationResults get_gene_ortholog_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Return phenotypes associated with orthologs for a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Return phenotypes associated with orthologs for a gene
    api_response = api_instance.get_gene_ortholog_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_ortholog_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_pathway_associations**
> AssociationResults get_gene_pathway_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns pathways associated with gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:50846. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns pathways associated with gene
    api_response = api_instance.get_gene_pathway_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_pathway_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:50846. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_phenotype_associations**
> AssociationResults get_gene_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns phenotypes associated with gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns phenotypes associated with gene
    api_response = api_instance.get_gene_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_publication_associations**
> AssociationResults get_gene_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns publications associated with a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns publications associated with a gene
    api_response = api_instance.get_gene_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_publication_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_variant_associations**
> AssociationResults get_gene_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns variants associated with a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. HGNC:10896
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns variants associated with a gene
    api_response = api_instance.get_gene_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_variant_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. HGNC:10896 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generic_associations**
> AssociationResults get_generic_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns associations for an entity regardless of the type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns associations for an entity regardless of the type
    api_response = api_instance.get_generic_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_generic_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generic_object**
> BioObject get_generic_object(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns basic info on object of any type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id, e.g. NCBIGene:84570
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns basic info on object of any type
    api_response = api_instance.get_generic_object(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_generic_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id, e.g. NCBIGene:84570 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**BioObject**](BioObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generic_object_by_type**
> get_generic_object_by_type(type, id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, get_association_counts=get_association_counts, distinct_counts=distinct_counts)

Return basic info on an object for a given type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
type = 'type_example' # str | bioentity type
id = 'id_example' # str | id, e.g. NCBIGene:84570
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
get_association_counts = false # bool | Get association counts (optional) (default to false)
distinct_counts = false # bool | Get distinct counts for associations (to be used in conjunction with 'get_association_counts' parameter) (optional) (default to false)

try:
    # Return basic info on an object for a given type
    api_instance.get_generic_object_by_type(type, id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, get_association_counts=get_association_counts, distinct_counts=distinct_counts)
except ApiException as e:
    print("Exception when calling BioentityApi->get_generic_object_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| bioentity type | 
 **id** | **str**| id, e.g. NCBIGene:84570 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **get_association_counts** | **bool**| Get association counts | [optional] [default to false]
 **distinct_counts** | **bool**| Get distinct counts for associations (to be used in conjunction with &#x27;get_association_counts&#x27; parameter) | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_case_associations**
> AssociationResults get_genotype_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns cases associated with a genotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. dbSNPIndividual:10440, dbSNPIndividual:22633
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns cases associated with a genotype
    api_response = api_instance.get_genotype_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_case_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. dbSNPIndividual:10440, dbSNPIndividual:22633 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_disease_associations**
> AssociationResults get_genotype_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns diseases associated with a genotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. dbSNPIndividual:11441 (if non-human will return models)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns diseases associated with a genotype
    api_response = api_instance.get_genotype_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. dbSNPIndividual:11441 (if non-human will return models) | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_gene_associations**
> AssociationResults get_genotype_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genes associated with a genotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genes associated with a genotype
    api_response = api_instance.get_genotype_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_genotype_associations**
> AssociationResults get_genotype_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genotypes-genotype associations

Genotypes may be related to one another according to the GENO model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genotypes-genotype associations
    api_response = api_instance.get_genotype_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_model_associations**
> AssociationResults get_genotype_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns models associated with a genotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns models associated with a genotype
    api_response = api_instance.get_genotype_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_model_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_phenotype_associations**
> AssociationResults get_genotype_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns phenotypes associated with a genotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns phenotypes associated with a genotype
    api_response = api_instance.get_genotype_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_publication_associations**
> AssociationResults get_genotype_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns publications associated with a genotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns publications associated with a genotype
    api_response = api_instance.get_genotype_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_publication_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_variant_associations**
> AssociationResults get_genotype_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genotypes-variant associations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. MONARCH:FBgeno422705
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genotypes-variant associations
    api_response = api_instance.get_genotype_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_variant_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. MONARCH:FBgeno422705 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goterm_gene_associations**
> AssociationResults get_goterm_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, relationship_type=relationship_type)

Returns associations to GO terms for a gene

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of a GO term, e.g. GO:0044598
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
relationship_type = 'involved_in' # str | relationship type ('involved_in', 'involved_in_regulation_of' or 'acts_upstream_of_or_within') (optional) (default to involved_in)

try:
    # Returns associations to GO terms for a gene
    api_response = api_instance.get_goterm_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, relationship_type=relationship_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_goterm_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of a GO term, e.g. GO:0044598 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **relationship_type** | **str**| relationship type (&#x27;involved_in&#x27;, &#x27;involved_in_regulation_of&#x27; or &#x27;acts_upstream_of_or_within&#x27;) | [optional] [default to involved_in]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_case_associations**
> AssociationResults get_model_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns cases associated with a model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a model, e.g. Coriell:GM22295, Coriell:HG02187
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns cases associated with a model
    api_response = api_instance.get_model_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_model_case_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a model, e.g. Coriell:GM22295, Coriell:HG02187 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_disease_associations**
> AssociationResults get_model_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns diseases associated with a model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a model, e.g. MGI:5573196
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns diseases associated with a model
    api_response = api_instance.get_model_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_model_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a model, e.g. MGI:5573196 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_gene_associations**
> AssociationResults get_model_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genes associated with a model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a model, e.g. MMRRC:042787
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genes associated with a model
    api_response = api_instance.get_model_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_model_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a model, e.g. MMRRC:042787 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_genotype_associations**
> AssociationResults get_model_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genotypes associated with a model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a model, e.g. Coriell:NA16660
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genotypes associated with a model
    api_response = api_instance.get_model_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_model_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a model, e.g. Coriell:NA16660 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_phenotype_associations**
> AssociationResults get_model_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns phenotypes associated with a model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns phenotypes associated with a model
    api_response = api_instance.get_model_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_model_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_publication_associations**
> AssociationResults get_model_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns publications associated with a model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a model, e.g. MGI:5644542
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns publications associated with a model
    api_response = api_instance.get_model_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_model_publication_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a model, e.g. MGI:5644542 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_variant_associations**
> AssociationResults get_model_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns variants associated with a model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a model, e.g. MMRRC:042787
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns variants associated with a model
    api_response = api_instance.get_model_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_model_variant_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a model, e.g. MMRRC:042787 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pathway_disease_associations**
> AssociationResults get_pathway_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns diseases associated with a pathway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE any pathway element. E.g. REACT:R-HSA-5387390
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns diseases associated with a pathway
    api_response = api_instance.get_pathway_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_pathway_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE any pathway element. E.g. REACT:R-HSA-5387390 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pathway_gene_associations**
> AssociationResults get_pathway_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genes associated with a pathway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE any pathway element. E.g. REACT:R-HSA-5387390
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genes associated with a pathway
    api_response = api_instance.get_pathway_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_pathway_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE any pathway element. E.g. REACT:R-HSA-5387390 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pathway_phenotype_associations**
> AssociationResults get_pathway_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns phenotypes associated with a pathway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE any pathway element. E.g. REACT:R-HSA-5387390
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns phenotypes associated with a pathway
    api_response = api_instance.get_pathway_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_pathway_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE any pathway element. E.g. REACT:R-HSA-5387390 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_anatomy_associations**
> list[NamedObject] get_phenotype_anatomy_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns anatomical entities associated with a phenotype

Example IDs:   * MP:0008521 abnormal Bowman membrane

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of phenotype, e.g. MP:0008521. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns anatomical entities associated with a phenotype
    api_response = api_instance.get_phenotype_anatomy_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_anatomy_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of phenotype, e.g. MP:0008521. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**list[NamedObject]**](NamedObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_case_associations**
> AssociationResults get_phenotype_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns cases associated with a phenotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | Pheno class CURIE identifier, e.g  HP:0011951 (Aspiration pneumonia), HP:0002450 (Abnormal motor neuron morphology)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns cases associated with a phenotype
    api_response = api_instance.get_phenotype_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_case_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Pheno class CURIE identifier, e.g  HP:0011951 (Aspiration pneumonia), HP:0002450 (Abnormal motor neuron morphology) | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_disease_associations**
> D2PAssociationResults get_phenotype_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns diseases associated with a phenotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of phenotype, e.g. HP:0007359. Equivalent IDs can be used with same results
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns diseases associated with a phenotype
    api_response = api_instance.get_phenotype_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of phenotype, e.g. HP:0007359. Equivalent IDs can be used with same results | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**D2PAssociationResults**](D2PAssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_gene_associations**
> AssociationResults get_phenotype_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genes associated with a phenotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level), 
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genes associated with a phenotype
    api_response = api_instance.get_phenotype_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level),  | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_gene_by_taxon_associations**
> get_phenotype_gene_by_taxon_associations(taxid, id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns gene IDs for all genes associated with a given phenotype, filtered by taxon

For example, MP:0001569 + NCBITaxon:10090 (mouse)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
taxid = 'taxid_example' # str | Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus)
id = 'id_example' # str | Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns gene IDs for all genes associated with a given phenotype, filtered by taxon
    api_instance.get_phenotype_gene_by_taxon_associations(taxid, id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_gene_by_taxon_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxid** | **str**| Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus) | 
 **id** | **str**| Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_genotype_associations**
> AssociationResults get_phenotype_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genotypes associated with a phenotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genotypes associated with a phenotype
    api_response = api_instance.get_phenotype_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_pathway_associations**
> AssociationResults get_phenotype_pathway_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns pathways associated with a phenotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns pathways associated with a phenotype
    api_response = api_instance.get_phenotype_pathway_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_pathway_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_publication_associations**
> AssociationResults get_phenotype_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns publications associated with a phenotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns publications associated with a phenotype
    api_response = api_instance.get_phenotype_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_publication_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_variant_associations**
> AssociationResults get_phenotype_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns variants associated with a phenotype

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns variants associated with a phenotype
    api_response = api_instance.get_phenotype_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_variant_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publication_disease_associations**
> AssociationResults get_publication_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns diseases associated with a publication

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a publication, e.g. PMID:11751940
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns diseases associated with a publication
    api_response = api_instance.get_publication_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_publication_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publication_gene_associations**
> AssociationResults get_publication_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genes associated with a publication

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a publication, e.g. PMID:11751940
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genes associated with a publication
    api_response = api_instance.get_publication_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_publication_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publication_genotype_associations**
> AssociationResults get_publication_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genotypes associated with a publication

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a publication, e.g. PMID:11751940
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genotypes associated with a publication
    api_response = api_instance.get_publication_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_publication_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publication_model_associations**
> AssociationResults get_publication_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns models associated with a publication

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a publication, e.g. PMID:11751940
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns models associated with a publication
    api_response = api_instance.get_publication_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_publication_model_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publication_phenotype_associations**
> AssociationResults get_publication_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns phenotypes associated with a publication

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a publication, e.g. PMID:11751940
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns phenotypes associated with a publication
    api_response = api_instance.get_publication_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_publication_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_publication_variant_associations**
> AssociationResults get_publication_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns variants associated with a publication

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier for a publication, e.g. PMID:11751940
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns variants associated with a publication
    api_response = api_instance.get_publication_variant_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_publication_variant_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_participant_in_associations**
> list[Association] get_substance_participant_in_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns associations between an activity and process and the specified substance

Examples relationships:   * substance is a metabolite of a process  * substance is synthesized by a process  * substance is modified by an activity  * substance elicits a response program/pathway  * substance is transported by activity or pathway  For example, CHEBI:40036 (amitrole)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of substance, e.g. CHEBI:40036
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns associations between an activity and process and the specified substance
    api_response = api_instance.get_substance_participant_in_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_participant_in_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of substance, e.g. CHEBI:40036 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_role_associations**
> list[Association] get_substance_role_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns associations between given drug and roles

Roles may be human-oriented (e.g. pesticide) or molecular (e.g. enzyme inhibitor)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of substance, e.g. CHEBI:40036
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns associations between given drug and roles
    api_response = api_instance.get_substance_role_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_role_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of substance, e.g. CHEBI:40036 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_treats_associations**
> get_substance_treats_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns substances associated with a disease

e.g. drugs or small molecules used to treat

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of substance, e.g. CHEBI:40036
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns substances associated with a disease
    api_instance.get_substance_treats_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_treats_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of substance, e.g. CHEBI:40036 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_case_associations**
> AssociationResults get_variant_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns cases associated with a variant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. OMIM:309550.0004, dbSNP:rs5030868
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns cases associated with a variant
    api_response = api_instance.get_variant_case_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_case_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. OMIM:309550.0004, dbSNP:rs5030868 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_disease_associations**
> AssociationResults get_variant_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns diseases associated with a variant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. ClinVarVariant:14925
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns diseases associated with a variant
    api_response = api_instance.get_variant_disease_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. ClinVarVariant:14925 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_gene_associations**
> AssociationResults get_variant_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genes associated with a variant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genes associated with a variant
    api_response = api_instance.get_variant_gene_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_genotype_associations**
> AssociationResults get_variant_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns genotypes associated with a variant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns genotypes associated with a variant
    api_response = api_instance.get_variant_genotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_model_associations**
> AssociationResults get_variant_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)

Returns models associated with a variant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. OMIM:607623.0012, dbSNP:rs5030868
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)

try:
    # Returns models associated with a variant
    api_response = api_instance.get_variant_model_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_model_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. OMIM:607623.0012, dbSNP:rs5030868 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_phenotype_associations**
> AssociationResults get_variant_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns phenotypes associated with a variant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns phenotypes associated with a variant
    api_response = api_instance.get_variant_phenotype_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_publication_associations**
> AssociationResults get_variant_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)

Returns publications associated with a variant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)
facet = false # bool | Enable faceting (optional) (default to false)
facet_fields = ['facet_fields_example'] # list[str] | Fields to facet on (optional)
unselect_evidence = false # bool | If true, excludes evidence objects in response (optional) (default to false)
exclude_automatic_assertions = false # bool | If true, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
fetch_objects = false # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to false)
use_compact_associations = false # bool | If true, returns results in compact associations format (optional) (default to false)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 (optional)
direct = false # bool | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False (optional) (default to false)
taxon = ['taxon_example'] # list[str] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default (optional)
direct_taxon = false # bool | Set true to exclude inferred taxa (optional) (default to false)
relation = 'relation_example' # str | A relation CURIE to filter associations (optional)
sort = 'sort_example' # str | Sorting responses <field> <desc,asc> (optional)
q = 'q_example' # str | Query string to filter documents (optional)

try:
    # Returns publications associated with a variant
    api_response = api_instance.get_variant_publication_associations(id, rows=rows, start=start, facet=facet, facet_fields=facet_fields, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, fetch_objects=fetch_objects, use_compact_associations=use_compact_associations, slim=slim, evidence=evidence, direct=direct, taxon=taxon, direct_taxon=direct_taxon, relation=relation, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_publication_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 
 **facet** | **bool**| Enable faceting | [optional] [default to false]
 **facet_fields** | [**list[str]**](str.md)| Fields to facet on | [optional] 
 **unselect_evidence** | **bool**| If true, excludes evidence objects in response | [optional] [default to false]
 **exclude_automatic_assertions** | **bool**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **bool**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**list[str]**](str.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **direct_taxon** | **bool**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **str**| A relation CURIE to filter associations | [optional] 
 **sort** | **str**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **str**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

