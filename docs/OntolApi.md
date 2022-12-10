# swagger_client.OntolApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extract_ontology_subgraph_resource**](OntolApi.md#get_extract_ontology_subgraph_resource) | **GET** /ontol/subgraph/{ontology}/{node} | Extract a subgraph from an ontology
[**get_information_content_resource**](OntolApi.md#get_information_content_resource) | **GET** /ontol/information_content/{subject_category}/{object_category}/{subject_taxon} | Returns information content (IC) for a set of relevant ontology classes
[**post_extract_ontology_subgraph_resource**](OntolApi.md#post_extract_ontology_subgraph_resource) | **POST** /ontol/subgraph/{ontology}/{node} | Extract a subgraph from an ontology

# **get_extract_ontology_subgraph_resource**
> get_extract_ontology_subgraph_resource(node, ontology, cnode=cnode, include_ancestors=include_ancestors, include_descendants=include_descendants, relation=relation, include_meta=include_meta)

Extract a subgraph from an ontology

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntolApi()
node = 'node_example' # str | class ID, e.g. HP:0001288
ontology = 'ontology_example' # str | ontology ID, e.g. go, uberon, mp, hp
cnode = ['cnode_example'] # list[str] | Additional classes (optional)
include_ancestors = true # bool | Include Ancestors (optional) (default to true)
include_descendants = true # bool | Include Descendants (optional)
relation = ['relation_example'] # list[str] | Additional classes (optional)
include_meta = false # bool | Include metadata in response (optional) (default to false)

try:
    # Extract a subgraph from an ontology
    api_instance.get_extract_ontology_subgraph_resource(node, ontology, cnode=cnode, include_ancestors=include_ancestors, include_descendants=include_descendants, relation=relation, include_meta=include_meta)
except ApiException as e:
    print("Exception when calling OntolApi->get_extract_ontology_subgraph_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| class ID, e.g. HP:0001288 | 
 **ontology** | **str**| ontology ID, e.g. go, uberon, mp, hp | 
 **cnode** | [**list[str]**](str.md)| Additional classes | [optional] 
 **include_ancestors** | **bool**| Include Ancestors | [optional] [default to true]
 **include_descendants** | **bool**| Include Descendants | [optional] 
 **relation** | [**list[str]**](str.md)| Additional classes | [optional] 
 **include_meta** | **bool**| Include metadata in response | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_information_content_resource**
> get_information_content_resource(subject_category, object_category, subject_taxon, evidence=evidence)

Returns information content (IC) for a set of relevant ontology classes

``` IC = -log2( freq(t) / popSize ) ```  Here the frequency and population is calculated for a particular dataset: e.g. all human disease-phenotype associations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntolApi()
subject_category = 'subject_category_example' # str | 
object_category = 'object_category_example' # str | 
subject_taxon = 'subject_taxon_example' # str | 
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)

try:
    # Returns information content (IC) for a set of relevant ontology classes
    api_instance.get_information_content_resource(subject_category, object_category, subject_taxon, evidence=evidence)
except ApiException as e:
    print("Exception when calling OntolApi->get_information_content_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_category** | **str**|  | 
 **object_category** | **str**|  | 
 **subject_taxon** | **str**|  | 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_extract_ontology_subgraph_resource**
> post_extract_ontology_subgraph_resource(node, ontology, cnode=cnode, include_ancestors=include_ancestors, include_descendants=include_descendants, relation=relation, include_meta=include_meta)

Extract a subgraph from an ontology

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntolApi()
node = 'node_example' # str | class ID, e.g. HP:0001288
ontology = 'ontology_example' # str | ontology ID, e.g. go, uberon, mp, hp
cnode = ['cnode_example'] # list[str] | Additional classes (optional)
include_ancestors = true # bool | Include Ancestors (optional) (default to true)
include_descendants = true # bool | Include Descendants (optional)
relation = ['relation_example'] # list[str] | Additional classes (optional)
include_meta = false # bool | Include metadata in response (optional) (default to false)

try:
    # Extract a subgraph from an ontology
    api_instance.post_extract_ontology_subgraph_resource(node, ontology, cnode=cnode, include_ancestors=include_ancestors, include_descendants=include_descendants, relation=relation, include_meta=include_meta)
except ApiException as e:
    print("Exception when calling OntolApi->post_extract_ontology_subgraph_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| class ID, e.g. HP:0001288 | 
 **ontology** | **str**| ontology ID, e.g. go, uberon, mp, hp | 
 **cnode** | [**list[str]**](str.md)| Additional classes | [optional] 
 **include_ancestors** | **bool**| Include Ancestors | [optional] [default to true]
 **include_descendants** | **bool**| Include Descendants | [optional] 
 **relation** | [**list[str]**](str.md)| Additional classes | [optional] 
 **include_meta** | **bool**| Include metadata in response | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

