# swagger_client.OntologyApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ontology_subset**](OntologyApi.md#get_ontology_subset) | **GET** /ontology/subset/{id} | Returns meta data of an ontology subset (slim)
[**get_ontology_term**](OntologyApi.md#get_ontology_term) | **GET** /ontology/term/{id} | Returns meta data of an ontology term
[**get_ontology_term_graph**](OntologyApi.md#get_ontology_term_graph) | **GET** /ontology/term/{id}/graph | Returns graph of an ontology term
[**get_ontology_term_subgraph**](OntologyApi.md#get_ontology_term_subgraph) | **GET** /ontology/term/{id}/subgraph | Extract a subgraph from an ontology term
[**get_ontology_term_subsets**](OntologyApi.md#get_ontology_term_subsets) | **GET** /ontology/term/{id}/subsets | Returns subsets (slims) associated to an ontology term
[**get_ontology_terms_shared_ancestor**](OntologyApi.md#get_ontology_terms_shared_ancestor) | **GET** /ontology/shared/{subject}/{object} | Returns the ancestor ontology terms shared by two ontology terms

# **get_ontology_subset**
> get_ontology_subset(id)

Returns meta data of an ontology subset (slim)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntologyApi()
id = 'id_example' # str | name of a slim subset, e.g. goslim_agr, goslim_generic

try:
    # Returns meta data of an ontology subset (slim)
    api_instance.get_ontology_subset(id)
except ApiException as e:
    print("Exception when calling OntologyApi->get_ontology_subset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| name of a slim subset, e.g. goslim_agr, goslim_generic | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ontology_term**
> get_ontology_term(id)

Returns meta data of an ontology term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntologyApi()
id = 'id_example' # str | CURIE identifier of a GO term, e.g. GO:0003677

try:
    # Returns meta data of an ontology term
    api_instance.get_ontology_term(id)
except ApiException as e:
    print("Exception when calling OntologyApi->get_ontology_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of a GO term, e.g. GO:0003677 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ontology_term_graph**
> get_ontology_term_graph(id, graph_type=graph_type)

Returns graph of an ontology term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntologyApi()
id = 'id_example' # str | CURIE identifier of a GO term, e.g. GO:0000981
graph_type = 'topology_graph' # str | graph type ('topology_graph', 'regulates_transitivity_graph' or 'neighborhood_graph') (optional) (default to topology_graph)

try:
    # Returns graph of an ontology term
    api_instance.get_ontology_term_graph(id, graph_type=graph_type)
except ApiException as e:
    print("Exception when calling OntologyApi->get_ontology_term_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of a GO term, e.g. GO:0000981 | 
 **graph_type** | **str**| graph type (&#x27;topology_graph&#x27;, &#x27;regulates_transitivity_graph&#x27; or &#x27;neighborhood_graph&#x27;) | [optional] [default to topology_graph]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ontology_term_subgraph**
> get_ontology_term_subgraph(id, cnode=cnode, include_ancestors=include_ancestors, include_descendants=include_descendants, relation=relation, include_meta=include_meta)

Extract a subgraph from an ontology term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntologyApi()
id = 'id_example' # str | CURIE identifier of a GO term, e.g. GO:0007275
cnode = ['cnode_example'] # list[str] | Additional classes (optional)
include_ancestors = true # bool | Include Ancestors (optional) (default to true)
include_descendants = true # bool | Include Descendants (optional)
relation = ['relation_example'] # list[str] | Additional classes (optional)
include_meta = false # bool | Include metadata in response (optional) (default to false)

try:
    # Extract a subgraph from an ontology term
    api_instance.get_ontology_term_subgraph(id, cnode=cnode, include_ancestors=include_ancestors, include_descendants=include_descendants, relation=relation, include_meta=include_meta)
except ApiException as e:
    print("Exception when calling OntologyApi->get_ontology_term_subgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of a GO term, e.g. GO:0007275 | 
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

# **get_ontology_term_subsets**
> get_ontology_term_subsets(id)

Returns subsets (slims) associated to an ontology term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntologyApi()
id = 'id_example' # str | CURIE identifier of a GO term, e.g. GO:0006259

try:
    # Returns subsets (slims) associated to an ontology term
    api_instance.get_ontology_term_subsets(id)
except ApiException as e:
    print("Exception when calling OntologyApi->get_ontology_term_subsets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of a GO term, e.g. GO:0006259 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ontology_terms_shared_ancestor**
> get_ontology_terms_shared_ancestor(subject, object)

Returns the ancestor ontology terms shared by two ontology terms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntologyApi()
subject = 'subject_example' # str | CURIE identifier of a GO term, e.g. GO:0006259
object = 'object_example' # str | CURIE identifier of a GO term, e.g. GO:0046483

try:
    # Returns the ancestor ontology terms shared by two ontology terms
    api_instance.get_ontology_terms_shared_ancestor(subject, object)
except ApiException as e:
    print("Exception when calling OntologyApi->get_ontology_terms_shared_ancestor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| CURIE identifier of a GO term, e.g. GO:0006259 | 
 **object** | **str**| CURIE identifier of a GO term, e.g. GO:0046483 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

