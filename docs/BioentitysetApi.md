# swagger_client.BioentitysetApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_set_associations**](BioentitysetApi.md#get_entity_set_associations) | **GET** /bioentityset/associations | Returns compact associations for a given input set
[**get_entity_set_graph_resource**](BioentitysetApi.md#get_entity_set_graph_resource) | **GET** /bioentityset/graph | TODO Graph object spanning all entities
[**get_entity_set_summary**](BioentitysetApi.md#get_entity_set_summary) | **GET** /bioentityset/descriptor/counts | Summary statistics for objects associated
[**get_over_representation**](BioentitysetApi.md#get_over_representation) | **GET** /bioentityset/overrepresentation | Summary statistics for objects associated

# **get_entity_set_associations**
> list[AssociationResults] get_entity_set_associations(subject=subject, background=background, object_category=object_category, object_slim=object_slim)

Returns compact associations for a given input set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetApi()
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
background = ['background_example'] # list[str] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests (optional)
object_category = 'object_category_example' # str | E.g. phenotype, function (optional)
object_slim = 'object_slim_example' # str | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED (optional)

try:
    # Returns compact associations for a given input set
    api_response = api_instance.get_entity_set_associations(subject=subject, background=background, object_category=object_category, object_slim=object_slim)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentitysetApi->get_entity_set_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **background** | [**list[str]**](str.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **object_category** | **str**| E.g. phenotype, function | [optional] 
 **object_slim** | **str**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_set_graph_resource**
> get_entity_set_graph_resource(subject=subject, background=background, object_category=object_category, object_slim=object_slim)

TODO Graph object spanning all entities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetApi()
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
background = ['background_example'] # list[str] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests (optional)
object_category = 'object_category_example' # str | E.g. phenotype, function (optional)
object_slim = 'object_slim_example' # str | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED (optional)

try:
    # TODO Graph object spanning all entities
    api_instance.get_entity_set_graph_resource(subject=subject, background=background, object_category=object_category, object_slim=object_slim)
except ApiException as e:
    print("Exception when calling BioentitysetApi->get_entity_set_graph_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **background** | [**list[str]**](str.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **object_category** | **str**| E.g. phenotype, function | [optional] 
 **object_slim** | **str**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_set_summary**
> get_entity_set_summary(subject=subject, background=background, object_category=object_category, object_slim=object_slim)

Summary statistics for objects associated

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetApi()
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
background = ['background_example'] # list[str] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests (optional)
object_category = 'object_category_example' # str | E.g. phenotype, function (optional)
object_slim = 'object_slim_example' # str | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED (optional)

try:
    # Summary statistics for objects associated
    api_instance.get_entity_set_summary(subject=subject, background=background, object_category=object_category, object_slim=object_slim)
except ApiException as e:
    print("Exception when calling BioentitysetApi->get_entity_set_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **background** | [**list[str]**](str.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **object_category** | **str**| E.g. phenotype, function | [optional] 
 **object_slim** | **str**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_over_representation**
> get_over_representation(object_category=object_category, subject=subject, background=background, subject_category=subject_category, max_p_value=max_p_value, ontology=ontology, taxon=taxon)

Summary statistics for objects associated

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetApi()
object_category = 'object_category_example' # str | E.g. phenotype, function (optional)
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
background = ['background_example'] # list[str] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests (optional)
subject_category = 'gene' # str | Default: gene. Other types may be used e.g. disease but statistics may not make sense (optional) (default to gene)
max_p_value = '0.05' # str | Exclude results with p-value greater than this (optional) (default to 0.05)
ontology = 'ontology_example' # str | ontology id. Must be obo id. Examples: go, mp, hp, uberon (optional: will be inferred if left blank) (optional)
taxon = 'taxon_example' # str | must be NCBITaxon CURIE. Example: NCBITaxon:9606 (optional)

try:
    # Summary statistics for objects associated
    api_instance.get_over_representation(object_category=object_category, subject=subject, background=background, subject_category=subject_category, max_p_value=max_p_value, ontology=ontology, taxon=taxon)
except ApiException as e:
    print("Exception when calling BioentitysetApi->get_over_representation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_category** | **str**| E.g. phenotype, function | [optional] 
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **background** | [**list[str]**](str.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **subject_category** | **str**| Default: gene. Other types may be used e.g. disease but statistics may not make sense | [optional] [default to gene]
 **max_p_value** | **str**| Exclude results with p-value greater than this | [optional] [default to 0.05]
 **ontology** | **str**| ontology id. Must be obo id. Examples: go, mp, hp, uberon (optional: will be inferred if left blank) | [optional] 
 **taxon** | **str**| must be NCBITaxon CURIE. Example: NCBITaxon:9606 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

