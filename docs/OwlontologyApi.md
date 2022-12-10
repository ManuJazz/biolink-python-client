# swagger_client.OwlontologyApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dl_query**](OwlontologyApi.md#get_dl_query) | **GET** /owl/ontology/dlquery/{query} | Placeholder - use OWLery for now
[**get_sparql_query**](OwlontologyApi.md#get_sparql_query) | **GET** /owl/ontology/sparql/{query} | Placeholder - use direct SPARQL endpoint for now

# **get_dl_query**
> list[Association] get_dl_query(query)

Placeholder - use OWLery for now

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OwlontologyApi()
query = 'query_example' # str | 

try:
    # Placeholder - use OWLery for now
    api_response = api_instance.get_dl_query(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwlontologyApi->get_dl_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sparql_query**
> list[Association] get_sparql_query(query)

Placeholder - use direct SPARQL endpoint for now

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OwlontologyApi()
query = 'query_example' # str | 

try:
    # Placeholder - use direct SPARQL endpoint for now
    api_response = api_instance.get_sparql_query(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwlontologyApi->get_sparql_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

