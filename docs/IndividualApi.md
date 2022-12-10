# swagger_client.IndividualApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_individual**](IndividualApi.md#get_individual) | **GET** /individual/{id} | Returns list of matches
[**get_pedigree**](IndividualApi.md#get_pedigree) | **GET** /individual/pedigree/{id} | Returns list of matches

# **get_individual**
> list[Association] get_individual(id)

Returns list of matches

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndividualApi()
id = 'id_example' # str | 

try:
    # Returns list of matches
    api_response = api_instance.get_individual(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndividualApi->get_individual: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pedigree**
> list[Association] get_pedigree(id)

Returns list of matches

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndividualApi()
id = 'id_example' # str | 

try:
    # Returns list of matches
    api_response = api_instance.get_pedigree(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndividualApi->get_pedigree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

