# swagger_client.BioentitysetslimmerApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_set_anatomy_slimmer**](BioentitysetslimmerApi.md#get_entity_set_anatomy_slimmer) | **GET** /bioentityset/slimmer/anatomy | For a given gene(s), summarize its annotations over a defined set of slim
[**get_entity_set_function_slimmer**](BioentitysetslimmerApi.md#get_entity_set_function_slimmer) | **GET** /bioentityset/slimmer/function | For a given gene(s), summarize its annotations over a defined set of slim
[**get_entity_set_phenotype_slimmer**](BioentitysetslimmerApi.md#get_entity_set_phenotype_slimmer) | **GET** /bioentityset/slimmer/phenotype | For a given gene(s), summarize its annotations over a defined set of slim

# **get_entity_set_anatomy_slimmer**
> get_entity_set_anatomy_slimmer(subject, slim, exclude_automatic_assertions=exclude_automatic_assertions, rows=rows, start=start)

For a given gene(s), summarize its annotations over a defined set of slim

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetslimmerApi()
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
exclude_automatic_assertions = false # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)

try:
    # For a given gene(s), summarize its annotations over a defined set of slim
    api_instance.get_entity_set_anatomy_slimmer(subject, slim, exclude_automatic_assertions=exclude_automatic_assertions, rows=rows, start=start)
except ApiException as e:
    print("Exception when calling BioentitysetslimmerApi->get_entity_set_anatomy_slimmer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_set_function_slimmer**
> get_entity_set_function_slimmer(subject, slim, relationship_type=relationship_type, exclude_automatic_assertions=exclude_automatic_assertions, rows=rows, start=start)

For a given gene(s), summarize its annotations over a defined set of slim

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetslimmerApi()
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
relationship_type = 'acts_upstream_of_or_within' # str | relationship type ('involved_in' or 'acts_upstream_of_or_within') (optional) (default to acts_upstream_of_or_within)
exclude_automatic_assertions = false # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)

try:
    # For a given gene(s), summarize its annotations over a defined set of slim
    api_instance.get_entity_set_function_slimmer(subject, slim, relationship_type=relationship_type, exclude_automatic_assertions=exclude_automatic_assertions, rows=rows, start=start)
except ApiException as e:
    print("Exception when calling BioentitysetslimmerApi->get_entity_set_function_slimmer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | 
 **relationship_type** | **str**| relationship type (&#x27;involved_in&#x27; or &#x27;acts_upstream_of_or_within&#x27;) | [optional] [default to acts_upstream_of_or_within]
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_set_phenotype_slimmer**
> get_entity_set_phenotype_slimmer(subject, slim, exclude_automatic_assertions=exclude_automatic_assertions, rows=rows, start=start)

For a given gene(s), summarize its annotations over a defined set of slim

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetslimmerApi()
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
exclude_automatic_assertions = false # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional) (default to false)
rows = 100 # int | number of rows (optional) (default to 100)
start = 56 # int | beginning row (optional)

try:
    # For a given gene(s), summarize its annotations over a defined set of slim
    api_instance.get_entity_set_phenotype_slimmer(subject, slim, exclude_automatic_assertions=exclude_automatic_assertions, rows=rows, start=start)
except ApiException as e:
    print("Exception when calling BioentitysetslimmerApi->get_entity_set_phenotype_slimmer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **rows** | **int**| number of rows | [optional] [default to 100]
 **start** | **int**| beginning row | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

