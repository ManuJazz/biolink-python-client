# swagger_client.EvidencegraphApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_evidence_graph_object**](EvidencegraphApi.md#get_evidence_graph_object) | **GET** /evidence/graph/{id} | Returns evidence graph object for a given association
[**get_evidence_graph_table**](EvidencegraphApi.md#get_evidence_graph_table) | **GET** /evidence/graph/{id}/table | Returns evidence as a association_results object given an association

# **get_evidence_graph_object**
> list[Graph] get_evidence_graph_object(id)

Returns evidence graph object for a given association

Note that every association is assumed to have a unique ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvidencegraphApi()
id = 'id_example' # str | association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada

try:
    # Returns evidence graph object for a given association
    api_response = api_instance.get_evidence_graph_object(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvidencegraphApi->get_evidence_graph_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada | 

### Return type

[**list[Graph]**](Graph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evidence_graph_table**
> list[AssociationResults] get_evidence_graph_table(id, is_publication=is_publication)

Returns evidence as a association_results object given an association

Note that every association is assumed to have a unique ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvidencegraphApi()
id = 'id_example' # str | association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada
is_publication = false # bool | If true, considers dc:source as edge (optional) (default to false)

try:
    # Returns evidence as a association_results object given an association
    api_response = api_instance.get_evidence_graph_table(id, is_publication=is_publication)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvidencegraphApi->get_evidence_graph_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada | 
 **is_publication** | **bool**| If true, considers dc:source as edge | [optional] [default to false]

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

