# swagger_client.OntollabelerApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ontol_labeler_resource**](OntollabelerApi.md#get_ontol_labeler_resource) | **GET** /ontol/labeler/ | Fetches a map from CURIEs/IDs to labels

# **get_ontol_labeler_resource**
> get_ontol_labeler_resource(id)

Fetches a map from CURIEs/IDs to labels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntollabelerApi()
id = ['id_example'] # list[str] | List of ids

try:
    # Fetches a map from CURIEs/IDs to labels
    api_instance.get_ontol_labeler_resource(id)
except ApiException as e:
    print("Exception when calling OntollabelerApi->get_ontol_labeler_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| List of ids | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

