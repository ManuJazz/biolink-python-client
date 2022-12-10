# swagger_client.IdentifierprefixesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prefix_collection**](IdentifierprefixesApi.md#get_prefix_collection) | **GET** /identifier/prefixes/ | Returns list of prefixes
[**get_prefix_contract**](IdentifierprefixesApi.md#get_prefix_contract) | **GET** /identifier/prefixes/contract/{uri} | Returns contracted URI
[**get_prefix_expand**](IdentifierprefixesApi.md#get_prefix_expand) | **GET** /identifier/prefixes/expand/{id} | Returns expanded URI

# **get_prefix_collection**
> get_prefix_collection()

Returns list of prefixes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentifierprefixesApi()

try:
    # Returns list of prefixes
    api_instance.get_prefix_collection()
except ApiException as e:
    print("Exception when calling IdentifierprefixesApi->get_prefix_collection: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prefix_contract**
> get_prefix_contract(uri)

Returns contracted URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentifierprefixesApi()
uri = 'uri_example' # str | URI of entity to be contracted to identifier/CURIE, e.g \"http://www.informatics.jax.org/accession/MGI:1\"

try:
    # Returns contracted URI
    api_instance.get_prefix_contract(uri)
except ApiException as e:
    print("Exception when calling IdentifierprefixesApi->get_prefix_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| URI of entity to be contracted to identifier/CURIE, e.g \&quot;http://www.informatics.jax.org/accession/MGI:1\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prefix_expand**
> get_prefix_expand(id)

Returns expanded URI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentifierprefixesApi()
id = 'id_example' # str | ID of entity to be contracted to URI, e.g \"MGI:1\"

try:
    # Returns expanded URI
    api_instance.get_prefix_expand(id)
except ApiException as e:
    print("Exception when calling IdentifierprefixesApi->get_prefix_expand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of entity to be contracted to URI, e.g \&quot;MGI:1\&quot; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

